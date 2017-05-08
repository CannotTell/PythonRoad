#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/2017 11:28 AM
# @Author  : JZK
# @File    : loginTest.py

filePath = 'C:\\Users\\zhukai.jiang\\PycharmProjects\\PythonRoad\\Files\\db'
def login(userName, pwd):
    '''
    验证用户登入
    :param userName: 用户名 
    :param pwd: 密码
    :return: bool类型
    '''
    with open(filePath, encoding='utf-8') as f:
        for line in f:
            li = line.split('$')
            Name = li[0].strip()
            password = li[1].strip()
            if(Name == userName and password == pwd):
                return True

        return False

def UserExist(UserName):
    '''
    检查用户是否存在
    :param UserName:用户名 
    :return: Bool
    '''
    with open(filePath, encoding='utf-8') as f:
        for line in f:
            li = line.split('$')
            Name = li[0].strip()
            if (Name == UserName):
                return True
    return False

def Register(UserName, Pwd):
    '''
    新注册用户
    :param UserName: 用户名
    :param Pwd: 密码
    :return: Bool
    '''
    try:
        with open(filePath, 'a',encoding='utf-8') as f:
            s = '\n' + UserName + '$' + Pwd
            f.write(s)
        return True
    except:
        return False

inp = input('请输入1注册或2登入：')

if inp == '1':
    UserName = input('请输入新用户名：')
    while(UserExist(UserName)):
        UserName = input('用户名已存在，请重新输入：')

    pwd = input('请输入密码：')
    pwd2 = input('请再次确认输入密码：')
    if (pwd == pwd2 and Register(UserName, pwd)):
        print('注册成功')
    else:
        print('注册失败')

if inp == '2':
    username = input('请输入用户名：')
    pwd = input('请输入密码：')
    if login(username, pwd):
        print('Sucess')
    else:
        print('Faile')