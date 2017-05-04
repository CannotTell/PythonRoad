#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/2017 3:51 PM
# @Author  : JZK
# @File    : Copy.py

'''
深浅copy，首先先搞清楚Python的可变类型和不可变类型.
不可变类型：str, int, tuple
可变类型 list, dic等

对于不可变类型 str, int 我们在赋值时其实是新new了一个内存给当前变量，其原地址的值是无法修改的
OK，对于浅拷贝，只copy父对象，不会copy对象内部的对象，也就是说只是new了一个新变量指向内存并没有改变
慎copy就不用说了，都给你Copy了。
那么也就是说，对于不可变类型的int，str来说，赋值，浅拷贝和深拷贝都是一样的，没有区别。
'''
import copy

#字符串
s1 = 'xyz'
s2 = copy.copy(s1)
s3 = copy.deepcopy(s1)
print(id(s1))
print(id(s2))
print(id(s3))

#数字
i1 = 12345
i2 = copy.copy(i1)
i3 = copy.deepcopy(i1)
print(id(i1))
print(id(i2))
print(id(i3))

#字典
dic1 = {'k1':[1,2,3,4], 'k2':2,'k3':3}
dic2 = copy.copy(dic1)
print(id(dic1))
print(id(dic2))
dic1['k1'][0] = 0
print(dic1.get('k1'))
print(dic2.get('k1'))
dic2 = copy.deepcopy(dic1)
dic1['k1'][0] = 1111
print(dic1.get('k1'))
print(dic2.get('k1'))