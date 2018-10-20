---
layout:     post
title:      "Java多线程笔记"
subtitle:   ""
date:       2018-10-18
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### 基本线程实现

基本线程类指的是Thread类，Runnable接口，Callable接口

具有如下常用方法：

```
    //当前线程可转让cpu控制权，让别的就绪状态线程运行（切换）
    public static Thread.yield() 
    //暂停一段时间
    public static Thread.sleep()  
    //在一个线程中调用other.join(),将等待other执行完后才继续本线程。　　　　
    public join()
    //后两个函数皆可以被打断
    public interrupte()
```


### 线程库

Java1.5提供了一个非常高效实用的多线程包:java.util.concurrent, 提供了大量高级工具,可以帮助开发者编写高效、易维护、结构清晰的Java多线程程序。

#### Executor和ExecutorService

Executor：具体Runnable任务的执行者。 

ExecutorService：一个线程池管理者。

CompletableFuture： 继承自Future，Future 以及相关使用方法提供了异步执行任务的能力，但是对于结果的获取却是很不方便，只能通过阻塞或者轮询的方式得到任务的结果。JAVA8提出的CompletableFuture，提供了非常强大的 Future 的扩展功能，可以帮助我们简化异步编程的复杂性，并且提供了函数式编程的能力，可以通过回调的方式处理计算结果，也提供了转换和组合 CompletableFuture 的方法。


#### CountDownLatch

CountDownLatch是一个同步辅助类，在完成一组正在其他线程中执行的操作之前，它允许一个或多个线程一直等待。 

CountDownLatch 是一个通用同步工具，它有很多用途。将计数 1 初始化的 CountDownLatch 用作一个简单的开/关锁存器， 在通过调用 countDown() 的线程打开入口前，所有调用 await 的线程都一直在入口处等待。 

用 N 初始化的 CountDownLatch 可以使一个线程在 N 个线程完成某项操作之前一直等待，或者使其在某项操作完成 N 次之前一直等待。 
CountDownLatch 的一个有用特性是，它不要求调用 countDown 方法的线程等到计数到达零时才继续， 
而在所有线程都能通过之前，它只是阻止任何线程继续通过一个 await。 

#### CyclicBarrier

CyclicBarrier是一个同步辅助类，它允许一组线程互相等待，直到到达某个公共屏障点。


#### ThreadLocal

ThreadLocal可以在每个线程内部保存变量。这种变量在多线程环境下访问(通过get或set方法访问)时能保证各个线程里的变量相对独立于其他线程内的变量。ThreadLocal实例通常来说都是private static类型的，用于关联线程和线程的上下文。简单用法如下：

```
    private ThreadLocal<Integer> threadLocal = new ThreadLocal<>();
    
    public void start() {
        for (int i=0; i<10; i++) {
            new Thread(new Runnable(){
                @override
                public void run(){
                    threadLocal.set(i);
                    threadLocal.get();
                    threadLocal.remove();
                }
            }).start();
        }
    }

```

ThreadLocal并不维护ThreadLocalMap，并不是一个存储数据的容器，它只是相当于一个工具包，提供了操作该容器的方法，如get、set、remove等。而ThreadLocal内部类ThreadLocalMap才是存储数据的容器，并且该容器由Thread维护。每一个Thread对象均含有一个ThreadLocalMap类型的成员变量threadLocals，它存储本线程中所有ThreadLocal对象及其对应的值。ThreadLocalMap由一个个Entry对象构成，Entry继承自`WeakReference<ThreadLocal<?>>`.

当执行set方法时，ThreadLocal首先会获取当前线程对象，然后获取当前线程的ThreadLocalMap对象。再以当前ThreadLocal对象为key，将值存储进ThreadLocalMap对象中。
get方法执行过程类似。ThreadLocal首先会获取当前线程对象，然后获取当前线程的ThreadLocalMap对象。再以当前ThreadLocal对象为key，获取对应的value。

在ThreadLocalMap中，只有key是弱引用，value仍然是一个强引用。当某一条线程中的ThreadLocal使用完毕，没有强引用指向它的时候，这个key指向的对象就会被垃圾收集器回收，从而这个key就变成了null；然而，此时value和value指向的对象之间仍然是强引用关系，只要这种关系不解除，value指向的对象永远不会被垃圾收集器回收，从而导致内存泄漏！
ThreadLocal每次操作set、get、remove操作时，ThreadLocal都会将key为null的Entry删除，从而避免内存泄漏。
因此如果一个线程运行周期较长，而且将一个大对象放入LocalThreadMap后便不再调用set、get、remove方法，此时该仍然可能会导致内存泄漏。这就需要程序员在完成ThreadLocal的使用后要养成手动调用remove的习惯，从而避免内存泄漏。

#### Lock

concurrent包中提供了三种锁：
1. ReentrantLock 可重入的意义在于持有锁的线程可以继续持有，并且要释放对等的次数后才真正释放该锁。
2. ReentrantReadWriteLock.ReadLock 可重入读锁
3. ReentrantReadWriteLock.WriteLock 可重入写锁。读和读之间不会互斥，读和写、写和读、写和写之间才会互斥

锁和synchronized一样， 两者都是为了解决同步问题，处理资源争端而产生的技术。但是锁更灵活，可以自由定义多把锁的枷锁解锁顺序（synchronized要按照先加的后解顺序）。

