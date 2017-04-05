---
layout:     post
title:      "Python开发中遇到的问题"
subtitle:   ""
date:       2017-04-05
author:     "brucechen"
header-img: "img/post-bg-python.jpg"
published: false
tags:
    - Python
    - 读书笔记
---

### 多线程，多进程问题

#### concurrent.futures.process.BrokenProcessPool
出现原因：没有在__main__函数中使用**ProcessPoolExecutor.map**创建进程
解决办法：将进程创建代码放入函数，在__main__函数中执行