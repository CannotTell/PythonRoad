#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午12:12
# @Author  : JZK
# @File    : 迭代对象和迭代器.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from collections import Iterable, Iterator


class MyClass():
    def __init__(self):
        self.list = [1, 2, 'test', 1.3]

    def __iter__(self):
        return iter(self.list)

    def __next__(self):
        return self.list[0]


if __name__ == '__main__':
    m = MyClass()

    # print(isinstance([], Iterable))
    # print(isinstance(iter([]), Iterator))
    # print(isinstance((), Iterable))
    # print(isinstance(iter(()), Iterator))
    # print(isinstance({}, Iterable))
    # print(isinstance(iter({}), Iterator))
    # print(isinstance('test', Iterable))
    # print(isinstance(iter('test'), Iterator))
    #
    #
    #
    #
    #
    # print(isinstance(1, Iterable))
    # print(isinstance(m, Iterable))
    #
    # print(isinstance(iter([]), Iterator))
    # print(isinstance((), Iterator))
    # print(isinstance({}, Iterator))
    # print(isinstance('test', Iterator))
    # print(isinstance(1, Iterator))
    # print(isinstance(m, Iterator))
    def add(s, x):
        return s + x


    def gen():
        for i in range(4):
            yield i


    base = gen()
    for n in [1, 10]:
        base = (add(i, n) for i in base)
    print(list(base))


