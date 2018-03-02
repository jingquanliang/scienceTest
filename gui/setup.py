#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 15:33:33
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : 0.1
from distutils.core import setup
import py2exe
import sys

py2exe_options = {
    "includes": ["sip","PyQt5.QtGui","PyQt5.QtWidgets","PyQt5.QtCore","PyQt5.QtCore"],
    # "dll_excludes": ["MSVCP90.dll",],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    # "bundle_files": 1, # 64位不支持
    }

setup(
  name = '第一个PyQt5程序',
  version = '1.0',
  windows = [{"script":"mygui.py"}],
  # zipfile = None,
  options = {'py2exe': py2exe_options},
  # options={"py2exe":{"includes":["sip"]}},
  # console=["gui.py"]
  )

