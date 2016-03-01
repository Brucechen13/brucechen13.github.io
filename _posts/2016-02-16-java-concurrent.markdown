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
继承Thread类的方法尽管被我列为一种多线程实现方式，但Thread本质上也是实现了Runnable接口的一个实例，它代表一个线程的实例，并且，启动线程的唯一方法就是通过Thread类的start()实例方法。start()方法是一个native方法，它将启动一个新线程，并执行run()方法。

### concurrent包
ExecutorService、Callable、Future这个对象实际上都是属于Executor框架中的多线程类，用来实现带返回值的多线程。
```
public static void main(String[] args) throws ExecutionException,  
    InterruptedException {  
	int taskSize = 5;  
   // 创建一个线程池  
   ExecutorService pool = Executors.newFixedThreadPool(taskSize);  
   // 创建多个有返回值的任务  
   List<Future> list = new ArrayList<Future>();  
   for (int i = 0; i < taskSize; i++) {  
    Callable c = new MyCallable(i + " ");  
    // 执行任务并获取Future对象  
    Future f = pool.submit(c);  
    // System.out.println(">>>" + f.get().toString());  
    list.add(f);  
   }  
   // 关闭线程池  
   pool.shutdown();  
  
   // 获取所有并发任务的运行结果  
   for (Future f : list) {  
    // 从Future对象上获取任务的返回值，并输出到控制台  
    System.out.println(">>>" + f.get().toString());  
   } 
}  
}  
  
class MyCallable implements Callable<Object> {  
private String taskNum;  
  
MyCallable(String taskNum) {  
   this.taskNum = taskNum;  
}  
  
public Object call() throws Exception {  
   System.out.println(">>>" + taskNum + "任务启动");  
   Date dateTmp1 = new Date();  
   Thread.sleep(1000);  
   Date dateTmp2 = new Date();  
   long time = dateTmp2.getTime() - dateTmp1.getTime();  
   System.out.println(">>>" + taskNum + "任务终止");  
   return taskNum + "任务返回运行结果,当前任务时间【" + time + "毫秒】";  
}  
```