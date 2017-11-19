#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午6:30
# @Author  : JZK
# @File    : 深浅copy区别.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from copy import copy, deepcopy
"""
python 深浅copy区别代码
"""

# b和c分别深浅copy了a
a = [1, 2, 3, ['a', 'b', 'c']]
b = copy(a)
c = deepcopy(a)
d = a

# 看下各自id
print(id(a))
print(id(b))
print(id(c))
print(id(d))

# 对a操作
a.append(4)
a[3].append('d')

print(a)
print(b)
print(c)
print(d)

"""
由此可见 浅copy就是对对象的最外层copy了，
对内层对象还是引用原来的地址，
所以a的内层对象变化会影响倒b。
但是对于c深copy来讲完全没有影响
"""
