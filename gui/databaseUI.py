#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-10 18:29:56
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

from PyQt5.QtWidgets import *
class DataBaseDialog(QDialog):
    def __init__(self,settings):
        self.settings=settings
        super(DataBaseDialog,self).__init__()
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("数据库设置")
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("数据库设置")
        layout = QFormLayout()
        layout.addRow(QLabel("IP地址:"), QLineEdit())
        layout.addRow(QLabel("端口号:"), QLineEdit())
        layout.addRow(QLabel("数据库名称:"), QLineEdit())
        # layout.addRow("端口号:", QSpinBox())
        # layout.addRow(QLabel("other infomation:"), QTextEdit())
        self.formGroupBox.setLayout(layout)

    def accept(self):
        self.settings.setValue("xxxxxxxxxxx", 698)
        QMessageBox.information(self,"","保存成功")
    def aboutqt(self):
        QMessageBox.aboutQt(self)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
