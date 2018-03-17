---
layout:     post
title:      "Coursera deep learning学习笔记"
subtitle:   "S13"
date:       2017-10-22
author:     "brucechen"
header-img: "img/post-bg-ai.jpg"
published: true
tags:
    - DL
    - 读书笔记
---

### 超参的调参
判断出哪些参数属于最重要参数，哪些参数相对优先级低。
通常参数需要在一个小区间随机初始化，不应该直接在这个小区间随机，比如区间[0.9,0.999]，如果直接随机可能会导致数据分布和预期的有所不同。可以把区间转换为[1-0.1,1-0.001]，初始化[0.001, 0.1], 等价于[10^-3, 10^-1]，所以应该在[-3,-1]之间随机。
如果有足够的计算资源，还可以并行训练多组参数的模型。

### Batch-Normalization
对于神经网络来说，每层计算`zi`，计算出均值与方差，计算`zi-norm = (zi-μ)/σ`。然后`zi = theta1*zi-norm+theta2`

### Softmax
用于多分类