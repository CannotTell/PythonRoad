#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 12:50 PM
# @Author  : JZK
# @File    : CreateXML.py

from xml.etree import ElementTree as ET
import os

fileName = 'Files' + os.path.sep + 'test.xml'
filePath = os.path.join(os.path.dirname(os.getcwd()), fileName)

#方法一
# 创建根节点
root = ET.Element("famliy")


# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})
# 创建小儿子
son2 = ET.Element('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
#grandson1 = son1.makeelement('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
#grandson2 = son1.makeelement('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son1)

tree = ET.ElementTree(root)
tree.write(filePath,encoding='utf-8', short_empty_elements=False)

#方法2
root = ET.Element("famliy")


# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})

# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text = '孙子'


et = ET.ElementTree(root)  #生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)


def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    调用此方法是，写XML文件是用普通写文件操作
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")