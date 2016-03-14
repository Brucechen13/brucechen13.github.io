---
layout:     post
title:      "线程本地存储与ThreadLocal"
subtitle:   ""
date:       2016-01-24
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### 线程本地存储(Thread Local Storage)
如果一段共享数据的代码可以保证在同一个线程执行，就可以把共享数据的可见范围限制在同一个线程之内，不需要其他同步操作来保证共享数据的安全性。
Java中可以通过ThreadLocal实现类似的线程本地存储，ThreadLocal 不是用于解决共享变量的问题，不是为了协调线程同步而存在，而是为了方便每个线程处理自己的状态而引入的一个机制。ThreadLocal类接口提供了四个方法：
* void set(T value)，设置当前线程的线程局部变量的值。
* public T get()，该方法返回当前线程所对应的线程局部变量。
* public void remove()，将当前线程局部变量的值删除，目的是为了减少内存的占用，该方法是JDK 5.0新增的方法。需要指出的是，当线程结束后，对应该线程的局部变量将自动被垃圾回收，所以显式调用该方法清除线程的局部变量并不是必须的操作，但它可以加快内存回收的速度。
* protected T initialValue()，返回该线程局部变量的初始值，该方法是一个protected的方法，显然是为了让子类覆盖而设计的。这个方法是一个延迟调用方法，在线程第1次调用get()或set()时才执行，并且仅执行1次。ThreadLocal中的缺省实现直接返回一个null。

### ThreadLocal与线程同步机制的区别
ThreadLocal 不是用于解决共享变量的问题，不是为了协调线程同步而存在，而是为了方便每个线程处理自己的状态而引入的一个机制