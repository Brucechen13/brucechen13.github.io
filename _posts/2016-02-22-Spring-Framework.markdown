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
2.3 使用场景
上述的构造图展示Spring可以适用于很多场景，通过使用Spring实用的事务管理和web整合框架，既可以应用于资源有限的嵌入式应用，也可以引用在成熟的企业应用。

![java-javascript](/img/in-post/spring/overview-full.png.png)
<small class="img-hint">Typical full-fledged Spring web application</small>

Spring的声明式事务管理功能使得web程序可以像使用EJB容器管理事务的一样完全事务性。所有的事务逻辑可以被简单的POJO实现并被Spring的IoC容器管理。对于邮件发送和数据验证支持的额外服务由web层提供，可以让你选择怎样执行验证规则。Spring的ORM支持可以和JPA，Hibernate和JDO整合。例如，当使用Hibernate，你可以继续使用你的映射文件和标准的Hibernate`SessionFactory`配置。控制器无缝衔接web层和模型层，移除了`ActionForms`和其他用于传输HTTP参数到模型层的需要。
2.3.1 依赖管理和命名约定
依赖管理不同于依赖注入，为了在你的项目中使用诸如依赖注入这样的Spring功能，你需要装配所有需要的库并在运行时或者编译时把这些库放入classpath中。这些依赖并不是被注入的虚拟组件，而是文件系统中的物理资源。依赖管理的过程包括定位这些资源，载入并添加到classpath中。依赖可以是直接的（比如我的项目在运行时直接依赖Spring），也可以是间接的（比如我的项目依赖`commons-dbcp`，它依赖于`commons-pool`）。间接依赖也被称为传递，这也是所有依赖中最难鉴别和管理的。
如果你将使用Spring，你需要赋值你所需要的Spring组件到jar库中。为了让这个步骤更加容易，Spring被打包成一系列将依赖尽可能分割的模块，比如如果你不想实现web应用，你就不需要`spring-web`模块。为了表示Spring库的模块，我们使用一个速记的命名约定`spring-*`或`spring-*.jar`，`*`代表模块的名字（如`spring-core、spring-mvc、spring-jms`）。你使用的实际jar文件名字通常是模块名加上版本号（如`spring-core-4.3.0.BUILD-SNAPSHOT.jar`）。
每个Spring框架的正式版都会发布组件到以下位置：
* Maven Central，Maven请求的默认库，并不需要其他特殊的配置。很多Spring依赖的常用库也可以从Maven Central找到。而且很大一部分Spring社区用户使用Maven来管理依赖，这对他们来说很便捷。这里的jar是以`spring-*-<Version>.jar`的形式命名的，对应的Maven组id则是`org.springframework`。
* 专门用于托管Spring的公用Maven库。除了最终的GA正式版，这个库也托管开发快照版
和里程碑版。jar文件的命名规则和Maven Central是一致的，所以这是一个获取Spring开发版本和其他在Maven Central的库配合使用的地方。为了更容易被下载，这个库
还包含打包了所有Spring的jar文件的分发zip文件。
因此，你需要决定的第一件事就是如何管理你的依赖，我们一般推荐使用自动管理系统，如Maven，Gradle或lvy，但是你也可以下载这些jars文件人工管理。

##### Spring依赖和Spring的依赖
尽管Spring为众多的企业级和其他额外工具提供了集成和支持。她还是有意识的保持她的
强制依赖尽可能少。仅用Spring来构建简单的使用案例，您不应当去定位大量的jar库并下载（即使是自动的）。基本的依赖注入只需要一个额外的强制依赖用于日志管理（后面会更加详细的介绍日志选项）。接着我们会描绘配置一个依赖Spring的应用所应遵循的基本步骤，依次会涉及到Maven，Gradle和Ivy。所有案例里，如果有任何不清楚的，参考您的依赖管理系统相对应的文档，或者看一些示例代码。Spring编译时，是用Gradle来管理依赖的，我们的示例大部分使用Gadle或者Maven。

##### Maven依赖管理
如果您使用Maven来管理依赖，您甚至不需要显式提供日志依赖。比方说，创建一个应用上下并使用依赖注入去配置一个应用，你的Maven依赖应该如下：

