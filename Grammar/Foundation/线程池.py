#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午9:37
# @Author  : JZK
# @File    : 线程池.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


if __name__ == '__main__':
    pool = ThreadPoolExecutor(4)

    a = pool.submit(fetch_url, 'http://www.zhihu.com')
    b = pool.submit(fetch_url, 'http://www.baidu.com')
    print('任务提交完成')

    # 查看任务是否完成
    print(a.done())
    print(b.done())
    # 打印结果
    print(a.result())
    print(b.result())