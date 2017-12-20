#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/20/2017 11:41 AM
# @Author  : JZK
# @File    : classmethod和staticmethod.py


class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def x():
        print('x')

    @classmethod
    def y(cls, y):
        a = cls(y, y)
        return a

    def z(self):
        print('z')


if __name__ == '__main__':
    # print(A(1, 2).a)
    A.x()
    print(A.y(1).a)