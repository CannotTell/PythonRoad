#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 5:37 PM
# @Author  : JZK
# @File    : TryCatch.py

try:
    # 主代码块
    pass
except KeyError as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass