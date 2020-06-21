# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(251, 186)
        Login.setMaximumSize(QtCore.QSize(16777146, 16777215))
        Login.setFocusPolicy(QtCore.Qt.StrongFocus)
        Login.setStyleSheet("font: 11pt \"Sans\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Login)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 150, 301, 32))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.buttonBox.setFont(font)
        self.buttonBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBox.setToolTipDuration(2)
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.usernameLabel = QtWidgets.QLabel(Login)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.usernameLabel.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.usernameLabel.setStyleSheet("font: 11pt \"Sans\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Login)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 80, 81, 17))
        self.passwordLabel.setObjectName("passwordLabel")
        self.usernameLine = QtWidgets.QLineEdit(Login)
        self.usernameLine.setGeometry(QtCore.QRect(20, 30, 211, 41))
        self.usernameLine.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.usernameLine.setAcceptDrops(False)
        self.usernameLine.setToolTip("")
        self.usernameLine.setAccessibleDescription("")
        self.usernameLine.setInputMask("")
        self.usernameLine.setMaxLength(32767)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(Login)
        self.passwordLine.setGeometry(QtCore.QRect(20, 100, 211, 41))
        self.passwordLine.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.passwordLine.setAcceptDrops(False)
        self.passwordLine.setAccessibleDescription("")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setProperty("setEchoMode", "")
        self.passwordLine.setObjectName("passwordLine")

        self.retranslateUi(Login)
        self.buttonBox.accepted.connect(Login.accept)
        self.buttonBox.rejected.connect(Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.usernameLabel.setText(_translate("Login", "Username"))
        self.passwordLabel.setText(_translate("Login", "Password"))
        self.usernameLine.setAccessibleName(_translate("Login", "Username"))
        self.passwordLine.setAccessibleName(_translate("Login", "Password"))
