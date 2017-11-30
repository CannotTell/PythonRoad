#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 1:42 PM
# @Author  : JZK
# @File    : 单例模式_元类.py


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = {}
        super().__init__(*args, **kwargs)
    '''
    元类的__call__方法可以在其类实例化之前执行，所以这里可以控制实例的生成，
    type（）是可以直接用来创建对象的，在调用type（）的时候其实是调用其元类的
    __call__方法，所以这里super（）.__call__()就可以生成实例的
    '''
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
            return cls.__instance[cls]
        else:
            return cls.__instance[cls]


class A(metaclass=Singleton):
    def __init__(self, i):
        self.i = i


if __name__ == '__main__':
    a = A(1)
    b = A(2)
    print(a.i)
    print(b.i)
    print(type(a))
    print(a is b)