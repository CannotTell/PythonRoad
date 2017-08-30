#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/2017 11:34 AM
# @Author  : JZK
# @File    : TestGevent.py

import gevent

def one():
    gevent.sleep(2)
    print('1')

def two():
    gevent.sleep(1)
    print('2')

def three():
    gevent.sleep(0)
    print('3')


gevent.joinall([
    gevent.spawn(one),
    gevent.spawn(two),
    gevent.spawn(three)
])