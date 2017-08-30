#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/29/2017 11:27 AM
# @Author  : JZK
# @File    : Restart.py


import os

pathCommand = 'cd /www/DataWebsite2.1'

stopCommand = 'killall  -9 uwsgi'

startCommand = 'nohup uwsgi --ini config.ini &'

os.system(pathCommand)
os.system(stopCommand)
os.system(startCommand)

print('OK...')