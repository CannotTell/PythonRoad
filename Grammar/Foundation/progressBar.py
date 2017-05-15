#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/12/2017 12:38 PM
# @Author  : JZK
# @File    : progressBar.py

import sys, time

for i in range(31):
    print(end='\r')
    print('%s%% |%s' %(int((i / 30 * 100)), int(i / 30 * 100 ) * '|'), end='')
    sys.stdout.flush()
    time.sleep(.3)