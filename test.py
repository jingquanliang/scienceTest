#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-25 16:10:01
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import os

class JustCounter:
    # __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        # self.__secretCount += 1
        self.publicCount += 1
        self.mycount=1
        # print self.__secretCount

counter = JustCounter()
JustCounter.aa=1

counter.count()
print "mycounter is :"+str(counter.mycount)
print JustCounter.aa
# print counter.publicCount
# print JustCounter.publicCount
# print counter.__secretCount  # 报错，实例不能访问私有变量
