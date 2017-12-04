#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/1/2017 11:40 AM
# @Author  : JZK
# @File    : 单例模式_基类.py


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    pass


if __name__ == '__main__':
    a1 = A()
    a2 = A()

    print(a1 is a2)