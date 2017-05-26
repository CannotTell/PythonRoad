#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/24/2017 10:14 AM
# @Author  : JZK
# @File    : MyEmail.py
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mimetypes import guess_type
from email.encoders import encode_base64
from getpass import getpass
from smtplib import SMTP


class Email(object):
    def __init__(self, from_, to, subject, message, message_type='plain',
                 attachments=None, cc=None, message_encoding='utf-8'):
        self.email = MIMEMultipart()
        self.email['From'] = from_
        self.email['To'] = to
        self.email['Subject'] = subject
        if cc is not None:
            self.email['Cc'] = cc
        text = MIMEText(message, message_type, message_encoding)
        self.email.attach(text)
        if attachments is not None:
            for filename in attachments:
                mimetype, encoding = guess_type(filename)
                mimetype = mimetype.split('/', 1)
                fp = open(filename, 'rb')
                attachment = MIMEBase(mimetype[0], mimetype[1])
                attachment.set_payload(fp.read())
                fp.close()
                encode_base64(attachment)
                attachment.add_header('Content-Disposition', 'attachment',
                                      filename=os.path.basename(filename))
                self.email.attach(attachment)

    def __str__(self):
        return self.email.as_string()


class EmailConnection(object):
    def __init__(self, server, username, password):
        if ':' in server:
            data = server.split(':')
            self.server = data[0]
            self.port = int(data[1])
        else:
            self.server = server
            #self.port = 25
        self.username = username
        self.password = password
        self.connect()

    def connect(self):
        self.connection = SMTP(self.server)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(self.username, self.password)

    def send(self, message, from_=None, to=None):
        if type(message) == str:
            if from_ is None or to is None:
                raise ValueError('You need to specify `from_` and `to`')
            else:
                from_ = get_email(from_)
                to = get_email(to)
        else:
            from_ = message.email['From']
            if 'Cc' not in message.email:
                message.email['Cc'] = ''
            to_emails = [message.email['To']] + message.email['Cc'].split(',')
            to = to
            message = str(message)
        return self.connection.sendmail(from_, to, message)

    def close(self):
        self.connection.close()

def sendFromMyEmail():
    mail_server = 'smtp.qq.com'
    qq_number = '1483687801'
    pwd = 'slswhkbciontjeaf'
    to = 'eric.c.jzk@outlook.com'
    subject = "Auto Email From 'SharedVPN'"
    message = 'This a E-Mail Send From Python'
    attachments = 'shadowsocks.zip'

    print('Connecting to server...')
    server = EmailConnection(mail_server, qq_number, pwd)
    print('Preparing the email...')
    email = Email(qq_number + '@qq.com', to, subject, message, attachments)
    print('Sending...')
    server.send(email)
    print('Disconnecting...')
    server.close()
    print('Done!')


if __name__ == '__main__':
    sendFromMyEmail()
