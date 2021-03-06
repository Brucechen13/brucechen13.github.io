---
layout:     post
title:      "Redis笔记"
subtitle:   ""
date:       2018-10-01
author:     "brucechen"
header-img: "img/post-bg-code.jpg"
published: true
tags:
    - Redis
    - 读书笔记
---

Redis是一个广泛使用的分布式消息队列，可以通过简单的操作实现分布式的数据存储、修改、查询、删除以及消息订阅、推送等功能。Redis功能强大，但是代码却极其简单，一共只有几万行代码，为了更好的了解Redis的设计，参考了《Redis设计与实现》一书，结合Redis3.0代码对Redis的框架进行了总结。

### ***Redis中的数据结构***

#### 简单字符串SDS

Redis中为了存储字符串，自定义了一种成为SDS(simple dynamic string)的数据类型作为默认字符串表示。

SDS结构如下：

```
struct sdshdr{
    int len;//记录已使用字节的数量
    int free;//记录未使用字节的数量
    char buf[];//字节数组，用来保存字符串
}
```

需要注意的是，为了能够直接重用C语言字符串函数库的函数，SDS的字节数组后面会自动添加空字符'\0',空字符不计算在`len`和`free`属性中。

SDS相比C语言中字符串的优点有：
  - 直接获取字符串长度
  - 不会出现缓冲区溢出的问题，当对字符串进行拼接时SDS的函数会首先判断是否需要扩容。
  - 减少修改字符串导致的内存重分配次数，SDS在拼接或截取字符串时如果修改后不超过最大长度，则直接在`buf`数组上修改即可。
  - 可以以二进制安全的方式处理数据，不会做任何限制过滤。


SDS空间扩容策略：

    当SDS需要进行空间扩展时，程序不仅需要分配所需要的空间，而且还会分配额外的未使用空间便于下次扩展。
    当SDS的长度`len`小于1MB时，程序分配和len属性同样大小的未使用空间，这是`free`属性值和`len`属性值一样。当`len`大于1MB时，只会分配1MB空间。
    当SDS字符串需要缩短时，不需要分配新的空间，只需要修改free字段即可。


#### 链表

链表作为一种常用数据结构，可以快速增删元素以及顺序性节点访问和，在很多问题上都具有较高的性能。由于C原因不提供链接的实现，所以Redis实现了自己的双向链表结构。

链表结构如下：

```
struct listNode{
    struct listNode *prev;  //前置节点
    struct listNode *next; //后置节点
    void *value; // 节点的值
}

struct list{
    listNode *head; //表头节点
    listNode *tail; //表尾节点
    long len; //节点数量
}
```

Redis实现的链表结构具有如下特性：
 -  双向链表，每个节点都可以获得自己的前置节点和后置节点
 -  存在表头指针和表尾指针
 -  无环，表头节点的prev指针和表尾节点的next指针都指向NULL，对链表的访问以NULL为终点。
 -  带有链表计数器，可以O(1)时间获得链表节点的数量


#### 字典

字典也是一种常用的数据结构，可以保存键值对的映射关系。C语言中同样没有内置这种数据结构，所以Redis自己实现了字典结构。

字典的结构如下：

```
struct dictEntry{
    void *key; //键
    union v; //值
    dictEntry *next; //下一个哈希表节点
}
struct dictht{
    dictEntry **table; //哈希表数组
    long size; // 哈希表大小
    long sizemask; //哈希表大小掩码
    long used; //已有节点的数量
}
struct dict{
    dictType *type; //类型特定的相关函数
    void *privdata; //私有数据
    dictht ht[2]; //哈希表
    int trehashidx; //rehash索引
}
```

可以看出Redis的字典采用Hash+链表的方式实现，类似于JAVA中的HashMap，不同之处在于，Redis对字典在rehash的时候通过复制的方式来避免冲突。

当下列两种情况发生时，程序会自动对哈希表进行扩展操作：
  1.    服务器没有执行`BGSAVE`或者`BGREWRITEAOF`命令，并且哈希表的负载因子大于等于1
  2.    服务器正在执行`BGSAVE`或者`BGREWRITEAOF`命令，并且哈希表的负载因子大于等于5

负载因子为`ht[0].used / ht[0].size`

Redis中的**rehash**过程：

    随着操作不断进行，哈希表保存的键值对会逐渐的增多或减少，为了让哈希表的负载因子维持在合理的范围内，需要对哈希表进行相应的扩展或收缩。
    当扩展时，为ht[1]分配第一个大于等于ht[0].used*2 的2的n次幂的大小。收缩时，分配第一个大于等于ht[0].used的2的n次幂的大小
    将保存到ht[0]的所有键值rehash到ht[1]上，迁移完成后释放ht[0],将ht[1]设置为ht[0]

