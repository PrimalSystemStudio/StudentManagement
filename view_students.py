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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777202, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableView.setFont(font)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.setAcceptDrops(False)
        self.tableView.setToolTipDuration(5)
        self.tableView.setStyleSheet("")
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setAutoScroll(False)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
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
        self.actionPrint_full_list = QtWidgets.QAction(MainWindow)
        self.actionPrint_full_list.setObjectName("actionPrint_full_list")
        self.actionPrint_selected = QtWidgets.QAction(MainWindow)
        self.actionPrint_selected.setObjectName("actionPrint_selected")
        self.actionDelete_Entry = QtWidgets.QAction(MainWindow)
        self.actionDelete_Entry.setObjectName("actionDelete_Entry")
        self.actionEdit_Entry = QtWidgets.QAction(MainWindow)
        self.actionEdit_Entry.setObjectName("actionEdit_Entry")
        self.actionDuplicate_Entry = QtWidgets.QAction(MainWindow)
        self.actionDuplicate_Entry.setObjectName("actionDuplicate_Entry")
        self.menuPrint.addAction(self.actionPrint_selected)
        self.menuPrint.addAction(self.actionPrint_full_list)
        self.menubar.addAction(self.menuPrint.menuAction())

        self.retranslateUi(MainWindow)
        self.actionPrint_full_list.triggered.connect(MainWindow.printList)
        self.actionPrint_selected.triggered.connect(MainWindow.printSelection)
        self.tableView.customContextMenuRequested['QPoint'].connect(MainWindow.contextMenu)
        self.actionDelete_Entry.triggered.connect(MainWindow.deleteEntry)
        self.actionEdit_Entry.triggered.connect(MainWindow.editEntry)
        self.actionDuplicate_Entry.triggered.connect(MainWindow.dupEntry)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Students"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.actionPrint_full_list.setText(_translate("MainWindow", "Print list"))
        self.actionPrint_selected.setText(_translate("MainWindow", "Print selected records"))
        self.actionDelete_Entry.setText(_translate("MainWindow", "Delete Entry"))
        self.actionEdit_Entry.setText(_translate("MainWindow", "Edit Entry"))
        self.actionDuplicate_Entry.setText(_translate("MainWindow", "Duplicate Entry"))
