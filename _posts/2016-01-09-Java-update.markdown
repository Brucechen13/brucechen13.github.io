---
layout:     post
title:      "Java新特性"
subtitle:   "Java5到Java9的演变"
date:       2016-02-09
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

###  Java5 
* 泛型
Java的泛型属于伪泛型，只在编译前期起作用，编译后的字节码文件不会保存任何泛型信息，会通过类型擦除将类型参数替换为Object类型，并在实际使用时强制转换为目标类型。
* 枚举
EnumMap类。
* 装箱拆箱
基本数据类型转换为包装类型，包括Boolean,Byte,Short,Character,Integer,Long,Float,Double。
* 变长参数
```
private void vararg(Object... values){
}
```

* 注解
* foreach循环
for/in无法实现遍历时获取下标、遍历时删除。
* 静态导入
导入静态类，直接在静态函数中使用。
* 格式化
`java.text`包，提供了对日期、数字、字符串等的格式化。
* 多线程框架
线程池，JUC类库
* 工具类
增加了Arrays、Queue、StringBuilder类。

### Java6 
* JSR223脚本引擎
* JSR199——Java编译API
* JSR269——注解处理API
* 轻量级HttpServer

### Java7
* suppress异常
记录异常
* 捕获多个异常
* try-with-resource
不需要finally来保证流正确关闭
* JSR341-Expression Language Specification
* JSR203-New I/O 
提供了ByteBuffer、FileChanel等新增类，提高了I/O的性能。
* JSR203-InvokeDynamic
在字节码层次上支持JVM运行动态类型语言。
* Path接口、DirectoryStream、File、WatchService
* jcmd
替代jds,增加了新的功能
 + jcmd -l 
 列出所有java虚拟机
 + jcmd pid help
 显示可用的命令
 + jcmd pid VM.flags
 显示java虚拟机启动参数
* fork/join
用于并行执行任务的框架，把大任务分割成小任务，最后汇总得到任务的结果。
* Java Mission Control

### Java8
* 支持lambda表达式
* 集合的stream操作
* 提升HashMaps的性能
当hash冲突时，如果节点个数超过一定值，则不再使用链表存储，而是改换为红黑树存储。
* Date-Time包
* 丰富了java.lang和java.util包
* Concurrency

### Java9 
