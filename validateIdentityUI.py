# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validateIdentityUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore,QtGui,QtWidgets


class Ui_validateIdentityUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_validateIdentityUI,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, validateIdentityUI):
        validateIdentityUI.setObjectName("validateIdentityUI")
        validateIdentityUI.resize(635, 419)
        self.centralwidget = QtWidgets.QWidget(validateIdentityUI)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 280, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 100, 501, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 60, 401, 43))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_2.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.horizontalLayout_2.addWidget(self.commandLinkButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(80, 29, 451, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.widget1)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(50, 130, 520, 231))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        validateIdentityUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(validateIdentityUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 23))
        self.menubar.setObjectName("menubar")
        validateIdentityUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(validateIdentityUI)
        self.statusbar.setObjectName("statusbar")
        validateIdentityUI.setStatusBar(self.statusbar)

        self.retranslateUi(validateIdentityUI)
        QtCore.QMetaObject.connectSlotsByName(validateIdentityUI)

    def retranslateUi(self, validateIdentityUI):
        _translate = QtCore.QCoreApplication.translate
        validateIdentityUI.setWindowTitle(_translate("validateIdentityUI", "校验身份证"))
        self.commandLinkButton.setText(_translate("validateIdentityUI", "开始"))
        self.commandLinkButton_2.setText(_translate("validateIdentityUI", "停止"))
        self.label.setText(_translate("validateIdentityUI", "文件路径"))
        self.toolButton.setText(_translate("validateIdentityUI", "..."))
        self.textBrowser.setHtml(_translate("validateIdentityUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">使用说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">1.支持后缀为</span><span style=\" color:#ff0000;\">.xlsx</span><span style=\" color:#5500ff;\">的excel文件的校验；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">2.身份证号所在列的标题必须为“</span><span style=\" color:#ff0000;\">身份证号码</span><span style=\" color:#5500ff;\">”，且身份证号所在</span><span style=\" color:#ff0000;\">sheet必须是第一个</span><span style=\" color:#5500ff;\">；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">3.身份证号校验规则为：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">（1）长度必须为18位；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">（2）前17位为数字，最后1位校验码为数字或X</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">（3）对前2位的省区划进行判断，属于31个省市自治区的区划之一；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">（4）第7至14位为yyyymmdd出生日期，18&lt;=年龄&lt;=60；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5500ff;\">（5）最后一位校验码正确</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#5500ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#5500ff;\"><br /></p></body></html>"))

