---
layout:     post
title:      "笔记"
subtitle:   ""
date:       2017-07-12
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---

### Tensorflow-gpu环境 cudnn版本升级
运行程序时提示错误信息：
'''
 Loaded runtime CuDNN library: 6021 (compatibility version 6000) but source was compiled with 5105 (compatibility version 5100).  If using a binary install, upgrade your CuDNN library to match.  If building from sources, make sure the library loaded at runtime matches a compatible version specified during compile configuration.
'''
意思是TensorFlow使用的cudnn版本与机器中的cudnn版本不一致。当前机器的cudnn版本为5.1，需要使用cudnn6。
于是去官网下载了cudnn6，然后解压缩复制到cuda安装目录下，执行程序，依然出现了上述的错误信息，查看cuda/bin目录，发现了两个cudnn的dll文件，cudnn64_5.dll与cudnn64_6.dll。删除cudnn5后，运行程序出现了新的错误信息。
'''
builtins.ImportError: Traceback (most recent call last):
File "c:\Users\chenc\Anaconda3\envs\tensorflow-gpu\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 18, in swig_import_helper
return importlib.import_module(mname)
File "c:\Users\chenc\Anaconda3\envs\tensorflow-gpu\lib\importlib\__init__.py", line 126, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
File "<frozen importlib._bootstrap>", line 986, in _gcd_import
File "<frozen importlib._bootstrap>", line 969, in _find_and_load
File "<frozen importlib._bootstrap>", line 958, in _find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 666, in _load_unlocked
File "<frozen importlib._bootstrap>", line 577, in module_from_spec
'''
大意是无法加载所需控件，将cudnn6改为cudnn5以后上述问题消失，再次出现最开始的错误。