实际中，rehash的动作并不是一次性集中性完成的，而是分多次、渐进性完成的。

渐进式rehash:

1. 为ht[1]分配空间，让字典同时持有ht[0], ht[1]两个哈希表
2. 维持索引计数器`rehashidx`，置0，表示rehash正式开始。
3. rehash过程中，每次对字典进行添加删除查找或者更新操作时，除了会执行相应操作外，还会将ht[0]哈希表在rehashidx索引上的所有键值对rehash到ht[1]上，当rehash完成后，rehashidx增1.
4. 当ht[0]所有键值对都rehash到ht[1]后，rehashidx被置为-1，表示rehash操作完成
5. 在渐进式rehash过程中，字典会同时使用ht[0]和ht[1]两个哈希表来响应对字典的操作，而且新添加到字典的键值对只会保存到ht[1],ht[0]包含的键值对只减不增。
    


#### 跳跃表

跳跃表（skiplist）是一种高效的有序数据结构，可以实现平均O(logN)，最坏O(N)复杂度的节点查找，在大部分情况下效率可以达到平衡树的标准，而且实现要更加简单。Redis使用跳跃表作为有序集合键的底层实现，如果有序集合中元素数量较多或者元素是较长的字符串。

跳跃表的结构如下：

```
struct skiplistNode{
    struct skiplistLevel{
        skiplistNode *forward; // 前进指针
        int span; // 跨度
    }level[]; // 层
    skiplistNode *backward; // 后退指针
    double score;
    object *obj; // 成员对象
}

struct skiplist{
    skiplistNode *header, *tail; // 表头节点和表尾节点
    long len; // 节点的数量
    int level; // 最大层数
}
```

跳跃表具有如下特性：

1.  每个节点的层高都是1到32的随机数，且满足幂次定律，越大的数概率越小
2.  多个节点可以包含相同的分数，但是节点的成员对象必须是唯一的
3.  节点按分数大小排序，当分数相同时，按成员对象的大小进行排序

#### 整数集合

整数集合是集合键的底层实现之一，当一个集合只包含整数且元素个数不多时，Redis就会采用整数集合作为集合键的底层实现。

整数集合的结构如下：

```
struct intset{
    int encoding; // 编码方式
    int len; // 集合元素数量
    int8 contents[]; // 保存元素的数组
}
```

虽然contents的类型是int8，但是contents数组的真正类型取决于encoding属性的值。

当需要添加新的元素到整数集合且新元素类型比现有集合的类型要长时，需要对整数集合进行升级然后添加新元素。升级就是按照新元素的类型扩展新的空间，将原有元素全部类型转换放在对应的位置，然后添加新的元素。

需要注意的是，整数集合不支持降级操作，升级后就算导致升级的新元素被删除，整数集合的编码依然不会改变。



#### 压缩列表

压缩列表是列表键和集合键的底层实现之一。当一个列表键只包含少量列表项且每个列表项要不是小整数要不是短字符串，Redis就会采用压缩列表作为底层实现。

压缩列表的结构如下:

```
struct ziplist{
    int bytes; // 记录占用内存字节数
    int tail; // 记录列表表尾节点距离起始地址的偏移
    int16 len; // 记录节点数量
    entry[] objs; // 不定长的节点
    int8 end; // 压缩列表的末端
}

strcut entry{
    int previous_entry_len; // 上一个obj的长度， 根据内容大小为1字节或5字节（第一个字节为标示位）
    int encoding; // 编码 字节数组可能是1字节2字节或5字节， 整数是1字节
    int count; // 内容 长度由encoding决定
}
```


#### 对象

前面介绍了很多底层数据结构，Redis并没有直接使用这些实现键值对数据库，而是基于这些数据结构创建了对象系统，通过对象来操作底层数据结构。
适用对象的好处是我们可以针对不同的使用场景来设置不同的数据结构实现，而且实现了基于引用计数的内存回收机制，通过引用计数实现了对象共享，对象还带有访问时间记录信息。

Redis使用对象来表示键值对，对象的结构如下：

```
struct{
    int type; // 类型
    int encoding; // 编码
    void *ptr; // 底层实现数据结构
}
```

Redis对象类型共有五种：

1.  字符串对象
2.  列表对象
3.  哈希对象
4.  集合对象
5.  有序集合对象

Redis为自己的对象系统设计了一套内存回收机制，通过引用计数技术，追踪对象的引用技术信息，在适当的时候自动释放对象进行内存回收。需要注意的是，由于Redis内部不允许对对象的引用，所以不会出现**循环引用**的问题。

