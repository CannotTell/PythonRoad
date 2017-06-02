#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/2/2017 1:23 PM
# @Author  : JZK
# @File    : FilesExtract.py
import os
#import shutil

#python3
# inp = input('：')
# inp2 = input('文件特殊符号：')

inp = raw_input('File Path:')
inp2 = raw_input('File contains:')

#filePath = r'C:\Users\zhukai.jiang\Desktop\TestFolder'

def cp(oldPaht, newPath):
    cmdline = 'copy "' + oldPaht + '" "' + newPath + '"'
    #shutil.copyfile(oldPaht, newPath)
    os.system(cmdline)
    print(cmdline)

def getFiles(filePath, specile):
    #dictFile = {}
    count = 0
    for parent, dirnames, filenames in os.walk(filePath):
        for filename in filenames:
            #dictFile[os.path.join(parent, filename)] = filename
            if filename.endswith('.PDF') or filename.endswith('.pdf'):
                if specile in filename:
                    cp(os.path.join(parent, filename), os.getcwd())
                    count += 1
    return count

try:
    count = getFiles(inp,inp2)
    print('copied %d file(s)'% count)
except Exception as e:
    print(e)

