# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_students.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 863)
        MainWindow.setMaximumSize(QtCore.QSize(16777209, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.setAcceptDrops(False)
        self.tableView.setToolTipDuration(2)
        self.tableView.setStyleSheet("")
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setAutoScroll(False)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 22))
        self.menubar.setObjectName("menubar")
        self.menuPrint = QtWidgets.QMenu(self.menubar)
        self.menuPrint.setObjectName("menuPrint")
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
        self.actionPrint_full_list = QtWidgets.QAction(MainWindow)
        self.actionPrint_full_list.setObjectName("actionPrint_full_list")
        self.actionPrint_selected = QtWidgets.QAction(MainWindow)
        self.actionPrint_selected.setObjectName("actionPrint_selected")
        self.menuPrint.addAction(self.actionPrint_selected)
        self.menuPrint.addAction(self.actionPrint_full_list)
        self.menubar.addAction(self.menuPrint.menuAction())

        self.retranslateUi(MainWindow)
        self.actionPrint_full_list.triggered.connect(MainWindow.printList)
        self.actionPrint_selected.triggered.connect(MainWindow.printSelection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Students"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.actionA_to_Z.setText(_translate("MainWindow", "Last Name A to Z"))
        self.actionZ_to_A.setText(_translate("MainWindow", "Last Name Z to A"))
        self.actionDate_of_Birth.setText(_translate("MainWindow", "Date of Birth"))
        self.actionRecord_First_to_Last.setText(_translate("MainWindow", "Record First to Last"))
        self.actionRecord_Last_to_First.setText(_translate("MainWindow", "Record Last to First"))
        self.actionPrint_full_list.setText(_translate("MainWindow", "Print list"))
        self.actionPrint_selected.setText(_translate("MainWindow", "Print selected records"))
