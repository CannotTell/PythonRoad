#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/18/2017 10:44 AM
# @Author  : JZK
# @File    : MultiplexingClient.py
import socket
import random

for i in range(10):
    port = random.randrange(7000,7003)
    #print(port)
    cls = socket.socket()
    cls.connect(('127.0.0.1', port))
    ret = str(cls.recv(1024),encoding='utf-8')
    print(ret)
    cls.close()