# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'landing.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Management(object):
    def setupUi(self, Management):
        Management.setObjectName("Management")
        Management.resize(827, 600)
        Management.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(Management)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 170, 241, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.browseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout.addWidget(self.browseButton)
        self.reportButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reportButton.setObjectName("reportButton")
        self.verticalLayout.addWidget(self.reportButton)
        self.statsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.statsButton.setObjectName("statsButton")
        self.verticalLayout.addWidget(self.statsButton)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 120, 571, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(260, 10, 561, 101))
        self.title.setMaximumSize(QtCore.QSize(16777212, 16777211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        Management.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Management)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 22))
        self.menubar.setObjectName("menubar")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuRegister = QtWidgets.QMenu(self.menubar)
        self.menuRegister.setObjectName("menuRegister")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Management.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Management)
        self.statusbar.setObjectName("statusbar")
        Management.setStatusBar(self.statusbar)
        self.actionMinimize = QtWidgets.QAction(Management)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize_window = QtWidgets.QAction(Management)
        self.actionMaximize_window.setObjectName("actionMaximize_window")
        self.actionAdd_report = QtWidgets.QAction(Management)
        self.actionAdd_report.setObjectName("actionAdd_report")
        self.actionView_reports = QtWidgets.QAction(Management)
        self.actionView_reports.setObjectName("actionView_reports")
        self.actionRegister_new_student = QtWidgets.QAction(Management)
        self.actionRegister_new_student.setObjectName("actionRegister_new_student")
        self.actionView_student_database = QtWidgets.QAction(Management)
        self.actionView_student_database.setObjectName("actionView_student_database")
        self.actionGuide_to_this_program = QtWidgets.QAction(Management)
        self.actionGuide_to_this_program.setObjectName("actionGuide_to_this_program")
        self.actionAbout = QtWidgets.QAction(Management)
        self.actionAbout.setObjectName("actionAbout")
        self.menuReport.addAction(self.actionAdd_report)
        self.menuReport.addAction(self.actionView_reports)
        self.menuRegister.addAction(self.actionRegister_new_student)
        self.menuRegister.addAction(self.actionView_student_database)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMaximize_window)
        self.menuHelp.addAction(self.actionGuide_to_this_program)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuRegister.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Management)
        self.actionMaximize_window.triggered.connect(Management.showMaximized)
        self.actionMinimize.triggered.connect(Management.showMinimized)
        self.actionAdd_report.triggered.connect(Management.report)
        self.actionRegister_new_student.triggered.connect(Management.register)
        self.actionView_reports.triggered.connect(Management.browse)
        self.actionView_student_database.triggered.connect(Management.browse)
        self.browseButton.clicked.connect(Management.browse)
        self.registerButton.clicked.connect(Management.register)
        self.reportButton.clicked.connect(Management.report)
        self.statsButton.clicked.connect(Management.stats)
        self.actionGuide_to_this_program.triggered.connect(Management.guide)
        self.actionAbout.triggered.connect(Management.about)
        QtCore.QMetaObject.connectSlotsByName(Management)

    def retranslateUi(self, Management):
        _translate = QtCore.QCoreApplication.translate
        Management.setWindowTitle(_translate("Management", "MainWindow"))
        self.registerButton.setText(_translate("Management", "Register New Student"))
        self.browseButton.setText(_translate("Management", "Browse Students"))
        self.reportButton.setText(_translate("Management", "Add Report"))
        self.statsButton.setText(_translate("Management", "Statistics"))
        self.title.setText(_translate("Management", "Association of Early Intervention for Children with Disability"))
        self.menuReport.setTitle(_translate("Management", "Report"))
        self.menuRegister.setTitle(_translate("Management", "Register"))
        self.menuWindow.setTitle(_translate("Management", "Window"))
        self.menuHelp.setTitle(_translate("Management", "Help"))
        self.actionMinimize.setText(_translate("Management", "Minimize window"))
        self.actionMaximize_window.setText(_translate("Management", "Maximize window"))
        self.actionAdd_report.setText(_translate("Management", "Add report"))
        self.actionView_reports.setText(_translate("Management", "View reports"))
        self.actionRegister_new_student.setText(_translate("Management", "Register new student"))
        self.actionView_student_database.setText(_translate("Management", "View student database"))
        self.actionGuide_to_this_program.setText(_translate("Management", "Guide to this program"))
        self.actionAbout.setText(_translate("Management", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Management = QtWidgets.QMainWindow()
    ui = Ui_Management()
    ui.setupUi(Management)
    Management.show()
    sys.exit(app.exec_())

