#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/2017 6:54 PM
# @Author  : JZK
# @File    : Decorator.py

"""
装饰器
"""


# 在my_func函数之前和之后加处理， 前提是record_log本身没有参数
def record_log(func):
    def wrapper(*arg, **args):
        print('do log before')
        func(*arg, **args)
        print('do log after')
    return wrapper


# 如果record_log本身也有参数的写法
def record_log2(type):
    def decorator(func):
        def wrapper(*arg, **args):
            print('do log before with {}'.format(type))
            func(*arg, **args)
            print('do log after {}'.format(type))
        return wrapper
    return decorator


@ record_log2('test')
def my_func2(x, y):
    print('my func {0}-{1}'.format(x, y))


@record_log
def my_func(x, y):
    print('my func {0}-{1}'.format(x, y))


if __name__ == '__main__':
    my_func(1, 2)
    my_func2(1, 2)