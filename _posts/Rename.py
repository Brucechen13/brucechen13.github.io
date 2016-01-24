 # -*- coding: UTF-8 -*-
from datetime import *
import os
import os.path
import re
date_time = date.today()
print date_time.strftime('%Y-%m-%d')
pattern = re.compile("\d{4}-\d{2}-\d{2}-.+", re.I)
for root, dirs, files in os.walk("./"):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for file in files:                        #输出文件信息
        print "parent is" + root
        print "filename is:" + file
        if re.match(pattern, file) or file.endswith("py"):
            print "normal file"
        else:
            oldsrc = root + file
            newsrc = root + date_time.strftime('%Y-%m-%d') + '-' + file
            os.rename(oldsrc, newsrc)
