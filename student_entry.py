# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_entry.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 494)
        MainWindow.setMaximumSize(QtCore.QSize(16777210, 16777213))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_studentsDetails = QtWidgets.QLabel(self.centralwidget)
        self.label_studentsDetails.setMaximumSize(QtCore.QSize(16777215, 16777213))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_studentsDetails.setFont(font)
        self.label_studentsDetails.setObjectName("label_studentsDetails")
        self.verticalLayout.addWidget(self.label_studentsDetails)
        self.student_details = QtWidgets.QGridLayout()
        self.student_details.setObjectName("student_details")
        self.dateBirth = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBirth.sizePolicy().hasHeightForWidth())
        self.dateBirth.setSizePolicy(sizePolicy)
        self.dateBirth.setStatusTip("")
        self.dateBirth.setCalendarPopup(True)
        self.dateBirth.setObjectName("dateBirth")
        self.student_details.addWidget(self.dateBirth, 1, 5, 1, 1)
        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setObjectName("label_family")
        self.student_details.addWidget(self.label_family, 0, 4, 1, 1)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.student_details.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name2.setObjectName("lineEdit_name2")
        self.student_details.addWidget(self.lineEdit_name2, 0, 2, 1, 1)
        self.lineEdit_diagnosis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_diagnosis.setObjectName("lineEdit_diagnosis")
        self.student_details.addWidget(self.lineEdit_diagnosis, 1, 3, 1, 1)
        self.label_birthdate = QtWidgets.QLabel(self.centralwidget)
        self.label_birthdate.setObjectName("label_birthdate")
        self.student_details.addWidget(self.label_birthdate, 1, 4, 1, 1)
        self.lineEdit_name3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name3.setObjectName("lineEdit_name3")
        self.student_details.addWidget(self.lineEdit_name3, 0, 3, 1, 1)
        self.lineEdit_family = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_family.setObjectName("lineEdit_family")
        self.student_details.addWidget(self.lineEdit_family, 0, 5, 1, 1)
        self.label_birthplace = QtWidgets.QLabel(self.centralwidget)
        self.label_birthplace.setObjectName("label_birthplace")
        self.student_details.addWidget(self.label_birthplace, 1, 0, 1, 1)
        self.lineEdit_birthplace = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_birthplace.setObjectName("lineEdit_birthplace")
        self.student_details.addWidget(self.lineEdit_birthplace, 1, 1, 1, 1)
        self.label_nationality = QtWidgets.QLabel(self.centralwidget)
        self.label_nationality.setObjectName("label_nationality")
        self.student_details.addWidget(self.label_nationality, 2, 0, 1, 1)
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setObjectName("label_gender")
        self.student_details.addWidget(self.label_gender, 2, 2, 1, 1)
        self.lineEdit_nationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")
        self.student_details.addWidget(self.lineEdit_nationality, 2, 1, 1, 1)
        self.radioMale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMale.setObjectName("radioMale")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioMale)
        self.student_details.addWidget(self.radioMale, 3, 3, 1, 1)
        self.lineEdit_name1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name1.setObjectName("lineEdit_name1")
        self.student_details.addWidget(self.lineEdit_name1, 0, 1, 1, 1)
        self.lineEdit_caregiver = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_caregiver.setObjectName("lineEdit_caregiver")
        self.student_details.addWidget(self.lineEdit_caregiver, 2, 5, 1, 1)
        self.label_caregiver = QtWidgets.QLabel(self.centralwidget)
        self.label_caregiver.setObjectName("label_caregiver")
        self.student_details.addWidget(self.label_caregiver, 2, 4, 1, 1)
        self.radioFemale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioFemale.setObjectName("radioFemale")
        self.buttonGroup.addButton(self.radioFemale)
        self.student_details.addWidget(self.radioFemale, 2, 3, 1, 1)
        self.label_diagnosis = QtWidgets.QLabel(self.centralwidget)
        self.label_diagnosis.setObjectName("label_diagnosis")
        self.student_details.addWidget(self.label_diagnosis, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.student_details)
        self.label_addressDetails = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_addressDetails.setFont(font)
        self.label_addressDetails.setObjectName("label_addressDetails")
        self.verticalLayout.addWidget(self.label_addressDetails)
        self.address_details = QtWidgets.QGridLayout()
        self.address_details.setObjectName("address_details")
        self.label_wallaya = QtWidgets.QLabel(self.centralwidget)
        self.label_wallaya.setObjectName("label_wallaya")
        self.address_details.addWidget(self.label_wallaya, 0, 0, 1, 1)
        self.label_lane = QtWidgets.QLabel(self.centralwidget)
        self.label_lane.setObjectName("label_lane")
        self.address_details.addWidget(self.label_lane, 1, 2, 1, 1)
        self.label_house = QtWidgets.QLabel(self.centralwidget)
        self.label_house.setObjectName("label_house")
        self.address_details.addWidget(self.label_house, 1, 4, 1, 1)
        self.lineEdit_lane = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lane.setObjectName("lineEdit_lane")
        self.address_details.addWidget(self.lineEdit_lane, 1, 3, 1, 1)
        self.lineEdit_wallaya = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_wallaya.setObjectName("lineEdit_wallaya")
        self.address_details.addWidget(self.lineEdit_wallaya, 0, 1, 1, 1)
        self.lineEdit_street = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.address_details.addWidget(self.lineEdit_street, 1, 1, 1, 1)
        self.lineEdit_block = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_block.setObjectName("lineEdit_block")
        self.address_details.addWidget(self.lineEdit_block, 0, 5, 1, 1)
        self.label_village = QtWidgets.QLabel(self.centralwidget)
        self.label_village.setObjectName("label_village")
        self.address_details.addWidget(self.label_village, 0, 2, 1, 1)
        self.lineEdit_village = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_village.setObjectName("lineEdit_village")
        self.address_details.addWidget(self.lineEdit_village, 0, 3, 1, 1)
        self.label_block = QtWidgets.QLabel(self.centralwidget)
        self.label_block.setObjectName("label_block")
        self.address_details.addWidget(self.label_block, 0, 4, 1, 1)
        self.lineEdit_house = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_house.setObjectName("lineEdit_house")
        self.address_details.addWidget(self.lineEdit_house, 1, 5, 1, 1)
        self.label_street = QtWidgets.QLabel(self.centralwidget)
        self.label_street.setObjectName("label_street")
        self.address_details.addWidget(self.label_street, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.address_details)
        self.label_contact = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_contact.setFont(font)
        self.label_contact.setObjectName("label_contact")
        self.verticalLayout.addWidget(self.label_contact)
        self.emergency_contact = QtWidgets.QGridLayout()
        self.emergency_contact.setObjectName("emergency_contact")
        self.lineEdit_contactName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contactName.setObjectName("lineEdit_contactName")
        self.emergency_contact.addWidget(self.lineEdit_contactName, 0, 1, 1, 1)
        self.label_contactRelation = QtWidgets.QLabel(self.centralwidget)
        self.label_contactRelation.setObjectName("label_contactRelation")
        self.emergency_contact.addWidget(self.label_contactRelation, 0, 2, 1, 1)
        self.label_contactName = QtWidgets.QLabel(self.centralwidget)
        self.label_contactName.setObjectName("label_contactName")
        self.emergency_contact.addWidget(self.label_contactName, 0, 0, 1, 1)
        self.lineEdit_contactRelation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contactRelation.setObjectName("lineEdit_contactRelation")
        self.emergency_contact.addWidget(self.lineEdit_contactRelation, 0, 3, 1, 1)
        self.lineEdit_contactMobile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contactMobile.setObjectName("lineEdit_contactMobile")
        self.emergency_contact.addWidget(self.lineEdit_contactMobile, 0, 5, 1, 1)
        self.label_contactMobile = QtWidgets.QLabel(self.centralwidget)
        self.label_contactMobile.setObjectName("label_contactMobile")
        self.emergency_contact.addWidget(self.label_contactMobile, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.emergency_contact)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1012, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuSave = QtWidgets.QMenu(self.menuBar)
        self.menuSave.setObjectName("menuSave")
        self.menuExport = QtWidgets.QMenu(self.menuBar)
        self.menuExport.setObjectName("menuExport")
        self.menuAssessment = QtWidgets.QMenu(self.menuBar)
        self.menuAssessment.setObjectName("menuAssessment")
        self.menuTools = QtWidgets.QMenu(self.menuAssessment)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExport_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionExport_as_PDF.setObjectName("actionExport_as_PDF")
        self.actionExport_as_Word_document = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Word_document.setObjectName("actionExport_as_Word_document")
        self.actionSensory = QtWidgets.QAction(MainWindow)
        self.actionSensory.setObjectName("actionSensory")
        self.actionResults = QtWidgets.QAction(MainWindow)
        self.actionResults.setObjectName("actionResults")
        self.actionPlan = QtWidgets.QAction(MainWindow)
        self.actionPlan.setObjectName("actionPlan")
        self.actionBattele = QtWidgets.QAction(MainWindow)
        self.actionBattele.setObjectName("actionBattele")
        self.actionPhysio = QtWidgets.QAction(MainWindow)
        self.actionPhysio.setObjectName("actionPhysio")
        self.actionBehavior = QtWidgets.QAction(MainWindow)
        self.actionBehavior.setObjectName("actionBehavior")
        self.actionSpeech = QtWidgets.QAction(MainWindow)
        self.actionSpeech.setObjectName("actionSpeech")
        self.actionSave_Record = QtWidgets.QAction(MainWindow)
        self.actionSave_Record.setEnabled(True)
        self.actionSave_Record.setObjectName("actionSave_Record")
        self.actionLock = QtWidgets.QAction(MainWindow)
        self.actionLock.setObjectName("actionLock")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setEnabled(True)
        self.actionEdit.setObjectName("actionEdit")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.menuSave.addAction(self.actionSave_Record)
        self.menuSave.addAction(self.actionLock)
        self.menuSave.addAction(self.actionEdit)
        self.menuExport.addAction(self.actionPrint)
        self.menuExport.addAction(self.actionExport_as_Word_document)
        self.menuTools.addAction(self.actionBattele)
        self.menuTools.addAction(self.actionSensory)
        self.menuTools.addAction(self.actionPhysio)
        self.menuTools.addAction(self.actionBehavior)
        self.menuTools.addAction(self.actionSpeech)
        self.menuAssessment.addAction(self.actionPlan)
        self.menuAssessment.addAction(self.actionResults)
        self.menuAssessment.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuSave.menuAction())
        self.menuBar.addAction(self.menuExport.menuAction())
        self.menuBar.addAction(self.menuAssessment.menuAction())

        self.retranslateUi(MainWindow)
        self.actionSave_Record.triggered.connect(MainWindow.saveRecord)
        self.actionEdit.triggered.connect(MainWindow.editRecord)
        self.actionLock.triggered.connect(MainWindow.lockRecord)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information"))
        self.centralwidget.setAccessibleName(_translate("MainWindow", "Student information"))
        self.centralwidget.setAccessibleDescription(_translate("MainWindow", "Student information form"))
        self.label_studentsDetails.setText(_translate("MainWindow", "Student Details"))
        self.dateBirth.setAccessibleName(_translate("MainWindow", "Date of birth"))
        self.label_family.setText(_translate("MainWindow", "Family Name"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.lineEdit_name2.setAccessibleName(_translate("MainWindow", "Father\'s name"))
        self.lineEdit_diagnosis.setAccessibleName(_translate("MainWindow", "Hospital diagnosis"))
        self.label_birthdate.setText(_translate("MainWindow", "Date of Birth"))
        self.lineEdit_name3.setAccessibleName(_translate("MainWindow", "Grandfather\'s name"))
        self.lineEdit_family.setAccessibleName(_translate("MainWindow", "Family name"))
        self.label_birthplace.setText(_translate("MainWindow", "Birth Place"))
        self.lineEdit_birthplace.setAccessibleName(_translate("MainWindow", "Birthplace"))
        self.label_nationality.setText(_translate("MainWindow", "Nationality"))
        self.label_gender.setText(_translate("MainWindow", "Gender"))
        self.lineEdit_nationality.setAccessibleName(_translate("MainWindow", "Nationality"))
        self.radioMale.setText(_translate("MainWindow", "Male"))
        self.lineEdit_name1.setAccessibleName(_translate("MainWindow", "First name"))
        self.lineEdit_caregiver.setAccessibleName(_translate("MainWindow", "Primary caregiver"))
        self.label_caregiver.setText(_translate("MainWindow", "Primary Caregiver"))
        self.radioFemale.setText(_translate("MainWindow", "Female"))
        self.label_diagnosis.setText(_translate("MainWindow", "Hospital Diagnosis"))
        self.label_addressDetails.setText(_translate("MainWindow", "Address Details"))
        self.label_wallaya.setText(_translate("MainWindow", "Wallaya"))
        self.label_lane.setText(_translate("MainWindow", "Lane No."))
        self.label_house.setText(_translate("MainWindow", "House No."))
        self.lineEdit_lane.setAccessibleName(_translate("MainWindow", "Lane number"))
        self.lineEdit_wallaya.setAccessibleName(_translate("MainWindow", "Wallaya"))
        self.lineEdit_street.setAccessibleName(_translate("MainWindow", "Street"))
        self.lineEdit_block.setAccessibleName(_translate("MainWindow", "Block number"))
        self.label_village.setText(_translate("MainWindow", "Village"))
        self.lineEdit_village.setAccessibleName(_translate("MainWindow", "Village"))
        self.label_block.setText(_translate("MainWindow", "Block No."))
        self.lineEdit_house.setAccessibleName(_translate("MainWindow", "House number"))
        self.label_street.setText(_translate("MainWindow", "Street"))
        self.label_contact.setText(_translate("MainWindow", "Emergency Contact"))
        self.lineEdit_contactName.setAccessibleName(_translate("MainWindow", "Emergency contact name"))
        self.label_contactRelation.setText(_translate("MainWindow", "Relation to student"))
        self.label_contactName.setText(_translate("MainWindow", "Name"))
        self.lineEdit_contactRelation.setAccessibleName(_translate("MainWindow", "Emergency contact relation to student"))
        self.lineEdit_contactMobile.setAccessibleName(_translate("MainWindow", "Mobile number for emergency ctconta"))
        self.label_contactMobile.setText(_translate("MainWindow", "Mobile No."))
        self.menuSave.setTitle(_translate("MainWindow", "Record"))
        self.menuExport.setTitle(_translate("MainWindow", "Print"))
        self.menuAssessment.setTitle(_translate("MainWindow", "Details"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionExport_as_PDF.setText(_translate("MainWindow", "Export as PDF"))
        self.actionExport_as_Word_document.setText(_translate("MainWindow", "Export as Word document"))
        self.actionSensory.setText(_translate("MainWindow", "Sensory"))
        self.actionResults.setText(_translate("MainWindow", "Results"))
        self.actionPlan.setText(_translate("MainWindow", "Plan"))
        self.actionBattele.setText(_translate("MainWindow", "Battele"))
        self.actionPhysio.setText(_translate("MainWindow", "Physiotherapy"))
        self.actionBehavior.setText(_translate("MainWindow", "Behaviour"))
        self.actionSpeech.setText(_translate("MainWindow", "Speech and Language"))
        self.actionSave_Record.setText(_translate("MainWindow", "Save Record"))
        self.actionLock.setText(_translate("MainWindow", "Lock Record"))
        self.actionEdit.setText(_translate("MainWindow", "Edit Record"))
        self.actionPrint.setText(_translate("MainWindow", "Print details"))
