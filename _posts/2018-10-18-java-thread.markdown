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

### Java多线程


### 线程库


### 其他组件

#### ThreadLocal

ThreadLocal可以在每个线程内部保存变量。简单用法如下：

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

ThreadLocal并不维护ThreadLocalMap，并不是一个存储数据的容器，它只是相当于一个工具包，提供了操作该容器的方法，如get、set、remove等。而ThreadLocal内部类ThreadLocalMap才是存储数据的容器，并且该容器由Thread维护。ThreadLocalMap由一个个Entry对象构成，Entry继承自`WeakReference<ThreadLocal<?>>`.

当执行set方法时，ThreadLocal首先会获取当前线程对象，然后获取当前线程的ThreadLocalMap对象。再以当前ThreadLocal对象为key，将值存储进ThreadLocalMap对象中。
get方法执行过程类似。ThreadLocal首先会获取当前线程对象，然后获取当前线程的ThreadLocalMap对象。再以当前ThreadLocal对象为key，获取对应的value。

在ThreadLocalMap中，只有key是弱引用，value仍然是一个强引用。当某一条线程中的ThreadLocal使用完毕，没有强引用指向它的时候，这个key指向的对象就会被垃圾收集器回收，从而这个key就变成了null；然而，此时value和value指向的对象之间仍然是强引用关系，只要这种关系不解除，value指向的对象永远不会被垃圾收集器回收，从而导致内存泄漏！
ThreadLocal每次操作set、get、remove操作时，ThreadLocal都会将key为null的Entry删除，从而避免内存泄漏。
因此如果一个线程运行周期较长，而且将一个大对象放入LocalThreadMap后便不再调用set、get、remove方法，此时该仍然可能会导致内存泄漏。这就需要程序员在完成ThreadLocal的使用后要养成手动调用remove的习惯，从而避免内存泄漏。