#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/2017 10:29 PM
# @Author  : JZK
# @File    : ThreadPool.py
# 进程池
from multiprocessing import Pool
import time

def myFun(i):
    time.sleep(2)
    return i + 100

def end_call(arg):
    print('end call', arg)


if __name__ == '__main__':
    p = Pool(5)

    for i in range(10):
        p.apply_async(func=myFun, args=(i,), callback=end_call)

    print('end')
    p.close()
    p.join()