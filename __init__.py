from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import validateIdentityUI


app = QtWidgets.QApplication(sys.argv)
win = validateIdentityUI.Ui_validateIdentityUI()
win.show()
sys.exit(app.exec_())