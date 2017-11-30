#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/30/2017 2:43 PM
# @Author  : JZK
# @File    : 元类.py


# 自定义类A
class A:
    pass


if __name__ == '__main__':
    # 自定义类D
    D = type('D', (object, ), {})
    a = A()
    b = 1
    c = 'str'
    d = D()
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(callable(a))