#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 1:06 PM
# @Author  : JZK
# @File    : Socket_Client.py

import socket

cls = socket.socket()
cls.connect(('127.0.0.1',9999))

ret = cls.recv(1024) #recv也是阻塞线程
ret_str = str(ret, encoding='utf-8')
print(ret_str)

while True:
    inp = input('Please input something:')
    inp_bytes = bytes(inp, encoding='utf-8')
    cls.sendall(inp_bytes)
    if inp == 'q' or inp == 'Q':
        break
    else:
        ret2 = cls.recv(1024)
        print(str(ret2, encoding='utf-8'))

cls.close()
