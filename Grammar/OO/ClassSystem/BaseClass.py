#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 9:04 AM
# @Author  : JZK
# @File    : BaseClass.py

class People:
    def __init__(self, name, gender, age):
        self.NAME = name
        self.GENDER = gender
        self.AGE = age

class Teacher(People):

    def __init__(self,name, gender, age):
        super(Teacher,self).__init__(name, gender, age)
        self.__COURSE_FEE = 0
    def setCourseFee(self,courseFee):
        self.__COURSE_FEE += courseFee

    def getCourseFee(self):
        return self.__COURSE_FEE

class Student(People):
    def __init__(self, name, gender, age):
        super(Student, self).__init__(name, gender, age)
        self.__COURSE_LISTS = []
        self.__COURSE_RECORD = {}
    def ChoiceCourse(self, course):
        self.__COURSE_LISTS.append(course)
        self.__COURSE_RECORD['course'] = 0
    def goToClass(self, courseName):
        if self.__COURSE_RECORD.has_key(courseName):
            self.__COURSE_RECORD[courseName] += 1
        else:
            print('You did not Choice the Course...')



class Course:
    totalClass = ['计算机科学', '软件工程', '数据结构', 'Java语言']
    #__CourseTime = ''
    def __init__(self, courseName, coursePrice, courseTeacher, courseTime):
        self.COURSE_NAME = courseName
        self.COURSE_PRICE = coursePrice
        self.COURSE_TEACHER = courseTeacher
        self.COURSE_TIME = courseTime


def sao():
    print('ok')