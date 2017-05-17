#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 3:33 PM
# @Author  : JZK
# @File    : Socket_Server_file.py
import socket
import progressbar

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen(5)
p = progressbar.ProgressBar()

while True:

    conn, address = sk.accept()

    conn.sendall(bytes('Server Ready', encoding='utf-8'))
    # 收到大小后直接接受文件有可能会粘包
    fileSize = int(str(conn.recv(1024), encoding='utf-8'))
    # 再发送一条确认信息后再接受文件
    conn.sendall(bytes('File Size Received', encoding='utf-8'))
    received = 0

    f = open('new_file', 'wb')

    p.start(fileSize)
    #for i in range(fileSize):
    while True:
        if fileSize == received:
            break

        data = conn.recv(1024)
        f.write(data)

        received += len(data)
        p.update(received)
    f.close()
    p.finish()
    print('File Send Over!')
    #break
