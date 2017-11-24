#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/24/2017 12:47 PM
# @Author  : JZK
# @File    : Gevent.py

import gevent


def func1():
    print('run func1')
    gevent.sleep(0)
    print('finish func1')


def func2():
    print('run func2')
    gevent.sleep(0)
    print('finish func2')


if __name__ == '__main__':
    gevent.joinall([gevent.spawn(func1),
                    gevent.spawn(func2)])