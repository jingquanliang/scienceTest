#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 15:33:33
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : 0.1

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QSettings

from databaseUI import *
#从PyQt库导入QtWidget通用窗口类
class MainWindow(QMainWindow):
#自己建一个mywindows类，以class开头，mywindows是自己的类名，
#（QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，
    def __init__(self):
        super(MainWindow,self).__init__()
        self.settings=QSettings("wise.ini",QSettings.IniFormat)
        self.settings.setValue("editor/wrapMargin", 68)
        # print settings.fileName()

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('看什么看 ^_^')




        self.initUI() #布局，菜单栏之类的

    def initUI(self):

        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(), screen.height())
        # self.resize(900, 800)
        self.center()#居中
        self.setWindowTitle('myapp')
        self.setWindowIcon(QIcon('icons/myapp.ico'))

        #文本输入框
        text = QTextEdit()
        self.setCentralWidget(text)

        #按钮
        # btn = QPushButton('Push', self)
        # btn.setToolTip('Press and Push')
        # btn.resize(btn.sizeHint())
        # btn.move(40, 50)


        # 菜单栏
        # 文件
        menu_control = self.menuBar().addMenu('File')
        act_quit = menu_control.addAction("quit")
        act_quit.triggered.connect(self.close)

        menu_help = self.menuBar().addMenu('Help')
        act_about = menu_help.addAction('about...')
        act_about.triggered.connect(self.about)



        # 系统设置
        system_control = self.menuBar().addMenu('系统设置')
        act_quit = system_control.addAction("数据库设置")
        act_quit.triggered.connect(self.openDataBaseDiolag)

        menu_help = self.menuBar().addMenu('关于我们')
        act_about = system_control.addAction('about...')
        act_about.triggered.connect(self.about)


        #工具栏
        exitAct = QAction(QIcon('icons/myapp.ico'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        exitAct.setStatusTip('Be careful')
        self.toolbar = self.addToolBar('Exitoo')
        self.toolbar.addAction(exitAct)


        # 状态栏
        self.statusBar().showMessage('程序已就绪...')
        self.show()

    def openDataBaseDiolag(self):
        self.database=DataBaseDialog(self.settings)
        self.database.show()

    def about(self):
        QMessageBox.about(self,"about this software","wise system")
    def aboutqt(self):
        QMessageBox.aboutQt(self)

    def closeEvent(self, event):
        # 重新定义 colseEvent
        reply = QMessageBox.question\
        (self, '信息',
        '你确定要退出吗？',
        QMessageBox.Yes,
        QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #center method
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,\
        (screen.height()-size.height())/2)

QApplication.addLibraryPath("./plugins")
app = QApplication(sys.argv)
app.setOrganizationName("")
app.setApplicationName("my first app")


mainwindow = MainWindow()
# mainwindow.statusBar().showMessage('程序已就绪...')

label=QLabel(mainwindow)     #在窗口中绑定label
label.setText("hello world")

mainwindow.show()
sys.exit(app.exec_())

#pyqt窗口必须在QApplication方法中使用
# app = QtWidgets.QApplication(sys.argv)

# label=QtWidgets.QLabel("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")
# #qt支持html标签，强大吧
# #有了实例，就需要用show()让他显示
# label.show()

# widget = QtWidgets.QWidget()
# widget.resize(400, 100)
# widget.setWindowTitle("This is a demo for PyQt Widget.")
# widget.show()

# exit(app.exec_())