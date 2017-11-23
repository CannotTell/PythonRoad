#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/23/2017 2:36 PM
# @Author  : JZK
# @File    : 协程金拱门.py


def jingongmeng():
    ret = -1
    count = 1
    while True:
        msg = yield ret
        if msg == -1:
            return
        print('生产汉堡{}'.format(count))
        ret = count
        count += 1


def _me(j):
    # 这个send（None）是用来启迪上面的生成器，如果直接send值过去会报错的
    j.send(None)
    for i in range(1, 6):
        print('需要一个汉堡！')
        hanbao = j.send(i)
        print('汉堡{}收到'.format(hanbao))
    j.close()


if __name__ == '__main__':
    j = jingongmeng()
    _me(j)
