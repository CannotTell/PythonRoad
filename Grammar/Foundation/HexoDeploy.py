#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/19/2017 9:40 AM
# @Author  : JZK
# @File    : HexoDeploy.py
import os

cmd = 'hexo clean && hexo g -d'
info = os.system(cmd)
print(info)