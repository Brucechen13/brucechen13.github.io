---
layout:     post
title:      "正则学习笔记"
subtitle:   ""
date:       2017-04-01
author:     "brucechen"
header-img: "img/post-bg-reg.jpg"
published: true
tags:
    - 正则表达式
    - 读书笔记
---

### 正则表达式规则
正则表达式可以用来匹配复杂规则的字符串，往往几行的正则表达式就可以完成其他语言几十行甚至上百行代码的工作。正则表达式在许多编程语言中都提供了支持，这里使用Python作为示例。
#### 元字符
元字符在正则表达式中十分常见，用于匹配同一类型的所有字符，常用的元字符如下：

代码|说明
-|-
.|匹配除换行符以外的任意字符
\w|匹配字母或数字或下划线或汉字
\s|匹配任意的空白符
\d|匹配数字
\b|匹配单词的开始或结束
^|匹配字符串的开始
$|匹配字符串的结束

#### 常用的限定符
限定符用于表示匹配字符的次数，如下：

代码/语法|说明
*|重复零次或更多次
+|重复一次或更多次
?|重复零次或一次
{n}|重复n次
{n,}|重复n次或更多次
{n,m}|重复n到m次

### Python正则表达式
Python中对于正则表达式的支持主要是通过re模块，常用的函数如下。
#### re.match
匹配成功返回匹配的对象，否则返回None

函数语法：
	re.match(pattern, string, flags = 0)#flags用于控制表达式匹配方式，如区分大小写、多行匹配等
	
#### re.search
扫描整个字符串返回第一个成功的匹配

函数语法：
	re.search(pattern, string, flags=0)

#### re.sub
用于替换字符串的匹配项

函数语法：
	re.sub(pattern, repl, string, count=0, flags = 0)#repl替换的字符串，也可以是函数；count匹配后替换的最大次数，默认0表示替换所有匹配
	
#### 可选标志

修饰符|描述
re.I|大小写不敏感
re.L|本地化识别匹配
re.M|多行匹配，影响^和$
re.S|是.匹配包括换行在内所有字符
re.U|根据Unicode字符集解析字符
re.X|使用更灵活格式实现正则表达式





### 正则应用案例
1. 文件查找，查找所有**test+数字.txt**的文件

	参考输入:['test001.txt', 'test02.txt', 'test003', 'test.txt', 'test001.rar']
	
	'''
	for str in strs:
		if re.match(r'.*test\d*.txt', str):
			print(str)
	'''

2. 文件名更改，更改所有**test+数字.txt**的文件名为**new+数字.txt**

	参考输入：同上
	
	'''
	s = re.match(r'(.*test)(\d*).txt', str)
    if s is not None:
        print(str)
        print(s.group(1) + " " + s.group(2))
	'''