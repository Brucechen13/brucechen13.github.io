---
layout:     post
title:      "Coursera deep learning学习笔记"
subtitle:   "S11"
date:       2017-10-11
author:     "brucechen"
header-img: "img/post-bg-ai.jpg"
published: true
tags:
    - DL
    - 读书笔记
---

### Bias和Variance
Bias指的是训练误差，Bias高说明模型在训练集中并没有训练好，欠拟合
Variance指的是测试误差，Variance高说明模型在测试集表现不好，说明泛化能力差，有可能是过拟合了

### 正则化
L1 norm
L2 norm

### Dropout
随机使若干节点的输入为0

### 梯度消失/爆炸与参数初始化
在很深的神经网络中，随着初始参数的变化，计算结果很容易过大或过小，导致梯度过大或过小。
可以使用`Xavier initialization`方法来初始化参数，相当于在参数随机初始化后除以方差，使参数在1附近，不会过大或过小。

### 梯度检验
计算实际梯度与近似梯度。