# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_students.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 907)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 961, 911))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 22))
        self.menubar.setObjectName("menubar")
        self.menuPrint = QtWidgets.QMenu(self.menubar)
        self.menuPrint.setObjectName("menuPrint")
        self.menuEdit_Record = QtWidgets.QMenu(self.menubar)
        self.menuEdit_Record.setObjectName("menuEdit_Record")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionA_to_Z = QtWidgets.QAction(MainWindow)
        self.actionA_to_Z.setObjectName("actionA_to_Z")
        self.actionZ_to_A = QtWidgets.QAction(MainWindow)
        self.actionZ_to_A.setObjectName("actionZ_to_A")
        self.actionDate_of_Birth = QtWidgets.QAction(MainWindow)
        self.actionDate_of_Birth.setObjectName("actionDate_of_Birth")
        self.actionRecord_First_to_Last = QtWidgets.QAction(MainWindow)
        self.actionRecord_First_to_Last.setObjectName("actionRecord_First_to_Last")
        self.actionRecord_Last_to_First = QtWidgets.QAction(MainWindow)
        self.actionRecord_Last_to_First.setObjectName("actionRecord_Last_to_First")
        self.menuView.addAction(self.actionA_to_Z)
        self.menuView.addAction(self.actionZ_to_A)
        self.menuView.addAction(self.actionDate_of_Birth)
        self.menuView.addAction(self.actionRecord_First_to_Last)
        self.menuView.addAction(self.actionRecord_Last_to_First)
        self.menubar.addAction(self.menuPrint.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit_Record.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.menuEdit_Record.setTitle(_translate("MainWindow", "View Record"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionA_to_Z.setText(_translate("MainWindow", "Last Name A to Z"))
        self.actionZ_to_A.setText(_translate("MainWindow", "Last Name Z to A"))
        self.actionDate_of_Birth.setText(_translate("MainWindow", "Date of Birth"))
        self.actionRecord_First_to_Last.setText(_translate("MainWindow", "Record First to Last"))
        self.actionRecord_Last_to_First.setText(_translate("MainWindow", "Record Last to First"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

