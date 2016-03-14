---
layout:     post
title:      "Java的一些特性与机制"
subtitle:   "RMI JMS"
date:       2016-03-13
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### RMI
Java RMI指的是远程方法调用（Remote Method Invocation）。可以让某个虚拟机上的对象调用另一个虚拟机中的对象方法。下面是一个简单的RMI应用。

```
//定义一个远程接口，必须继承Remote接口，需要远程调用的方法必须抛出RemoteException
public interface IHello extends Remote{
	public String helloWorld() throws RemoteException;
	public String sayHello(string name) throws RemoteException;
}
```

实现被调用方的远程接口
```
public class HelloImpl extends UnicastRemoteObjects implements IHello{
	public HelloImpl() throws RemoteException{}
	public String helloWorld() throws RemoteException{
		return "Hello World";
	}
	public String sayHello(String name) throws RemoteException{
		return "hello"+name;
	}
}
```

被调用方需要创建RMI注册表，启动RMI服务，并将远程对象注册到RMI注册表中，这样才可以被正确调用。
```
public class HelloServer{
	public static main(String[] args){
		try{
			IHello rhello = new HelloImpl();
			LocateRegistry.createRegistry(8888);//创建注册表实例并指定端口
			Naming.rebind("rmi://localhost:8888/RHello",rhello);//远程对象注册到RMI注册服务器上
		}catch(RemoteException){
			System.out.println("创建远程对象发生异常！");
            e.printStackTrace(); 
		}catch (AlreadyBoundException e) {
            System.out.println("发生重复绑定对象异常！");
            e.printStackTrace();
        } catch (MalformedURLException e) {
            System.out.println("发生URL畸形异常！");
            e.printStackTrace();
        } 
	}
}
```

至此，RMI服务器构建完成，下面进行客户端测试。
```
public class HelloInvocation{
	public static void main(String[] args){
		try{
			IHello rHello = (IHello)Naming.lookup("rmi://localhost:8888/RHello");
			System.out.println(rhello.helloWorld());
            System.out.println(rhello.sayHelloToSomeBody("Chen")); 
		}catch (NotBoundException e) {
            e.printStackTrace();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (RemoteException e) {
            e.printStackTrace();  
        }
	}
}
```

### JMS
JMS，即Java Message Service，是Java平台中关于面向消息中间件的API，用于两个程序之间、或分布式系统中发送消息，进行异步通信。
JMS由以下元素组成：
* JMS提供者，JMS接口的具体实现
* JMS客户，生成或消费基于消息的Java应用程序或对象
* JMS生产者，创建并发送消息的JMS客户
* JMS消费者，接收消息的JMS客户
* JMS消息，JMS客户之间传递数据的对象
* JMS队列，一个容纳被发送等待阅读的消息区域
* JMS主题，一种支持发送消息给多个订阅者的机制


### RPC








