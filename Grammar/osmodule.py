#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/13/2017 2:32 PM
# @Author  : JZK
# @File    : osmodule.py

import os
path = os.getcwd()
print(path)
print(os.stat(os.getcwd()))
print(os.path.dirname(path))