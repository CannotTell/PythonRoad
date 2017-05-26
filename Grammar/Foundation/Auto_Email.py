#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/23/2017 4:58 PM
# @Author  : JZK
# @File    : Auto_Email.py

from email.header import Header
from smtplib import SMTP_SSL
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

qq_number = '1483687801'
receiver='eric.c.jzk@outlook.com'
mail_title = 'Python 的邮件'
mail_content = '你好，现在在进行一项用python登录qq邮箱发邮件的测试'

def Send_Email(account_to, subject, mail_content):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_mail = '1483687801@qq.com'
    pwd = 'slswhkbciontjeaf'

    smtp = SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(qq_number, pwd)

    themsg = MIMEMultipart()
    themsg['Subject'] = Header(subject, 'utf-8')
    themsg['To'] = account_to
    themsg['From'] = sender_mail
    text = MIMEText(mail_content, 'plain', 'utf-8')
    themsg.attach(text)
    #themsg.preamble = mail_content

    with open('shadowsocks.zip', 'rb') as zf:

        msg = MIMEBase('application', 'zip')
        msg.set_payload(zf.read())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment',
                       filename='shadowsocks.zip')
        themsg.attach(msg)
        themsg = themsg.as_string()
    # msg = MIMEText(mail_content, "plain", 'utf-8')
    # msg["Subject"] = Header(subject, 'utf-8')
    # msg["From"] = sender_mail
    # msg["To"] = account_to
    #
    # att2 = MIMEText(open('shadowsocks.zip', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="shadowsocks.zip"'
    # msg.attach(att2)

    smtp.sendmail(sender_mail, account_to, bytes(themsg, encoding='utf-8'))
    smtp.quit()



try:
    Send_Email(receiver, mail_title, mail_content)
    print("Sucess!")
except Exception as e:
    print(e)

    #zip ~/sendLog/shadowsocks.zip /var/log/shadowsocks.log
    #slswhkbciontjeaf
#wprdfrnxqocsjcdi