除了利用引用计数进行垃圾回收，Redis还通过引用计数属性实现对象共享的功能。Redis在初始化服务器时，会创建从0到9999所有整数值的一万个字符串对象作为共享对象。

### Redis的键生存时间

通过`EXPIRE`命令或者`PEXPIRE`命令，客户端可以以秒或者毫秒级精度为数据库某个键设置生存时间，在经过指定的时间后服务器就会自动删除生存时间为0的键。

通过`EXPIREAT`命令或者`PEXPIREAT`命令，客户端可以指定某个键的过期时间。

四个命令最终都是通过转换为`PEXIREAT`命令实现的。

过期键会存储到过期字典中，当访问键时，首先检查键是否存在与过期字典中，如果存在取得键的过期时间，然后检查当前UNIX时间戳是否大于键的过期时间。

当一个键过期后，存在三种删除策略进行处理：

1.  定时删除，在设置键的过期时间同时创建一个定时器，在过期时间来临时删除键，会增加很多CPU开销
2.  惰性删除，每次访问键的时候如果判断键已经过期就删除键
3.  定期删除，每隔一段时间检查所有数据库，对过期键进行删除

Redis中实际使用惰性删除和定期删除两种策略。


### Redis的数据持久化方式

Redis是内存数据库，将所有数据都储存在内存中，所以如果不想办法将数据保存到磁盘中，一旦Redis进程退出，所有的数据都会消失。

Redis提供两种数据持久化的方法，**RDB持久化** 和 **AOF持久化** 。

#### RDB持久化

RDB持久化的方法就是将当前数据库的状态保存为RDB文件，并且可以通过RDB文件还原会数据库状态。

通过`SAVE`和`BGSAVE`两个命令可以生成RDB文件，`SAVE`命令会阻塞服务器进程，`BGSAVE`命令则会由子进程创建RDB文件。

Redis中并没有载入RDB文件的命令，当服务器启动时如果检测到RDB文件的存在就会自动载入RDB文件。需要注意的是，当服务器开启了AOF持久化功能时，服务器会优先使用AOF文件来还原数据库状态。

Redis服务器周期性操作函数`serverCron`默认每个100毫秒就会执行一次，其中一项功能就是检查过去一段时间内数据库修改的次数，如果修改次数达到设置的保存条件，就会执行`BGSAVE`命令。

RDB文件中会保存所有的数据库的所有键值对的信息。


#### AOF持久化

与RDB持久化保存数据库键值的方式不同，AOF持久化是通过保存Redis服务器执行的写命令来记录数据库状态的。

AOF持久化包括命令追加、文件写入、文件同步三部分。

### Redis的事件请求

Redis服务器是一个事件驱动程序，需要处理一下两类事件：

1. 文件事件，客户端通过套接字连接服务器，文件事件就是对套接字操作的抽象。
2. 时间事件，Redis服务器的一些操作需要在给定的时间点执行，时间事件就是服务器对这类定时操作的抽象。

#### 文件事件

Redis基于Reactor模式开发了自己的网络事件处理器，文件事件处理器通过I/O多路复用程序来同时监听多个套接字，当被监听的套接字有相应操作时，就会调用套接字之前关联好的事件处理器来处理这些事件。

文件事件处理器通过单线程运行，使用I/O多路复用程序来监听多个套接字，既实现了高性能的网络通信模型，又可以很好的保持了内部单线程设计的简单性。

Redis的I/O多路复用支持`select`,`epoll`,`evport`和`kqueue`实现，Redis程序编译时会自动选择系统中性能最好的函数库作为底层实现。

#### 时间事件

Redis的时间事件分为两类：

1. 定时事件
2. 周期性事件

Redis服务器目前只使用周期性事件，会将所有时间事件保存在一个时间无序链表中，每当时间事件执行器执行时，就会遍历整个链表，查找所有已到达的时间事件，并调用相应的事件处理器。



### 分布式Redis的设计

#### 集群

Redis集群是分布式数据库方案的实现方式，集群通过分片进行数据共享。

一个Redis集群通常由多个节点组成，刚开始时，每个节点都是相互独立的，都处于只包含自己的集群中，通过`cluster meet <ip> <port>`命令将各个独立的节点连接起来组成一个新的集群。

Redis服务器在启动时会根据 **cluster-enabled** 配置选项决定是否开启服务器的集群模式。开启集群模式下的服务器具有和单机模式下一样的功能。