```
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>4.3.0.BUILD-SNAPSHOT</version>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```


### Spring Framework4新功能
#### Spring 4.0增强和新功能
Spring框架第一个版本发布于2004年，自发布以来已历经三个主要版本更新:Spring 2.0提供了XML命名空间和AspectJ支持；Spring 2.5增加了注释驱动（annotation-driven）的配置支持；Spring 3.0增加了对Java 5+版本的支持和@Configuration模型。
Spring 4.0是最新的主要版本，并且首次完全支持Java 8的特性。你仍然可以使用老版本的Java，但是最低版本的要求已经提高到Java SE 6。我们也借主要版本更新的机会删除了许多过时的类和方法。
你可以在 [Spring Wiki文档](https://github.com/spring-projects/spring-framework/wiki) 上查看 [升级Spring 4.0迁移指南](https://github.com/spring-projects/spring-framework/wiki/Migrating-from-earlier-versions-of-the-spring-framework)。
3.1 改进的入门体验
新的 spring.io 网站提供了一整个系列的 "入门指南" 帮助你学习Spring。你可以本文档的 Spring 入门概述 一节阅读更多的入门指南。新网站还提供了Spring之下其他额外项目的一个全面的概述。
如果你是一个Maven用户，你可能会对 BOM 这个有用的POM文件感兴趣， 这个文件已经与每个Spring的发布版发布。
3.2 移除过时的包和方法
所有过时的包和许多过时的类和方法已经从Spring4中移除。如果你从之前的发布版升级Spring，你需要保证已经修复了所有使用过时的API方法。

查看完整的变化： [API差异报告](http://docs.spring.io/spring-framework/docs/3.2.4.RELEASE_to_4.0.0.RELEASE/)。

请注意，所有可选的第三方依赖都已经升级到了最低2010/2011(例如Spring4通常只支持2010年的最新或者现在的最新发布版本):尤其是 Hibernate 3.6+、EhCache 2.1+、Quartz 1.8+、Groovy 1.8+、Joda-Time 2.0+。但是有一个例外，Spring4依赖最近的Hibernate Validator 4.3+，现在对Jackson的支持集中在2.0+版本 (Spring3.2支持的Jackson 1.8/1.9，现在已经过时）。
3.3 Java 8 (以及6和7)
Spring4支持Java8的一些特性。你可以在Spring的回调接口中使用 lambda 表达式 和 方法引用。支持java.time (JSR-310)的值类型和一些改进过的注解，例如@Repeatable。你还可以使用Java8的参数名称发现机制（基于-parameters编译器标志）。

Spring仍然兼容老版本的Java和JDK：Java SE 6（具体来说，支持JDK6 update 18）以上版本，我们建议新的基于Spring4的项目使用Java7或Java8。
3.4 Java EE 6和7
Java EE 6 或以上版本是Spring4的底线,与JPA2.0和Servlet3.0规范有着特殊的意义。为了保持与Google App Engine和旧的应用程序服务器兼容,Spring4可以部署在Servlet2.5运行环境。但是我们强烈的建议您在Spring测试和模拟测试的开发环境中使用Servlet3.0+。
`如果你是WebSphere 7的用户，一定要安装JPA2.0功能包。在WebLogic 10.3.4或更高版本，安装附带的JPA2.0补丁。这样就可以将这两种服务器变成Spring4兼容的部署环境。`

从长远的观点来看，Spring4.0现在支持Java EE 7级别的适用性规范：尤其是JMS 2.0, JTA 1.2, JPA 2.1, Bean Validation 1.1 和JSR-236并发工具类。像往常一样，支持的重点是独立的使用这些规范。例如在Tomcat或者独立环境中。但是，当把Spring应用部署到Java EE 7服务器时它同样适用。

注意，Hibernate 4.3是JPA 2.1的提供者，因此它只支持Spring4。同样适用用于作为Bean Validation 1.1提供者的Hibernate Validator 5.0。这两个都不支持Spring3.2。
3.5 Groovy DSL定义Bean

Spring4.0支持使用Groovy DSL来进行外部的bean定义配置。这在概念上类似于使用XML的bean定义，但是支持更简洁的语法。使用Groovy还允许您轻松地将bean定义直接嵌入到引导代码中。例如：
```
def reader = new GroovyBeanDefinitionReader(myApplicationContext)
reader.beans {
    dataSource(BasicDataSource) {
        driverClassName = "org.hsqldb.jdbcDriver"
        url = "jdbc:hsqldb:mem:grailsDB"
        username = "sa"
        password = ""
        settings = [mynew:"setting"]
    }
    sessionFactory(SessionFactory) {
        dataSource = dataSource
    }
    myService(MyService) {
        nestedBean = { AnotherBean bean ->
            dataSource = dataSource
        }
    }
}
```
有关更多信息，请参阅 GroovyBeanDefinitionReader javadocs.
3.6 核心容器改进

有几种对核心容器的常规改进：

* Spring现在注入Bean的时候把 泛型类型 当成一种形式的 限定符。例如：如果你使用Spring Data Repository你可以方便的插入特定的实现：@Autowired Repository<Customer> customerRepository。
* 如果你使用Spring的元注解支持，你现在可以开发自定义注解来公开源注解的特定属性。
* 当自动装配到lists和arrays时，Beans现在可以被 排序 了。支持@Order注解和Ordered接口两种方式。
* @Lazy注解现在可以用在注入点以及@Bean定义上。
* 引入@Description注解,开发人员可以使用基于Java方式的配置。
* 根据条件筛选Beans的广义模型通过@Conditional注解加入。这和@Profile支持的类似，但是允许以编程式开发用户定义的策略。
* 基于CGLIB的代理类不在需要默认的构造方法。这个支持是由 objenesis库提供。这个库重新打包到Spring框架中，作为Spring框架的一部分发布。通过这个策略，针对代理实例被调用没有构造可言了。
* 框架现在支持管理时区。例如LocaleContext。 

3.7 常规Web改进

现在仍然可以部署到Servlet 2.5服务器，但是Spring4.0现在主要集中在Servlet 3.0+环境。如果你使用Spring MVC测试框架，你需要将Servlet 3.0兼容的JAR包放到 测试的classpath下。

除了稍后会提到的WebSocket支持外，下面的常规改进已经加入到Spring的Web模块：

    你可以在Spring MVC应用中使用新的@RestController注解，不在需要给@RequestMapping的方法添加@ResponseBody注解。
    AsyncRestTemplate类已被添加进来，当开发REST客户端时，允许非阻塞异步支持。
    当开发Spring MVC应用时，Spring现在提供了全面的时区支持 。 

3.8 WebSocket、SockJS和STOMP消息

一个新的spring-websocket模块提供了全面的基于WebSocket和在Web应用的客户端和服务器之间双向通信的支持。它和Java WebSocket API JSR-356兼容，此外还提供了当浏览器不支持WebSocket协议时的基于SockJS的备用选项。

一个新的spring-messaging模块添加了支持STOMP作为WebSocket子协议用于在应用中使用注解编程模型路由和处理从WebSocket客户端发送的STOMP消息。由于@Controller现在可以同时包含@RequestMapping和@MessageMapping方法用于处理HTTP请求和来自WebSocket连接客户端发送的消息。新的spring-messaging模块还包含了来自以前Spring集成项目的关键抽象，例如Message、MessageChannel、MessageHandler和其他作为基于消息传递的应用程序的基础。

欲知详情以及较全面的介绍，请参见Chapter 20, WebSocket 支持一节。
3.9 测试改进

除了精简spring-test模块中过时的代码外，Spring4还引入了几个用于单元测试和集成测试的新功能。

    几乎spring-test模块中所有的注解（例如：@ContextConfiguration、@WebAppConfiguration、@ContextHierarchy、@ActiveProfiles等等)现在可以用作元注解来创建自定义的composed annotations并且可以减少测试套件的配置。
    现在可以以编程方式解决Bean定义配置文件的激活。只需要实现一个自定义的ActiveProfilesResolver，并且通过@ActiveProfiles的resolver属性注册。
    新的SocketUtils类被引入到了spring-core模块。这个类可以使你能够扫描本地主机的空闲的TCP和UDP服务端口。这个功能不是专门用在测试的，但是可以证明在你使用Socket写集成测试的时候非常有用。例如测试内存中启动的SMTP服务器，FTP服务器，Servlet容器等。
    从Spring 4.0开始,org.springframework.mock.web包中的一套mock是基于Servlet 3.0 API。此外，一些Servlet API mocks（例如：MockHttpServletRequest、MockServletContext等等）已经有一些小的改进更新，提高了可配置性。 
4. Spring 4.1增强和新功能
Prev 	Part II. Spring 4.x的新功能	 Next
4. Spring 4.1增强和新功能
4.1 JMS改进

Spring 4.1引入了一个更简单的基础架构，使用 @JmsListener注解bean方法来注册JMS监听端点。XML命名空间已经通过增强来支持这种新的方式（jms:annotation-driven），它也可以完全通过Java配置( @EnableJms, JmsListenerContainerFactory)来配置架构。也可以使用 JmsListenerConfigurer注解来注册监听端点。

Spring 4.1还调整了JMS的支持，使得你可以从spring-messaging在Spring4.0引入的抽象获益，即：

    消息监听端点可以有更为灵活的签名，并且可以从标准的消息注解获益，例如@Payload、@Header、@Headers和@SendTo注解。另外，也可以使用一个标准的消息，以代替javax.jms.Message作为方法参数。
    一个新的可用 JmsMessageOperations接口和允许操作使用Message抽象的JmsTemplate。 

最后，Spring 4.1提供了其他各种各样的改进：

    JmsTemplate中的同步请求-答复操作支持
    监听器的优先权可以指定每个<jms:listener/>元素
    消息侦听器容器恢复选项可以通过使用 BackOff 实现进行配置
    JMS 2.0消费者支持共享 

4.2 Caching（缓存）改进

Spring 4.1 支持JCache (JSR-107)注解使用Spring的现有缓存配置和基础结构的抽象；使用标准注解不需要任何更改。

Spring 4.1也大大提高了自己的缓存抽象：

    缓存可以在运行时使用CacheResolver解决。因此使用value参数定义的缓存名称不在是强制性的。
    更多的操作级自定义项：缓存解析器，缓存管理器，键值生成器
    一个新的@CacheConfig类级别注解允许在类级别上共享常用配置，不需要启用任何缓存操作。
    使用CacheErrorHandler更好的处理缓存方法的异常 

Spring 4.1为了在CacheInterface添加一个新的putIfAbsent方法也做了重大的更改。
4.3 Web改进

    The existing support for resource handling based on the ResourceHttpRequestHandler has been expanded with new abstractions ResourceResolver, ResourceTransformer, and ResourceUrlProvider. A number of built-in implementations provide support for versioned resource URLs (for effective HTTP caching), locating gzipped resources, generating an HTML 5 AppCache manifests, and more. See Section 16.16.7, “Serving of Resources”.
    JDK 1.8’s java.util.Optional is now supported for @RequestParam, @RequestHeader, and @MatrixVariable controller method arguments.
    ListenableFuture is supported as a return value alternative to DeferredResult where an underlying service (or perhaps a call to AsyncRestTemplate) already returns ListenableFuture.
    @ModelAttribute methods are now invoked in an order that respects inter-dependencies. See SPR-6299.
    Jackson’s @JsonView is supported directly on @ResponseBody and ResponseEntity controller methods for serializing different amounts of detail for the same POJO (e.g. summary vs. detail page). This is also supported with View-based rendering by adding the serialization view type as a model attribute under a special key. See the section called “支持 Jackson 序列化视图” for details.
    JSONP is now supported with Jackson. See the section called “支持 Jackson JSONP”.
    A new lifecycle option is available for intercepting @ResponseBody and ResponseEntity methods just after the controller method returns and before the response is written. To take advantage declare an @ControllerAdvice bean that implements ResponseBodyAdvice. The built-in support for @JsonView and JSONP take advantage of this. See Section 16.4.1, “使用 HandlerInterceptor 拦截请求”.

    There are three new HttpMessageConverter options:
        Gson — lighter footprint than Jackson; has already been in use in Spring Android.
        Google Protocol Buffers — efficient and effective as an inter-service communication data protocol within an enterprise but can also be exposed as JSON and XML for browsers.
        Jackson based XML serialization is now supported through the jackson-dataformat-xml extension. When using @EnableWebMvc or <mvc:annotation-driven/>, this is used by default instead of JAXB2 if jackson-dataformat-xml is in the classpath. 
    Views such as JSPs can now build links to controllers by referring to controller mappings by name. A default name is assigned to every @RequestMapping. For example FooController with method handleFoo is named "FC#handleFoo". The naming strategy is pluggable. It is also possible to name an @RequestMapping explicitly through its name attribute. A new mvcUrl function in the Spring JSP tag library makes this easy to use in JSP pages. See Section 16.7.2, “Building URIs to Controllers and methods from views”.
    ResponseEntity provides a builder-style API to guide controller methods towards the preparation of server-side responses, e.g. ResponseEntity.ok().
    RequestEntity is a new type that provides a builder-style API to guide client-side REST code towards the preparation of HTTP requests.

    MVC Java config and XML namespace:
        View resolvers can now be configured including support for content negotiation, see Section 16.16.6, “View Resolvers”.
        View controllers now have built-in support for redirects and for setting the response status. An application can use this to configure redirect URLs, render 404 responses with a view, send "no content" responses, etc. Some use cases are listed here.
        Path matching customizations are frequently used and now built-in. See Section 16.16.9, “Path Matching”. 
    Groovy markup template support (based on Groovy 2.3). See the GroovyMarkupConfigurer and respecitve ViewResolver and ‘View’ implementations. 

4.4 WebSocket STOMP消息改进

    SockJS (Java) client-side support. See SockJsClient and classes in same package.
    New application context events SessionSubscribeEvent and SessionUnubscribeEvent published when STOMP clients subscribe and unsubscribe.
    New "websocket" scope. See Section 20.4.13, “WebSocket Scope”.
    @SendToUser can target only a single session and does not require an authenticated user.
    @MessageMapping methods can use dot "." instead of slash "/" as path separator. See SPR-11660.
    STOMP/WebSocket monitoring info collected and logged. See Section 20.4.15, “Runtime Monitoring”.
    Significantly optimized and improved logging that should remain very readable and compact even at DEBUG level.
    Optimized message creation including support for temporary message mutability and avoiding automatic message id and timestamp creation. See Javadoc of MessageHeaderAccessor.
    STOMP/WebSocket connections that have not activity 60 seconds after the WebSocket session is established. See SPR-11884. 

4.5 测试改进

    Groovy scripts can now be used to configure the ApplicationContext loaded for integration tests in the TestContext framework.
        See the section called “Context configuration with Groovy scripts” for details. 

    Test-managed transactions can now be programmatically started and ended within transactional test methods via the new TestTransaction API.
        See the section called “Programmatic transaction management” for details. 

    SQL script execution can now be configured declaratively via the new @Sql and @SqlConfig annotations on a per-class or per-method basis.
        See the section called “Executing SQL scripts” for details. 

    Test property sources which automatically override system and application property sources can be configured via the new @TestPropertySource annotation.
        See the section called “Context configuration with test property sources” for details. 

    Default TestExecutionListeners can now be automatically discovered.
        See the section called “Automatic discovery of default TestExecutionListeners” for details. 

    Custom TestExecutionListeners can now be automatically merged with the default listeners.
        See the section called “Merging TestExecutionListeners” for details. 

    The documentation for transactional testing support in the TestContext framework has been improved with more thorough explanations and additional examples.
        See the section called “Transaction management” for details. 
    Various improvements to MockServletContext, MockHttpServletRequest, and other Servlet API mocks.
    AssertThrows has been refactored to support Throwable instead of Exception.
    In Spring MVC Test, JSON responses can be asserted with JSON Assert as an extra option to using JSONPath much like it has been possible to do for XML with XMLUnit.
    MockMvcBuilder recipes can now be created with the help of MockMvcConfigurer. This was added to make it easy to apply Spring Security setup but can be used to encapsulate common setup for any 3rd party framework or within a project.
    MockRestServiceServer now supports the AsyncRestTemplate for client-side testing.

### 核心技术

### 测试

### 数据访问

### 网络

### 一体化