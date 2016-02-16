---
layout:     post
title:      "Java笔记"
subtitle:   "多线程总结"
date:       2016-02-16
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### 原子操作
Java中的原子操作包括：
* 除long、double之外的基本数据类型的赋值操作
* 所有引用reference的赋值操作
* java.concurrent.Atomic.*包的所有类的一切操作

对于long和double的赋值操作时非原子操作，因为long和double所占字节数都是8，也就是64bit，在32为操作系统读写需要分为两步完成，每次取32为数据，为了保证long和double操作的原子性，需要使用volatile关键字，volatile本身不保证获取和设置的原子性，仅仅保持修改的可见性，但是java的内存模型保证声明为volatile的long和double变量的get和set操作是原子性的。

### Thread & Runnable


### concurrent包