Redis集群通过分片的方式保存数据库中的键值对，集群中被分为16384个槽，每个键都属于其中一个槽，每个节点可以处理人一个槽的数据。当所有槽都有节点处理时，集群处于上线状态，否则处于下线状态。当各个节点连接后，需要指定每个节点需要处理的槽，只有所有槽都分配完毕，集群才可以上线。可以通过`cluster info`命令查询集群的上线状态。

集群上线后，客户端可以发送命令，接收命令的节点首先计算出键属于哪个槽，如果槽属于其他节点处理，会向客户端返回`moved`错误，指引客户端重定向正确的节点。


#### 主从服务器

Redis中可以通过`slaveof`命令让一个服务器去复制另一个服务器，充当另一个服务器的从服务器，这样当主服务器由于意外宕机时，从服务器可以接着充当数据服务器，避免服务中断。

Redis程序在2.8版本前后对于主从服务器之间复制功能实现的发生了较大的变化。

1. 旧版复制功能的实现：
    
    Redis的复制功能分为同步和命令传播两个操作。同步操作用于将从服务器的状态更新至主服务器当前所处的状态，命令传播操作则用于主服务器数据库状态被修改导致主从服务器状态不一致时的同步。

    同步操作执行时，从服务器向主服务器发送`sync`命令，主服务器执行`BGSAVE`命令生成RDB文件发送从服务器，从服务器加载RDB文件恢复服务器状态，主服务器发送缓冲区保存的所有写命令，从服务器执行这些写命令使得主从服务器状态一致

    同步操作后，主从服务器状态一致，然而，如果主服务器收到了新的写命令后状态又会不一样，这时需要进行命令传播操作。主服务器会把收到的写命令发送给从服务器执行。

    旧版复制的缺陷是如果主从服务器中间发生了断线，那么重新连接后需要重新进行同步操作，而同步操作显然是比较耗时的。

2. 新版复制功能的实现：

    为了解决旧版复制功能的缺陷，Redis从2.8版本开始，使用`psync`代替`sync`命令来执行复制时的同步操作。`psync`命令包括完整重同步和部分重同步两种模式。其中完整重同步和`sync`命令执行步骤基本一致，而部分重同步则用于处理断线后重复制的情况。在断线重连后，主服务器只需要将断开阶段执行的写命令发送给从服务器就可以了。

    部分重同步功能由三个部分构成，主从服务器的复制偏移量，主服务器的复制积压缓冲区，服务器运行ID。主服务器每次向从服务器发送N字节数据后，就将自己的复制偏移量加上N，从服务器每次收到主服务器的N字节数据后，就将自己的复制偏移量加上N，通过比较主从服务器的复制偏移量就可以知道同步状态和缺少数据的数量。主服务器在接受写命令后除了会发送给所有从服务器，还会入队到复制积压缓冲区中。如果主从服务器复制偏移量差小于复制积压缓冲区的大小，则只需要发送缺少的写命令，否则，执行完整重同步。服务器运行ID则是为了区分主服务器有没有变化，如果重连的主服务器ID和从服务器保存的主服务器ID不一致，需要执行完整重同步。

#### 主从服务器的哨兵

主从服务器的设计是为了在主服务器由于意外下线后，服务器并不会停止服务，因此这时需要将从服务器提升为主服务器继续提供服务，Redis通过哨兵系统来监视主从服务器的状态并在主服务器下线后升级从服务器。

哨兵系统是一个运行在特殊模式下的Redis服务器，哨兵默认每10秒向被监视的主服务器发送`INFO`命令，主服务器会将自己和从服务器的信息返回。当哨兵发现主服务器返回的信息有新的从服务器时，会创建到从服务器的连接。

当被监视的主服务器在一定时间内都没有返回有效信息，哨兵会将其设为主观下线状态，并向其他哨兵询问是否同意主服务器下线。当一定数量的哨兵都同意下线后，主服务器被设为客观下线。

主服务器客观下线后，首先监视这个主服务器的所有哨兵进行协商，选出领头哨兵，对下线主服务器进行转移操作。

故障转移包括以下三个步骤：

1.  从所有从服务器中选出一个，转换为主服务器
2.  让所有从服务器改为复制新的主服务器
3.  让已下线的主服务器设置为从服务器



### Redis使用经验

#### 慎用keys

 KEYS 的速度非常快，例如，Redis在一个有1百万个key的数据库里面执行一次查询需要的时间是40毫秒 。但在一个大的数据库中使用它仍然可能造成性能问题。由于Redis是单线程处理，如果命令延时很大会对整个redis服务产生影响。

 对于Redis 2.8以上版本给我们提供了一个更好的遍历key的命令 SCAN 该命令的基本格式为`SCAN cursor [MATCH pattern] [COUNT count]`