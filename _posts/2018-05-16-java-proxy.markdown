---
layout:     post
title:      "Java动态代理相关笔记"
subtitle:   ""
date:       2018-05-16
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### 代理模式

代理模式, 即给某一个对象提供一个代理, 并由代理对象控制对原对象的引用。

代理模式主要涉及三个角色:
- Subject: 抽象角色, 声明真实对象和代理对象的共同接口。
- Proxy: 代理角色, 它是真实角色的封装, 其内部持有真实角色的引用, 并且提供了和真实角色一样的接口, 因此程序中可以通过代理角色来操作真实的角色, 并且还可以附带其他额外的操作。
- RealSubject: 真实角色, 代理角色所代表的真实对象, 是我们最终要引用的对象。

代理模式的优点是能够协调调用者和被调用者, 在一定程度上降低了系统的耦合度，提高了灵活性。缺点就是增加了复杂度，而且由于增加了代理对象，请求的处理速度可能会变慢。

代理模式的常用实现如下：
1. 远程代理(remote proxy): 用本地对象来代表一个远端的对象, 对本地对象方法的调用都会作用于远端对象。远程代理最常见的例子是 ATM 机, 这里 ATM 机充当的就是本地代理对象, 而远端对象就是银行中的存取钱系统, 我们通过 ATM 机来间接地和远端系统打交道
2. 虚拟代理(virtual proxy): 虚拟代理是大型对象或复杂操作的占位符. 它常用的场景是实现延时加载或复杂任务的后台执行. 例如当一个对象需要很长的时间来初始化时, 那么可以先创建一个虚拟代理对象, 当程序实际需要使用此对象时, 才真正地实例化它, 这样就缩短了程序的启动时间, 即所谓的延时加载
3. 保护代理(protect proxy): 控制对一个对象的访问, 可以给不同的用户提供不同级别的使用权限. 例如我们可以在代理中检查用户的权限, 当权限不足时, 禁止用户调用此对象的方法
4. 缓存代理(cache proxy): 对实际对象的调用结果进行缓存。例如一些复杂的操作, 如数据库读取等, 可以通过缓存代理将结果存储起来, 下次再调用时, 直接返回缓存的结果
5. 图片代理(image proxy): 当用户需要加载大型图片时, 可以通过代理对象的方法来进行处理, 即在代理对象的方法中, 先使用一个线程向客户端浏览器加载一个小图片, 然后在后台使用另一个线程来调用大图片的加载方法将大图片加载到客户端


### Java中的静态代理

静态代理就是通过代理对象引用目标对象，然后继承共同的接口，代理类的接口实现中调用目标对象的实现。

下面是一个加载图片的静态代理示例。

```
public interface LoadImage {
    Image loadImage(String name);
}
public class LoadImageProxy implements LoadImage {
    private LoadImage loadImageReal;

    public LoadImageProxy(LoadImage loadImageReal) {
        this.loadImageReal = loadImageReal;
    }

    @Override
    public Image loadImage(String name) {
        return loadImageReal.loadImage(name);
    }
}
public static void main(String[] args) {
    LoadFromDisk loadFromDisk = new LoadFromDisk();
    LoadImageProxy proxy = new LoadImageProxy(loadFromDisk);
    proxy.loadImage("/tmp/test.png");
}
```

### Java中的动态代理

静态代理虽然简单，但是灵活性不高，这时可以使用动态代理。

动态代理就是动态地创建代理并且动态地处理所代理对象的方法调用。

采用动态代理来实现上面这个例子：

```
public interface LoadImage {
    Image loadImage(String name);
}
public class DynamicProxyHandler implements InvocationHandler {
    private Object proxied;

    public DynamicProxyHandler(Object proxied) {
        this.proxied = proxied;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("Proxy class: " + proxy.getClass() + ", method: " + method + ", args: " + args);
        return method.invoke(proxied, args);
    }
}
public static void main(String[] args) {
    // 实际对象
    LoadFromDisk loadFromDisk = new LoadFromDisk();
    // 通过 Proxy.newProxyInstance 静态方法创建代理对象
    LoadImage loadImage = (LoadImage) Proxy.newProxyInstance(LoadImage.class.getClassLoader(), new Class[]{LoadImage.class}, new DynamicProxyHandler(loadFromDisk));
    // 通过代理对象操作实际对象.
    loadImage.loadImage("/tmp/test.png");
}
```