#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 2:56 PM
# @Author  : JZK
# @File    : LoggingModule.py

import logging
import os
#logging线程安全

fileName = 'Files' + os.path.sep + 'test.log'
filePath = os.path.join(os.path.dirname(os.getcwd()), fileName)

logging.basicConfig(filename=filePath,
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)
#当level大于等于10的时候才会被记录

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10, 'log')

'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''