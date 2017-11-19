#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 下午8:46
# @Author  : JZK
# @File    : new和init.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

"""
__init__和__new__的区别, __call__用法
"""


class A:
    def __init__(self):
        print('A Class init')

    def __new__(cls, *args, **kwargs):
        print('A class new func')
        return object.__new__(cls, *args, **kwargs)


class B:

    def __new__(cls, *args, **kwargs):
        print('B class new func')
        return object.__new__(A, *args, **kwargs)

    def __init__(self):
        print('B class init')


if __name__ == '__main__':
    print(type(B()))