#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-30 14:28:08
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version

import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0,parentdir)

import unittest
from dao.dataCollector import *

class TestDataCollector(unittest.TestCase):

    def test_saveToFile(self):

        DataCollector.saveToFile("testfile.txt", "sjdlfjsldfj")


if __name__ == '__main__':
    unittest.main()