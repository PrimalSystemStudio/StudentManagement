import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(251, 186)
        Dialog.setMaximumSize(QtCore.QSize(16777146, 16777215))
        Dialog.setStyleSheet("font: 11pt \"Sans\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 150, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.usernameLabel.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 80, 81, 17))
        self.passwordLabel.setObjectName("passwordLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(20, 30, 211, 41))
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(20, 100, 211, 41))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setProperty("setEchoMode", "")
        self.passwordLineEdit.setObjectName("passwordLineEdit")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.handleLogin)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Login", "Login"))
        self.usernameLabel.setText(_translate("Login", "Username"))
        self.passwordLabel.setText(_translate("Login", "Password"))

    def handleLogin(self):
        if (self.usernameLineEdit.text() == 'username' and
                self.passwordLineEdit.text() == 'password'):
            QtWidgets.QApplication.exit(True)
        else:
            warn = QtWidgets.QMessageBox()
            warn.setIcon(QtWidgets.QMessageBox.Warning)
            warn.setText(
                "Username and password combination is incorrect, try again")
            warn.setWindowTitle("Login Error")
            warn.setStandardButtons(
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            warn.exec_()


def play():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
