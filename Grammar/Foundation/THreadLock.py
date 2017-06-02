#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/26/2017 10:12 AM
# @Author  : JZK
# @File    : THreadLock.py

import time
import threading

#NUM = 0

lock = threading.RLock()

def func(x):
    lock.acquire()  #获得锁
    global NUM
    for i in range(5):
        NUM = int(str(i) + str(x))
        print(NUM)
    NUM += 1
    time.sleep(1)

    lock.release()

for i in range(5):
    t = threading.Thread(target=func(i))
    t.start()