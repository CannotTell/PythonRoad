#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 11:38 AM
# @Author  : JZK
# @File    : 单例模式_装饰器.py


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class A:
    def __init__(self, a):
        self.a = a

    def test(self):
        pass


class B:
    def __init__(self):
        pass

    def test(self):
        pass

    def test2(self):
        pass


if __name__ == '__main__':
    a1 = A(1)
    a2 = A(2)

    print(a1.a)
    print(a2.a)
    print(B.__dict__)
    print(A.__dict__)
    print(type(A))
    print(type(B))
    print(id(a1))
    print(id(a2))