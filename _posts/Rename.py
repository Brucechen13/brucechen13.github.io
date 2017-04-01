 # -*- coding: UTF-8 -*-
from datetime import *
import os
import os.path
import re
date_time = date.today()
strText = '''---
layout:     post
title:      "笔记"
subtitle:   ""
date:       %s
author:     "brucechen"
header-img: "img/post-bg-java.jpg"
published: false
tags:
    - Java
    - 读书笔记
---''' % date_time.strftime('%Y-%m-%d')
print(date_time.strftime('%Y-%m-%d'))
f = open('%s.markdown'%date_time.strftime('%Y-%m-%d'), mode='w')
f.write(strText)
f.close()
print(strText)
