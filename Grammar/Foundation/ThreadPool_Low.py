#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/2017 10:19 PM
# @Author  : JZK
# @File    : ThreadPool_Low.py
# Low版自定义线程

import threading
import queue
import time

class ThreadPool(object):
    def __init__(self, max_num = 20):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)

def myfun(pool,i):
    time.sleep(1)
    print(i)
    pool.add_thread()

if __name__ == '__main__':



    p = ThreadPool(10)

    for i in range(10):
        td = p.get_thread()
        t = td(target = myfun, args=(p,i,))
        t.start()