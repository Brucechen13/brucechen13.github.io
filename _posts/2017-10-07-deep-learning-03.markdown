---
layout:     post
title:      "Coursera deep learning学习笔记"
subtitle:   "S03"
date:       2017-10-07
author:     "brucechen"
header-img: "img/post-bg-ai.jpg"
published: true
tags:
    - DL
    - 读书笔记
---

### 神经网络概述
神经网络就是在逻辑回归的基础上，增加多个计算节点。
神经网络包括输入层、隐藏层、输出层
隐藏层具有多层，每层多个节点，每个节点都可以看成是上一层的输入经过逻辑回归得到的结果。

### 神经网络的向量化
计算代价函数时可以通过矩阵计算同时计算所有输入数据。

### 激活函数
在隐藏层和输出层所使用的激活函数有很多，具有不同的特点和使用场景。
* sigmoid, `1/1+e^-z`，输出[0~1]之间。适用于二分类的输出层，求导为`g(z)(1-g(z))`
* tanh, `(e^z-e^z-e)/(e^z+e^-z)`，输出[-1~1]之间。由于具有将输出结果规范化的功能，可以用于隐藏层。求导为`1-tanh(z)^2`
* relu, `max(0, z)`，之前两种激活函数有个问题，就是在坐标轴两侧函数的梯度很小，导致收敛很慢。求导为`0 if z < 0 else 1`
* softmax, ``

### 神经网络的梯度下降
反向传播算法，链式求导
两层神经网络，正向计算
`
Z1 = W1*X+b1
A1 = tanh(Z1)
Z2 = W2.A1+b2
A2 = sigmoid(Z2)
`
反向传播算法，链式求导
`
dZ2 = A2 - Y
dW2 = A1*dZ2
db2 = dZ2
dZ1 = (1-A1^2)*dZ2*W2
dW1 = X*dZ1
db1 = dZ1
`



