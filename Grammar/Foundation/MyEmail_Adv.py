#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/25/2017 10:50 AM
# @Author  : JZK
# @File    : MyEmail_Adv.py

from email.header import Header
from smtplib import SMTP_SSL
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type
from email.mime.text import MIMEText
import logging
import time
import os

logging.basicConfig(filename='sendEmail.log', level=logging.INFO)
class Email():
    def __init__(self, host_server, from_number, pwd, to, subject, message, attachments = None, message_type = 'plain', message_encoding = 'utf-8'):

        logging.info('Script Initing.... Time: %s', time.asctime(time.localtime(time.time())))

        self.email = MIMEMultipart()
        self.email['From'] = from_number + '@qq.com'
        self.email['To'] = to
        self.email['Subject'] = Header(subject, 'utf-8')
        self.host_server = host_server
        self.pwd = pwd
        self.email_number = from_number

        text = MIMEText(message, message_type, message_encoding)
        self.email.attach(text)

        with open(attachments, 'rb') as zf:
            msg = MIMEBase('application', 'zip')
            msg.set_payload(zf.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment',
                           filename='shadowsocks.zip')
            self.email.attach(msg)
            logging.info('attach %s file finished. Time: %s', attachments, time.asctime(time.localtime(time.time())))

        #self.email = self.email.as_string()


    def sendEmail(self):
        logging.info('Starting Send! Time: %s', time.asctime(time.localtime(time.time())))
        smtp = SMTP_SSL(self.host_server)
        smtp.ehlo(self.host_server)
        smtp.login(self.email_number, self.pwd)
        smtp.sendmail(self.email['From'], self.email['To'], bytes(self.email.as_string(), encoding='utf-8'))
        smtp.quit()
        logging.info('Send Finished! Time: %s', time.asctime(time.localtime(time.time())))

def runEmail():
    email_number = '1483687801'
    to = 'eric.c.jzk@outlook.com'
    subject = "Sharedvpn's shadowsocks log file"
    mail_content = 'This ia an auto E-mail!'
    host_server = 'smtp.qq.com'
    pwd = 'slswhkbciontjeaf'
    attachment = 'shadowsocks.zip'

    try:
        Email(host_server, email_number, pwd, to, subject, mail_content, attachment).sendEmail()
        print('Send Email Sucess')
    except Exception as e:
        print(e)
        logging.critical('Error: %s', e)

if __name__ == '__main__':
    #runEmail()
    try:
        cmd = 'zip ~/sendLog/shadowsocks.zip /var/log/shadowsocks.log'
        os.system(cmd)
        logging.info('Zip File Finished! Time: %s', time.asctime(time.localtime(time.time())))
    except Exception as e:
        exit(1)
        logging.critical('Error: %s', e)
    else:
        runEmail()


