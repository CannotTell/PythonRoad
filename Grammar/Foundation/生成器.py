#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午7:16
# @Author  : JZK
# @File    : 生成器.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
import time, sys


# 列表推导式
ll = [x * 2 for x in range(10)]
# 生成器表达式
g = (x * 2 for x in range(10))
# print(ll)


# 生成器函数
def test_yield():
    for j in range(10):
        yield j


# print(test_yield())


def exe_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print('cost time {}s'.format(time.time()-start_time))
        return ret
    return wrapper



def gen_fib(n):
    pre, cur = 0, 1
    while n > 0:
        n -= 1
        yield cur
        pre, cur = cur, cur + pre



def fib(n):
    pre, cur = 0, 1
    _list = []
    while n > 0:
        n -= 1
        _list.append(cur)
        pre, cur = cur, cur + pre
    return _list


if __name__ == '__main__':
    print(sys.getsizeof(fib(1000)))
    print(sys.getsizeof(gen_fib(1000)))