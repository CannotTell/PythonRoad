#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 3:45 PM
# @Author  : JZK
# @File    : Socket_Client_file.py

import os
import socket

filePath = 'testfile.avi'
cls = socket.socket()
cls.connect(('127.0.0.1', 9999))

ret = cls.recv(1024)
print(str(ret, encoding='utf-8'))

fileSize = os.stat(filePath).st_size
cls.sendall(bytes(str(fileSize), encoding='utf-8'))
#接收下信息 排除粘包的问题
cls.recv()

with open(filePath, 'rb') as f:
    for line in f:
        cls.sendall(line)
cls.close()