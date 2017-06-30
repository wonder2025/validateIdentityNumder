# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import QtWidgets

# 从 ui.py 文件里 import ui类
from validateIdentityUI import Ui_validateIdentityUI


class MyDialog(Ui_validateIdentityUI):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        # 调用内部的 setupUi() ，本身对象作为参数
        self.setupUi(self)
        # 连接 QPushButton 的点击信号到槽 BigWork()
        self.pushButton.clicked.connect(self.validate_excel)
        self.pushButton_2.clicked.connect(self.stop_validate)
        # self.pushButton.clicked.connect(self.BigWork)
    def validate_excel(self):
        try:
            #把按钮禁用掉
            self.pushButton.setDisabled(True)
            #import 自己的进程类
            from threads import BigWorkThread
            #新建对象，传入参数
            filePath = self.lineEdit.text();
            print(filePath)
            houzui = ""
            if len(filePath) > 0:
                list = filePath.split('/')
                zui = list[len(list) - 1]
                houzui = zui.split(".")
                result_name = houzui[0] + "_" + "校验结果" + "." + houzui[1]
                path = ""
                for i in range(len(list) - 1):
                    path += list[i] + "\\"
                inpath = path + zui
                exportFilePath = path + result_name
                print(inpath)
                print(exportFilePath)
                self.bwThread = BigWorkThread(int(1),inpath,exportFilePath,True )
                # 连接子进程的信号和槽函数
                self.bwThread.finishSignal.connect(self.callbacklog)
                # 开始执行 run() 函数里的内容
                self.bwThread.start()
                # validateIdentity.read_excel(1, 2, 5, inpath, exportFilePath)
            else:
                self.setTextBrowser("文件路径不能为空")
                print("文件路径不能为空")
        except Exception as err:
            print(err)
            self.setTextBrowser("==========================")
            self.setTextBrowser("校验失败!错误描述:"+err)

    #增加形参准备接受返回值 ls
    def callbacklog(self,ls):
        #使用传回的返回值
        for word in ls:
            self.setTextBrowser(time.strftime("%Y/%m/%d %H:%M", time.localtime())+" "+word)
            print (time.strftime("%Y/%m/%d %H:%M", time.localtime())+" "+word)
        #恢复按钮
        self.pushButton.setDisabled(False)
    def stop_validate(self):
        # 把按钮禁用掉
        self.pushButton_2.setDisabled(True)
        self.bwThread.stop()
        self.pushButton_2.setDisabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 新建类对象
    Dialog = MyDialog()
    # 显示类对象
    Dialog.show()
    sys.exit(app.exec_())