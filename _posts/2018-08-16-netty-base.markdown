---
layout:     post
title:      "Netty笔记笔记"
subtitle:   ""
date:       2018-08-16
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: true
tags:
    - Java
    - 读书笔记
---

### Netty介绍

Java NIO的出现为高并发的网络编程提供了可能，然而NIO的网络程序实现并不简单而且很容易出现各种bug，因此通常推荐采用开源的网络库来完成。Netty就是一个高性能、异步事件驱动的NIO框架，它提供了对TCP、UDP和文件传输的支持，作为一个异步NIO框架，Netty的所有IO操作都是异步非阻塞的，通过Future-Listener机制，用户可以方便的主动获取或者通过通知机制获得IO操作结果。作为当前最流行的NIO框架，Netty在互联网领域、大数据分布式计算领域、游戏行业、通信行业等获得了广泛的应用，一些业界著名的开源组件也基于Netty的NIO框架构建。

### Netty网络通信demo

服务端
```
    final ByteBuf buf = Unpooled.unreleasableBuffer(
                Unpooled.copiedBuffer("Hi!\r\n", Charset.forName("UTF-8")));
    EventLoopGroup group = new NioEventLoopGroup();
    ServerBootstrap b = new ServerBootstrap();        //1

    b.group(group)                                    //2
     .channel(OioServerSocketChannel.class)
     .localAddress(new InetSocketAddress(port))
     .childHandler(new ChannelInitializer<SocketChannel>() { //3
         @Override
         public void initChannel(SocketChannel ch) 
             throws Exception {
             ch.pipeline().addLast(new ChannelInboundHandlerAdapter() {            //4
                 @Override
                 public void channelActive(ChannelHandlerContext ctx) throws Exception {
                     ctx.writeAndFlush(buf.duplicate()).addListener(ChannelFutureListener.CLOSE);//5
                 }
             });
         }
     });
    ChannelFuture f = b.bind().sync();  //6
    f.channel().closeFuture().sync();
```

客户端
```
    EventLoopGroup group = new NioEventLoopGroup();
    Bootstrap b = new Bootstrap();
    b.group(group)
            .channel(NioSocketChannel.class)
            .remoteAddress(new InetSocketAddress(host, port)) // 服务器的地址
            .handler(new ChannelInitializer<SocketChannel>() { 
                @Override
                protected void initChannel(SocketChannel socketChannel) throws Exception {
                    socketChannel.pipeline().addLast(new EchoClientInboundHandler());
                }
            });
    ChannelFuture f = b.connect().sync(); // 连接到服务器
    f.channel().closeFuture().sync();
```