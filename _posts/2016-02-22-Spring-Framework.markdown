---
layout:     post
title:      "Spring Framework Reference Documentation"
subtitle:   "中文翻译"
date:       2016-02-22
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - Spring
	- 翻译
---

[原文链接](http://docs.spring.io/spring/docs/4.3.0.BUILD-SNAPSHOT/spring-framework-reference/htmlsingle/)

Spring Framework是一个强大而且功能丰富的Java框架，所以打算通过官网教程来深入学习，再次过程中，勉强翻译一二，以为笔记。

### Spring Framework概览
Spring Framework是一个轻量级、可扩展的一站式企业级应用部署框架。然而，Spring是模块化的，允许你只是用你所需要的部分，而不用负担其他模块。你可以在顶层使用IoC容器应用于任何Web框架，也可以只是用Hibernate一体化代码、或者JDBC抽象层。Spring Framework支持声明式事务管理、RMI远程连接、Web Service和多种方式的数据持久化。也提供一个全功能的MVC框架，并且可以透明的整合AOP到你的软件中。
Spring被设计为非侵入的，意味着你的逻辑域代码并不需要依赖于框架。在你的集成层，例如数据访问层，数据访问的一些依赖和Spring的类库还是需要的。不过，将这些依赖于其他的基本代码相隔离是十分容易的。
这个文档是一个Spring Framework功能的引用指南，如果你对于这份文档有任何请求、评论或者问题，请发送到[user mailing lsit](https://groups.google.com/forum/#!forum/spring-framework-contrib)。
关于Frameworkd本身的问题应该在StackOverflow上提问(可见[https://spring.io/questions](https://spring.io/questions))。

#### 开始Spring之旅
这个使用引导提供了关于Spring Framework的详细信息，包括所有功能的综合文档，潜在概念（例如依赖注入）的背景说明。
如果你刚刚开始使用Spring，你可能需要首先通过创建一个基本的Spring Boot工程来使用Spring Framework。Spring Boot提供一个快速（而且自用）的方式去创建一个基于Spring的准备就绪的应用。它基于Spring Framework，支持配置文件，并被设计可以尽可能快的启动和运行。
你可以使用[start.spring.io](http://start.spring.io/) 去生成一个基本工程或者按照["Getting Started" guides](https://spring.io/guides) 例如[Getting Started Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/) 的步骤。不仅仅易于理解，这些引导也是非常任务集中的，大多数都是基于Spring Boot。他们也包含了来自Spring portfolio的其他工程，你可能想要考虑何时解决一个具体的问题。

#### Spring Framework简介
Spring Framework是一个为开发Java应用程序提供综合基础支持的Java平台。Spring搭建好基础以便你可以集中于应用程序的构建。
Spring允许通过简洁Java对象（POJOs）创建应用程序，并应用非侵入性企业级服务到POJOs。这种功能可以应用于Java SE项目模型和部分Java EE。
作为一个应用开发者，可以从Spring框架中获取如下收获：

* 不需要处理事务API而使Java方法执行数据库事务
* 不需要处理远端API而使本地方法变为远端程序。
* 不需要处理JMX API而使Java本地方法成为操作管理器。
* 不需要处理JMS API而使本地Java方法成为消息处理器。

2.1 依赖注入和控制反转
一个Java程序——一个宽松的可以运行在受限、嵌入式程序和N层、服务端企业级应用全域的部分——典型的有组合的对象组成合适的应用程序，因此程序的对象彼此间存在依赖。


### Spring Framework4新功能

### 核心技术

### 测试

### 数据访问

### 网络

### 一体化