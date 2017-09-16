---
layout:     post
title:      "荷兰军旗问题"
subtitle:   ""
date:       2017-09-13
author:     "brucechen"
header-img: "img/post-bg-code.jpg"
published: true
tags:
    - Code
    - 算法
---

### 荷兰国旗

拿破仑席卷欧洲大陆之后，代表自由，平等，博爱的竖色三色旗也风靡一时。荷兰国旗就是一面三色旗（只不过是横向的），自上而下为红白蓝三色。

该问题本身是关于三色球排序和分类的，由荷兰科学家Dijkstra提出。由于问题中的三色小球有序排列后正好分为三类，Dijkstra就想象成他母国的国旗，于是问题也就被命名为荷兰旗问题（Dutch National Flag Problem）。
下面是问题的正规描述： 现有n个红白蓝三种不同颜色的小球，乱序排列在一起，请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。

Solution:
初看起来，好像很难下手，如果直接暴力从左到右依次交换不合适的小球，并不是最优解法。
由于需要交换后有序且两两交换，类似于快排算法的partition过程，可以应用到此场景。
可以设置一个begin指针指向前段的颜色，一个current指针指向中段颜色，一个end指针指向后段颜色。current从左到右，当current指针所指元素为0时，与begin指针所指的元素交换，而后current++，begin++；current指针所指元素为1时，不做任何交换（即球不动），而后current++；current指针所指元素为2时，与end指针所指的元素交换，而后，current指针不动，end--。
`
while( current<=end )        
{             
  if( array[current] ==0 )             
   {                 
      swap(array[current],array[begin]);                  
      current++;                  
      begin++;            
   }             
   else if( array[current] == 1 )            
   {                 
      current++;            
   }   

   else //When array[current] =2   
   {               
      swap(array[current],array[end]);                
      end--;            
   }      
}
`