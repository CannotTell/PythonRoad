#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 10:18 AM
# @Author  : JZK
# @File    : xmlRead.py

import os
from xml.etree import ElementTree as ET

fileName = 'Files' + os.path.sep + 'model.xml'
filePath = os.path.join(os.path.dirname(os.getcwd()), fileName)
#print(filePath)

#打开文件解析xml，不可修改
with open(filePath, 'r', encoding='utf-8') as xml:
    root = ET.XML(xml.read())
    print(root.tag, root.attrib)
    for node in root:
        print(node.tag, node.attrib)
        for i in node.iter('TrainDetailInfo'):
            print(i.attrib,i.find('TrainStation').text,i.find('StartTime').text)

#打开并能修改
tree = ET.parse(filePath)
root = tree.getroot()
#修改节点文本
# for node in root.iter('TrainDetailInfo'):
#     node.find('TrainStation').text += '_test str'
# tree.write(filePath)

#删除好和添加节点属性
#
    #node.set('name','eric')
    #del node.attrib['name']
#tree.write(filePath)