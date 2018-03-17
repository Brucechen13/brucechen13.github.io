---
layout:     post
title:      "Coursera deep learning学习笔记"
subtitle:   "S12"
date:       2017-10-22
author:     "brucechen"
header-img: "img/post-bg-ai.jpg"
published: true
tags:
    - DL
    - 读书笔记
---

### Mini Batch
对于训练数据较多的问题，每次基于整个训练集来进行训练通常会耗费较多的时间，可以将原始数据集划分为若干小的批次，每次迭代逐个训练每个小块，可以达到近似的优化效果并且大大节省时间。
批次的大小通常划分为2的次方项，通常为64-512之间。批次大小为1的成为随机梯度下降。随机梯度下降的缺点是不能有效使用矩阵计算。

### 指数加权平均
`Vt = βVt-1 + (1-β)Xt`

### 偏差纠正指数加权平均
`Vt = Vt/(1-β^t)`

### 基于动量的梯度下降吧
`Vdw = βVdw + (1-β)dw
W = W - αVdw
`

### RMSprop
`
Sdw = β2Sdw + (1-β)dw^2
W = W - αdw/sqrt(Sdw+epison)
`

### Adam梯度下降
结合之前两种，
`Vdw = βVdw + (1-β)dw
Sdw = β2Sdw + (1-β2)dw^2
Vdw-correct = Vdw/(1-β^t)
Sdw-correct = Sdw/(1-β^t)
W = W - αVdw-correct/sqrt(Sdw-correct+epison)
`

### 学习因子递降
较大的学习因子会导致训练到一定程度无法收敛，较小的学习因子又会导致训练前期不能快速收敛，所以需要动态改变学习因子，使之随训练过程逐渐减小。