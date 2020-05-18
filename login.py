# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(251, 186)
        Dialog.setMaximumSize(QtCore.QSize(16777146, 16777215))
        Dialog.setStyleSheet("font: 11pt \"Sans\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 150, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.usernameLabel.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.usernameLabel.setStyleSheet("font: 11pt \"Sans\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 80, 81, 17))
        self.passwordLabel.setObjectName("passwordLabel")
        self.usernameLine = QtWidgets.QLineEdit(Dialog)
        self.usernameLine.setGeometry(QtCore.QRect(20, 30, 211, 41))
        self.usernameLine.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.usernameLine.setInputMask("")
        self.usernameLine.setMaxLength(32767)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(Dialog)
        self.passwordLine.setGeometry(QtCore.QRect(20, 100, 211, 41))
        self.passwordLine.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setProperty("setEchoMode", "")
        self.passwordLine.setObjectName("passwordLine")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

