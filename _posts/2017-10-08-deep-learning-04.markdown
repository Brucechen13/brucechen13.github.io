---
layout:     post
title:      "Coursera deep learning学习笔记"
subtitle:   "S04"
date:       2017-10-08
author:     "brucechen"
header-img: "img/post-bg-ai.jpg"
published: true
tags:
    - DL
    - 读书笔记
---

### 多层神经网络
`Zl=Wl*Al-1+bl
Al=g(Zl)`

### 为何多层网络有效
多层网络可以分别从不同层面获取输入数据的特征信息，从而可以更精确预测结果。
多层网络可以使用更少的节点获得某些计算结果，比如
`y = x1xorx2xorx3...xorxn`
使用多层网络可以每层只考虑两个节点的XOR运算，形成一颗满二叉树，知道根节点得到结果，需要O(log(n))的节点。
如果只允许单层隐藏层，则需要O(2^n)级别的节点数