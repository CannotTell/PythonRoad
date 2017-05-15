#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/2017 9:43 AM
# @Author  : JZK
# @File    : Email.py





def sendEmail(account, subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    ret = True
    localEmail = '1483687801@qq.com'
    password = 'cgyzdswdmx'
    server = smtplib.SMTP('smtp.qq.com', 465)

    try:
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = formataddr(['Auto Email',localEmail])
        meg['To'] = formataddr(['Dest',account])
        msg['Subject'] = subject

        #server = smtplib.SMTP('smtp.qq.com',465)
        server.login(localEmail, password)
        server.sendmail(localEmail, account, msg.as_string())
        #server.quit()
    except:
        ret = False
    finally:
        server.quit()
        return ret



account = ['564310009@qq.com', 'eric.c.jzk@outlook.com']
subject = 'Test Python Email'
message = 'Hello Python'
if sendEmail(account,subject,message):
    print('Sucess')
else :
    print('Failed')