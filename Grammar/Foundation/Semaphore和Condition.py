#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午6:18
# @Author  : JZK
# @File    : Semaphore和Condition.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
import threading
import time


def func(resource):
    # resource.acquire()
    with resource:
        print('{}获取锁,do something..'.format(threading.currentThread().getName()))
        time.sleep(3)
        # resource.release()
        print('{}释放锁'.format(threading.currentThread().getName()))


if __name__ == '__main__':
    # threading.BoundedSemaphore
    sema = threading.Semaphore(value=3)
    for i in range(4):
        t = threading.Thread(target=func, args=(sema,))
        t.start()
        # t.join()
    print('end')