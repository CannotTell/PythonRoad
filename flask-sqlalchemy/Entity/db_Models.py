#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/18/2017 6:18 PM
# @Author  : JZK
# @File    : db_Models.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class UserAccounts(db.Model):
    Id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    UserName = db.Column(db.String(64), unique=True)
    Password = db.Column(db.String(64))
    CreateDate = db.Column(db.DateTime, default = datetime.utcnow())
    Remark = db.Column(db.TEXT)

    def __init__(self, UserName, Password, Remark):
        self.UserName = UserName
        self.Password = Password
        self.Remark = Remark

    def __repr__(self):
        return '<UserAccounts %r>' % self.UserName


class DataLog(db.Model):
    ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    InputValues = db.Column(db.String(20), nullable = False)
    CalResult = db.Column(db.TEXT)
    Time = db.Column(db.INTEGER, nullable=False)
    CreatedTime = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, InputValues, CalResult, Time):
        self.InputValues = InputValues
        self.CalResult = CalResult
        self.Time = Time

    def __repr__(self):
        return '<DataLog %r>' % self.InputValues

class LoginLog(db.Model):
    ID = db.Column(db.Integer, primary_key= True, autoincrement= True)
    UserName = db.Column(db.String(64), nullable= False)
    IP = db.Column(db.String(64), nullable= False)
    Address = db.Column(db.String(64))
    LoginDate = db.Column(db.DateTime, default= datetime.utcnow())

    def __init__(self, UserName, IP, Address):
        self.UserName = UserName
        self.IP = IP
        self.Address = Address

    def __repr__(self):
        return '<LoginLog %r>' % self.UserName



if __name__ == '__main__':
    # db.create_all()
    # ua = UserAccounts('test','123','test')
    # dl = DataLog('input','result', '3')
    # db.session.add(ua)
    # db.session.add(dl)
    # db.session.commit()
    user = UserAccounts.query.filter_by(UserName='test').first()
    print(user)