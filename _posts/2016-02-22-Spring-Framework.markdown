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
尽管Java平台提供丰富的应用程序开发组建，依然缺乏组织基本构建快成为清晰的整体，并将这个任务留给设计师或开发者的概念。尽管你可以使用一些类似工厂模式、抽象工厂模式、建造者模式、装饰模式和服务定位器模式等设计模式来这个不同的类和对象生成，并去构建一个程序，这些设计模式虽然通过名字可以清晰看出功能和应用的地方，你仍然必须自己在应用中自己实现它们。
Spring Framework的控制反转(IoC)组件
2.2 模块
Spring Framework通过大约20个模块来实现功能，这些模块被分组为Core Container,Data Access/Integration,Web,AOP,Instrumentation,Messaging,Test。如下图：

![java-javascript](/img/in-post/spring/spring_module.png)
<small class="img-hint">spring modules</small>

接下来将介绍每个功能的具体模块及他们的组件名称和功能。组件名和组件ID的对应关系见[Dependency Management tools](http://docs.spring.io/spring/docs/4.3.0.BUILD-SNAPSHOT/spring-framework-reference/htmlsingle/#dependency-management) 

2.2.1 Core Container
核心容器包括`spring-core, spring-beans, spring-context, spring-context-support, and spring-expression(Spring表达式语言)`模块。
`spring-core`和`spring-beans`模块提供了整个框架基础的功能，包括IoC和依赖注入功能。`BeanFactory`是工厂模式的一个经典实现，它移除了程序中对单例的需求，允许你将程序逻辑的具体依赖和配置解耦。
上下文模块(`spring-context`)构建与Core和Beans模块的基础之上。类似于JNDI，通过一种框架式的方法关联对象。上下文模块继承Beans模块的功能，并增加了国际化、事件传播、资源加载和对Context的透明创建的支持。上下文模块也支持Java EE的功能，如EJB,JMX和基本的远端处理。`Application`接口是上下文模块的焦点，`spring-context-support`提供了整合常用第三方库如缓存caching (EhCache, Guava, JCache), 邮件服务 (JavaMail), 管理器 (CommonJ, Quartz) 和模板引擎(FreeMarker, JasperReports, Velocity)到Spring应用上下文中。
`spring-expression`模块提供了对于在运行时查询和操作对象表强大的表达式语言，它是定义在JSP2.1的unified表达式语言的一个扩展。这种语言支持设置和获取变量值，变量赋值，方法调用，访问数组上下文，容器和索引器，逻辑和算法运算符，命名变量，根据Spring IoC容器通过名称获取对象。他也支持list投影，选择和一般的list聚合。
2.2.2 AOP和Instrumentation
`spring-aop`模块提供了AOP面向切面编程，允许你定义列入方法拦截器和切入点去干净的将实现为不同功能的代码解耦。使用源层的功能性的元数据，你也可以使用类似于.NET的attributes属性，将行为信息包含到代码中。
`spring-aspects`模块提供了AspectJ的集成支持。
`spring-intrument`模块提供了class instrumentation支持和适用于特点的应用服务器的类加载器实现。`spring-instrument-tomcat`模块包含了Spring下Tomcat的instrumentation 代理。
2.2.3 Messaging
Spring Framework4包含了`spring-messaging`模块，通过Spring的`Message, MessageChannel, MessageHandler`项目的关键抽象，其他服务器与消息基础的引用。这个模块也包含一些列方法的消息注解，类似于Spring MVC的注解。
2.2.4 Data Access/Integration
Data Access/Integration层包括JDBC,ORM,OXM,JMS和Transaction模块。
`spring-jdbc`模块提供了一个JDBC抽象层，可以帮助省去冗长的JDBC编码和解析数据库厂商特定的错误代码。
`spring-tx`模块对于实现特定接口的类和所有的POJOs提供了编程式和声明式事务管理支持。
`spring-orm`模块提供了常见的对象-关系映射API，包括JPA,JDO和Hibernate。使用`spring-orm`模块可以混合其他spring提供的特性，如之前的简单声明式事务管理，进行所有其他框架的O/R映射。
`spring-jms`模块包括生产和消费消息的功能。Spring Framework 4.1之后和`spring-messaging`整合。
2.2.5 Web
Web层包括`spring-web,spring-webmvc,spring-websocket,spring-webmvc-portlet`模块。
`spring-web`模块提供了基本的面向Web的集成特性，如多文件上传，使用Servlet listener初始化IoC容器，以及一个面向Web的应用上下文。也包含了一个HTTP客户端和一个Spring远程支持的web相关部分。
`spring-webmvc`模块包含Springd的model-view-controller(MVC)和为Web应用程序实现的REST Web服务。Spring的MVC框架是的模型范围内的代码和web forms之间能够清晰的分离出来，并与Spring框架其他特性集成在一起。
`spring-webmvc-portlet`模块(Web-Portlet模块)提供了用于Portlet环境和`spring-webmvc`模块的MVC实现。
2.2.6 Test
`spring-test`模块支持JUnit或TestNG关于Spring组件的单元测试和集成测试。它提供Spring应用上下文的持久化引用并缓存这些上下文。也提供模拟对象可以独立的测试你的代码。

### Spring Framework4新功能

### 核心技术

### 测试

### 数据访问

### 网络

### 一体化