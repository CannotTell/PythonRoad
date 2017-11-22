#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 上午11:00
# @Author  : JZK
# @File    : 进程池.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from multiprocessing import Pool
import os
import time


def test_pool(msg):
    print('PID:{} says {}'.format(os.getpid(), msg))
    time.sleep(2)
    print('test_pool done')


if __name__ == '__main__':
    pool = Pool(processes=4)
    for i in range(5):
        msg = 'hello'
        # pool.apply_async(test_pool, (msg,)) # 非阻塞
        pool.apply(test_pool, (msg, ))  # 阻塞

    print('start..')
    pool.close()
    pool.join()
    print('done..')