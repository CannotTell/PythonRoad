#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 5:45 PM
# @Author  : JZK
# @File    : range_xrange.py

#2.7 range 和 xrange

x = range(0, 10)    #range一开始就在内存里生成了，耗资源
print(x)
y = xrange(0, 10)   #xrange 只有在遍历的时候才会生成
print(y)
for item in y:
    print(item)

#python3里的range和2.7的xrange一样


for item in xrange(1, 10, 2):   #间隔2从小到大输出
    print(item)

for item in xrange(10, 1, -1): #间隔1从大到小输出
    print(item)