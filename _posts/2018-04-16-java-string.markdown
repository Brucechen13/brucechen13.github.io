---
layout:     post
title:      "Java字符串相关笔记"
subtitle:   ""
date:       2018-04-16
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: true
tags:
    - Java
    - 读书笔记
---

### String类

String在Java中是不可变的类，类由final修饰，且内部实现的字符数组也由final修饰。

因此String的截取、拼接、字符替换等方法返回的都是新创建的对象

String的原生方法intern()可以返回当前字符串在常量池中的引用。

### StringBuilder类

继承自AbstractStringBuilder类，实现了对字符数组的抽象。

StringBuilder类是可变的,因此可以在创建以后修改内部的值。

不支持并发操作，线性不安全的。

在实际中，字符串拼接的方法基本都是线程内有效的，所以除非是需要进行线程间的字符串拼接，否则，还是应该使用StringBuilder类。

### StringBuffer类

同样继承自AbstractStringBuilder类。

StringBuffer类也是可变的，同时也是线程安全的,因此效率相对更低。

内部方法都是synchronized修饰过的，保证是同步的。

### String相关

#### String.intern() 

case 1:
```
    // 1
    String str1 = new StringBuilder("ja").append("va").toString();
    System.out.println(str1.intern() == str1);

    // 2
    String str2 = new StringBuffer("编").append("程").toString();
    System.out.println(str2.intern() == str2);

    // 3
    String str3 = new StringBuffer("编").append("程").toString();
    System.out.println(str3.intern() == str3);
```

ouput:
```
// 使用 JDK6 进行编译运行:
false, false, false
// 使用 JDK7 进行编译运行:
false, true, false
```

第一个false的原因是"java"字符串常量比较特殊, 它是固定存在字符串常量池中的, 因此 "str1.intern()" 返回的就是字符串常量池中的对象的引用, 和堆上的 str1 就自然是不相等了.

第二个在JDK6和JDK7中的区别则是由于String.intern() 方法的实现发生了变化。在 JDK6 及以前的 JDK 中，intern() 方法会把首次遇到的字符串实例 **复制** 到永久代中, 然后返回永久代中的实例。而对于 JDK7 以及之上的JDK，当遇到第一次出现的字符串时, intern() **不再复制实例**, 而是在常量池中记录首次出现的实例的引用, 并且 intern() 返回的是此实例引用。

第三个则是由于之前常量池已经存在对象，所以和新创建的堆上对象不相等。

