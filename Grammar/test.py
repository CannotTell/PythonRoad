#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/17/2017 7:04 PM
# @Author  : JZK
# @File    : test.py

from dateutil.relativedelta import *
import datetime


Now = datetime.datetime(2017, 8, 31, 8, 12, 34, 790945)
last = Now + relativedelta(months=+1)
print(Now.strftime("%Y-%m-%d"))
print(last.strftime("%Y-%m-%d"))