---
layout:     post
title:      "Spring笔记"
subtitle:   "学习Spring的配置与使用"
date:       2017-05-05
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### Spring概述
Spring是一个轻量级web开源框架，包含很多可选模块。这里主要介绍Spring-core以及SpringMVC。

#### 依赖注入
依赖注入，又叫做控制反转，主要就是将对象的创建与对象的使用分离，从而解除对象与对象的依赖之间的紧耦合。通过依赖注入，就不必在对象使用的场景中创建这个对象，而只需要由第三方创建这个对象，并将对象注入到场景中即可。这里面的大部分工作都可以由框架实现，从而大大减轻对象管理的工作。

#### 面向切面
依赖注入让相互协作的软件组件保持松散耦合，面向切面则可以让你把应用各处的功能分离出来形成可重用的组件。
诸如日志、事务管理和安全控制的系统服务经常需要融入到自身核心业务逻辑组件中，这些系统服务通常称为横切关注点，因为它们总是跨越系统的多个组件。
面向切面可以使这些服务模块化，并通过声明的方式应用到需要影响的组件中去，从而使这些组件具有更高的内聚性，减少对核心逻辑的污染。
面向切面的主要配置如下：
'''
<aop:config>
	<aop:aspect ref = "横切关注点bean">
		<aop:pointcut id="切面id"
		   expression="execution(* *.function(...))"/>定义切面
		<aop:before pointcut-ref="切面id" method=""/>
		<aop:after pointcut-ref="" method=""/>
	</aop:aspect>
</aop:config>
'''








