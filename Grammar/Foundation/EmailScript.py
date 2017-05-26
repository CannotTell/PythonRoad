#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/25/2017 5:38 PM
# @Author  : JZK
# @File    : EmailScript.py
import os
import MyEmail_Adv.py as MyEmail

try:
    cmd = 'zip ~/sendLog/shadowsocks.zip /var/log/shadowsocks.log'
    os.system(cmd)
except Exception as e:
    exit(1)
else:
    MyEmail.runEmail()