---
layout:     post
title:      "numpy模块笔记"
subtitle:   ""
date:       2017-04-07
author:     "brucechen"
header-img: "img/post-bg-python.jpg"
published: true
tags:
    - python
    - 读书笔记
---

### Python的numpy模块介绍
Numpy是Python的一个科学计算的库，提供了矩阵运算的功能，其一般与Scipy、matplotlib一起使用。其实，list已经提供了类似于矩阵的表示形式，不过numpy为我们提供了更多效率更高的函数。NumPy函数库中存在两种不同的数据类型（矩阵matrix和数组array），都可以用于处理行列表示的数字元素。虽然它们看起来很相似，但是在这两个数据类型上执行相同的数学运算可能得到不同的结果，其中NumPy函数库中的matrix与MATLAB中matrices等价。
Python中使用numpy十分简单，只需要
	pip install numpy

### Numpy模块功能

#### 矩阵
numpy中矩阵被表示为多维数组形式，称为ndarray。ndarray对象属性有：
* ndarray.ndim：数组的维数（即数组轴的个数），等于秩。最常见的为二维数组（矩阵）。
* ndarray.shape：数组的维度。为一个表示数组在每个维度上大小的整数元组。例如二维数组中，表示数组的“行数”和“列数”。ndarray.shape返回一个元组，这个元组的长度就是维度的数目，即ndim属性。
* ndarray.size：数组元素的总个数，等于shape属性中元组元素的乘积。
* ndarray.dtype：表示数组中元素类型的对象，可使用标准的Python类型创建或指定dtype。另外也可使用前一篇文章中介绍的NumPy提供的数据类型。
* ndarray.itemsize：数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(float64占用64个bits，每个字节长度为8，所以64/8，占用8个字节），又如，一个元素类型为complex32的数组item属性为4（32/8）。

#### 特殊矩阵

* 全零矩阵
	np.zeros( (3,4) )
* 全1矩阵
	np.ones((3,4))
* 序列矩阵，按照一定步长从开始到结尾生成矩阵
	np.arange( 10, 30, 5 )
* 单位矩阵
	np.eye(5)

#### 矩阵操作

* 矩阵元素相乘
	A*B
* 矩阵乘法
	A.dot(B)
* 矩阵转置，注意numpy对于一维的数组转置是不起作用的，在numpy中，一维的数组既不是行向量，也不是列向量，需要更改shape为(1,*)或(*,1)才可以，或者构造数组时声明为二维数组。
	C.transpose()


