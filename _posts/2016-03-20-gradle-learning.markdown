---
layout:     post
title:      "Gradle使用笔记"
subtitle:   ""
date:       2016-03-20
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### Gradle是什么
Gradle是一种构建工具，类似于Maven，它抛弃了基于XML的构建脚本，取而代之的是采用一种基于Groovy的内部领域特定语言。
Gradle中，有两个基本概念 **项目** 和 **任务** ：
* 项目，构建产物（比如项目打包成jar文件或war文件）或实施产物（将项目部署到生产环境）。一个项目包括一个或多个 **任务** 。
* 任务，不可分的最小工作单元，执行构建工作（比如项目编译或执行测试）。

Gradle包含以下配置文件：
* Gradle构建脚本（build.gradle）制订了一个项目和它的任务。
* Gradle属性文件（gradle.properties）用来配置构建属性。
* Gradle设置文件（gradle.setting），如果构建多于一个项目，项目结构根目录必须加入一个设置文件，指定哪个项目参与构建。

Gradle的设计理念是所有的特性由Gradle插件提供，我们可以在build.gradle中，通过名称指定Grale插件：
```
apply plugin:'java'
```
 
### 如何使用Gradle
#### 仓库管理简介

仓库是一种存放依赖的容器，每一个项目都具备一个或多个仓库。Gradle支持以下仓库格式：
* Ivy仓库
* Maven仓库
* Flat directory仓库
