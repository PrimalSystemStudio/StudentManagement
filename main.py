# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F or try fbs
# Username and password are both "admin"
import sys
import login
import landing
import student_entry
import view_students
import plan
import about
import stats
import guide
from PyQt5 import QtCore, QtWidgets, QtGui, QtSql, QtPrintSupport

# How many hours been spent on this project (for personal use)
hours = 36


# Define login dialogue
class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_Login()
        self.ui.setupUi(self)

        # Check if username/password combo is correct
        # If it is then open the landing page
        if self.exec_() == QtWidgets.QDialog.Accepted:
            if (self.ui.usernameLine.text() == 'admin' and
                    self.ui.passwordLine.text() == 'admin'):
                self.main_Ui = Landing()
                self.main_Ui.show()
            elif (self.ui.usernameLine.text() == '' or
                    self.ui.passwordLine.text() == ''):
                warn = QtWidgets.QMessageBox()
                warn.setIcon(QtWidgets.QMessageBox.Warning)
                warn.setText(
                    "Please enter a username and password.")
                warn.setStandardButtons(
                    QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                warn.buttonClicked.connect(self.reinit)
                warn.exec_()
            else:
                warn = QtWidgets.QMessageBox()
                warn.setIcon(QtWidgets.QMessageBox.Warning)
                warn.setText(
                   "Username and password combination is incorrect, try again")
                warn.setStandardButtons(
                    QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                warn.buttonClicked.connect(self.reinit)
                warn.exec_()
        else:
            sys.exit()

    # Reopen dialog if login attempt is unsuccessful
    def reinit(self, y):
        print("Button pressed is ", y.text())
        self.__init__()


# Define landing window
class Landing(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = landing.Ui_Management()
        self.ui.setupUi(self)

    def about(self):
        print("about button pressed")

    def browse(self):
        self.viewstudents = ViewStudents()
        self.viewstudents.show()

    def guide(self):
        print("guide button pressed")

    def register(self):
        self.newstudent = NewStudent()
        self.newstudent.show()

    def report(self):
        self.plan = Plan()
        self.plan.show()

    def stats(self):
        print("stats button pressed")


# Window for browsing the student database
class ViewStudents(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = view_students.Ui_MainWindow()
        self.ui.setupUi(self)

        # Define the database
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("documents/students.db")
        self.data.open()
        self.table = QtSql.QSqlTableModel()
        self.table.setTable('student_list')
        self.table.select()

        # Show the data in the table
        # Only show first 7 columns
        self.ui.tableView.setModel(self.table)
        for n in range(8, 20):
            self.ui.tableView.setColumnHidden(n, True)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.show()

    def printList(self):
        # Placeholder for print function
        pass

    def printSelection(self):
        # Placeholder for print function
        pass

    def contextMenu(self):
        # Shows on right click
        self.clickMenu = QtWidgets.QMenu()
        self.clickMenu.addAction(self.ui.actionDelete_Entry)
        self.clickMenu.addAction(self.ui.actionEdit_Entry)
        self.clickMenu.addAction(self.ui.actionDuplicate_Entry)
        self.clickMenu.popup(QtGui.QCursor.pos())

    def deleteEntry(self):
        # To remove a row of data
        # Warns before deleting the entry
        warn = QtWidgets.QMessageBox()
        warn.setIcon(QtWidgets.QMessageBox.Warning)
        warn.setText(
            "This will delete all information on this student. Are you sure?")
        warn.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if warn.exec_() == 16384:   # If "yes" is pressed
            index = self.ui.tableView.selectedIndexes()
            if index != []:
                self.table.removeRow(index[0].row())

    def editEntry(self):
        # Opens Student View populated with student data
        index = self.ui.tableView.selectedIndexes()
        global selected  # Currently highlighted row
        if index != []:
            selected = index[0].row()
        self.viewstudent = Student()
        self.viewstudent.show()

    def dupEntry(self):
        # Add new entry like the clicked entry
        # Duplicated entry does not include therapy plan and assessments
        index = self.ui.tableView.selectedIndexes()
        record = self.table.record(index[0].row())
        self.table.last_id = QtSql.QSqlQuery(
            "SELECT MAX(ID) FROM student_list")  # Find the last ID in table
        self.table.last_id.last()
        self.table.dupRecord = self.table.primaryValues(0)
        for x in range(1, 18):
            self.table.dupRecord.setValue(x, record.value(x))
        self.table.dupRecord.setValue(
            0, self.table.last_id.value(0) + 1)

        # Insert new record into the table
        self.table.insertRecord(-1, self.table.dupRecord)


# Window for inputing data for a new student
class NewStudent(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = student_entry.Ui_MainWindow()
        self.ui.setupUi(self)

        # Record starts off editable
        # "Edit record" is greyed out until the record is locked
        self.ui.actionEdit.setEnabled(False)

        # Grey out all actions
        self.ui.menuPrint.setEnabled(False)
        self.ui.menuExport.setEnabled(False)
        self.ui.menuAssessment.setEnabled(False)

        # Define the database
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("documents/students.db")
        self.data.open()
        self.table = QtSql.QSqlTableModel()
        self.table.setTable('student_list')
        self.table.select()

    def saveRecord(self):
        if (self.ui.lineEdit_name1.text() == '' or
                self.ui.lineEdit_name1.text() == ' ' or
                self.ui.lineEdit_family.text() == '' or
                self.ui.lineEdit_family.text() == ' '):
            warn = QtWidgets.QMessageBox()
            warn.setIcon(QtWidgets.QMessageBox.Warning)
            warn.setText(
               "Student cannot have no first or last name")
            warn.setStandardButtons(
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            warn.exec_()
        else:
            # Find the last ID in the table
            self.table.last_id = QtSql.QSqlQuery(
                "SELECT MAX(ID) FROM student_list")
            self.table.last_id.last()

            # Get info entered and put into a new record
            self.table.newRecord = self.table.primaryValues(0)
            self.table.newRecord.setValue(
                0, self.table.last_id.value(0) + 1)
            self.table.newRecord.setValue(
                1, self.ui.lineEdit_name1.text() +
                " " + self.ui.lineEdit_name2.text() +
                " " + self.ui.lineEdit_name3.text())
            self.table.newRecord.setValue(
                2, self.ui.lineEdit_family.text())
            self.birthdate = self.ui.dateBirth.dateTime()
            self.table.newRecord.setValue(
                3, self.ui.dateBirth.textFromDateTime(self.birthdate))
            self.table.newRecord.setValue(
                4, self.ui.lineEdit_birthplace.text())
            self.table.newRecord.setValue(
                5, self.ui.lineEdit_diagnosis.text())
            self.table.newRecord.setValue(
                6, self.ui.lineEdit_nationality.text())

            if self.ui.radioFemale.isChecked():
                self.table.newRecord.setValue(7, "Female")
            elif self.ui.radioMale.isChecked():
                self.table.newRecord.setValue(7, "Male")
            elif self.ui.radioOther.isChecked():
                self.table.newRecord.setValue(7, "Other")

            self.table.newRecord.setValue(
                8, self.ui.lineEdit_caregiver.text())
            self.table.newRecord.setValue(
                9, self.ui.lineEdit_contactName.text())
            self.table.newRecord.setValue(
                10, self.ui.lineEdit_contactMobile.text())
            self.table.newRecord.setValue(
                11, self.ui.lineEdit_wallaya.text())
            self.table.newRecord.setValue(
                12, self.ui.lineEdit_lane.text())
            self.table.newRecord.setValue(
                13, self.ui.lineEdit_house.text())
            self.table.newRecord.setValue(
                14, self.ui.lineEdit_street.text())
            self.table.newRecord.setValue(
                15, self.ui.lineEdit_block.text())
            self.table.newRecord.setValue(
                16, self.ui.lineEdit_village.text())
            self.table.newRecord.setValue(
                17, self.ui.lineEdit_contactRelation.text())

            # Insert new record into the table and select it
            self.table.insertRecord(-1, self.table.newRecord)
            self.hide()

    def editRecord(self):
        # Allows text to be edited
        if self.ui.actionEdit.isEnabled():
            self.ui.lineEdit_birthplace.setReadOnly(False)
            self.ui.lineEdit_caregiver.setReadOnly(False)
            self.ui.lineEdit_diagnosis.setReadOnly(False)
            self.ui.lineEdit_family.setReadOnly(False)
            self.ui.lineEdit_name1.setReadOnly(False)
            self.ui.lineEdit_name2.setReadOnly(False)
            self.ui.lineEdit_name3.setReadOnly(False)
            self.ui.lineEdit_nationality.setReadOnly(False)
            self.ui.radioFemale.setEnabled(True)
            self.ui.radioMale.setEnabled(True)
            self.ui.radioOther.setEnabled(True)
            self.ui.dateBirth.setReadOnly(False)
            self.ui.lineEdit_block.setReadOnly(False)
            self.ui.lineEdit_house.setReadOnly(False)
            self.ui.lineEdit_lane.setReadOnly(False)
            self.ui.lineEdit_street.setReadOnly(False)
            self.ui.lineEdit_village.setReadOnly(False)
            self.ui.lineEdit_wallaya.setReadOnly(False)
            self.ui.lineEdit_contactMobile.setReadOnly(False)
            self.ui.lineEdit_contactName.setReadOnly(False)
            self.ui.lineEdit_contactRelation.setReadOnly(False)
            self.ui.actionLock.setEnabled(True)
            self.ui.actionEdit.setEnabled(False)

    def lockRecord(self):
        # Stops text from being edited
        if self.ui.actionLock.isEnabled():
            self.ui.lineEdit_birthplace.setReadOnly(True)
            self.ui.lineEdit_caregiver.setReadOnly(True)
            self.ui.lineEdit_diagnosis.setReadOnly(True)
            self.ui.lineEdit_family.setReadOnly(True)
            self.ui.lineEdit_name1.setReadOnly(True)
            self.ui.lineEdit_name2.setReadOnly(True)
            self.ui.lineEdit_name3.setReadOnly(True)
            self.ui.lineEdit_nationality.setReadOnly(True)
            self.ui.radioFemale.setEnabled(False)
            self.ui.radioMale.setEnabled(False)
            self.ui.radioOther.setEnabled(False)
            self.ui.dateBirth.setReadOnly(True)
            self.ui.lineEdit_block.setReadOnly(True)
            self.ui.lineEdit_house.setReadOnly(True)
            self.ui.lineEdit_lane.setReadOnly(True)
            self.ui.lineEdit_street.setReadOnly(True)
            self.ui.lineEdit_village.setReadOnly(True)
            self.ui.lineEdit_wallaya.setReadOnly(True)
            self.ui.lineEdit_contactMobile.setReadOnly(True)
            self.ui.lineEdit_contactName.setReadOnly(True)
            self.ui.lineEdit_contactRelation.setReadOnly(True)
            self.ui.actionEdit.setEnabled(True)
            self.ui.actionLock.setEnabled(False)


# Window for editing data for a new student
class Student(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = student_entry.Ui_MainWindow()
        self.ui.setupUi(self)

        # Select table in the database
        self.table = QtSql.QSqlTableModel()
        self.table.setTable('student_list')
        self.table.select()

        # If a record is highlighted, it will be selected
        try:
            selected
        except NameError:
            record = self.table.record(0)
        else:
            record = self.table.record(selected)

        # Populate the entries with data from the database
        self.ui.label_studentsDetails.setText(
            "Student Details [ID " + str(record.value(0)) + "]")
        self.ui.lineEdit_birthplace.setText(record.value(4))
        self.ui.lineEdit_caregiver.setText(record.value(8))
        self.ui.lineEdit_diagnosis.setText(record.value(5))
        self.ui.lineEdit_family.setText(record.value(2))
        name = record.value(1)
        name = name.split(' ')
        self.ui.lineEdit_name1.setText(name[0])
        if len(name) > 1:
            self.ui.lineEdit_name2.setText(name[1])
            if len(name) > 2:
                self.ui.lineEdit_name3.setText(name[2])
        self.ui.lineEdit_nationality.setText(record.value(6))
        if record.value(7) == "Female":
            self.ui.radioFemale.setChecked(True)
            self.ui.radioMale.setChecked(False)
            self.ui.radioOther.setChecked(False)
        elif record.value(7) == "Male":
            self.ui.radioMale.setChecked(True)
            self.ui.radioFemale.setChecked(False)
            self.ui.radioOther.setChecked(False)
        elif record.value(7) == "Other":
            self.ui.radioMale.setChecked(False)
            self.ui.radioFemale.setChecked(False)
            self.ui.radioOther.setChecked(True)
        dateBirth = record.value(3)
        dateBirth = QtCore.QDate.fromString(dateBirth, "dd/MM/yyyy")
        self.ui.dateBirth.setDate(dateBirth)
        self.ui.lineEdit_contactMobile.setText(str(record.value(10)))
        self.ui.lineEdit_contactName.setText(record.value(9))
        self.ui.lineEdit_contactRelation.setText(str(record.value(8)))
        self.ui.lineEdit_wallaya.setText(record.value(11))
        self.ui.lineEdit_lane.setText(record.value(12))
        self.ui.lineEdit_house.setText(record.value(13))
        self.ui.lineEdit_street.setText(record.value(14))
        self.ui.lineEdit_block.setText(record.value(15))
        self.ui.lineEdit_village.setText(record.value(16))
        self.ui.lineEdit_contactRelation.setText(record.value(17))

        # "Edit record" is greyed out until the record is locked
        self.ui.actionEdit.setEnabled(False)
        self.ui.actionLock.setEnabled(True)

        # Connect actions to relevant functions
        self.ui.actionPrint.triggered.connect(
            self.printStudents)
        self.ui.actionExport_as_Word_document.triggered.connect(
            self.exportDocx)
        self.ui.actionBattele.triggered.connect(
            self.assessBattele)
        self.ui.actionBehavior.triggered.connect(
            self.assessBehaviour)
        self.ui.actionPhysio.triggered.connect(
            self.assessPhysio)
        self.ui.actionSpeech.triggered.connect(
            self.assessSpeech)
        self.ui.actionEdit.triggered.connect(
            self.editRecord)
        self.ui.actionLock.triggered.connect(
            self.lockRecord)
        self.ui.actionPlan.triggered.connect(
            self.viewPlan)
        self.ui.actionResults.triggered.connect(
            self.checkResults)

    def saveRecord(self):
        # Overwrite the record selected
        record = self.table.record(selected)
        self.table.wRecord = record
        self.table.wRecord.setValue(
            1, self.ui.lineEdit_name1.text() +
            " " + self.ui.lineEdit_name2.text() +
            " " + self.ui.lineEdit_name3.text())
        self.table.wRecord.setValue(
            2, self.ui.lineEdit_family.text())
        self.birthdate = self.ui.dateBirth.dateTime()
        self.table.wRecord.setValue(
            3, self.ui.dateBirth.textFromDateTime(self.birthdate))
        self.table.wRecord.setValue(
            4, self.ui.lineEdit_birthplace.text())
        self.table.wRecord.setValue(
            5, self.ui.lineEdit_diagnosis.text())
        self.table.wRecord.setValue(
            6, self.ui.lineEdit_nationality.text())

        if self.ui.radioFemale.isChecked():
            self.table.wRecord.setValue(7, "Female")
        elif self.ui.radioMale.isChecked():
            self.table.wRecord.setValue(7, "Male")
        elif self.ui.radioOther.isChecked():
            self.table.wRecord.setValue(7, "Other")

        self.table.wRecord.setValue(
            8, self.ui.lineEdit_contactRelation.text())
        self.table.wRecord.setValue(
            9, self.ui.lineEdit_contactName.text())
        self.table.wRecord.setValue(
            10, self.ui.lineEdit_contactMobile.text())
        self.table.wRecord.setValue(
            11, self.ui.lineEdit_wallaya.text())
        self.table.wRecord.setValue(
            12, self.ui.lineEdit_lane.text())
        self.table.wRecord.setValue(
            13, self.ui.lineEdit_house.text())
        self.table.wRecord.setValue(
            14, self.ui.lineEdit_street.text())
        self.table.wRecord.setValue(
            15, self.ui.lineEdit_block.text())
        self.table.wRecord.setValue(
            16, self.ui.lineEdit_village.text())
        self.table.wRecord.setValue(
            17, self.ui.lineEdit_contactRelation.text())

        # Overwrite the record in the table
        self.table.setRecord(selected, self.table.wRecord)

    def editRecord(self):
        # Allows text to be edited
        if self.ui.actionEdit.isEnabled():
            self.ui.lineEdit_birthplace.setReadOnly(False)
            self.ui.lineEdit_caregiver.setReadOnly(False)
            self.ui.lineEdit_diagnosis.setReadOnly(False)
            self.ui.lineEdit_family.setReadOnly(False)
            self.ui.lineEdit_name1.setReadOnly(False)
            self.ui.lineEdit_name2.setReadOnly(False)
            self.ui.lineEdit_name3.setReadOnly(False)
            self.ui.lineEdit_nationality.setReadOnly(False)
            self.ui.radioFemale.setEnabled(True)
            self.ui.radioMale.setEnabled(True)
            self.ui.radioOther.setEnabled(True)
            self.ui.dateBirth.setReadOnly(False)
            self.ui.lineEdit_block.setReadOnly(False)
            self.ui.lineEdit_house.setReadOnly(False)
            self.ui.lineEdit_lane.setReadOnly(False)
            self.ui.lineEdit_street.setReadOnly(False)
            self.ui.lineEdit_village.setReadOnly(False)
            self.ui.lineEdit_wallaya.setReadOnly(False)
            self.ui.lineEdit_contactMobile.setReadOnly(False)
            self.ui.lineEdit_contactName.setReadOnly(False)
            self.ui.lineEdit_contactRelation.setReadOnly(False)
            self.ui.actionLock.setEnabled(True)
            self.ui.actionEdit.setEnabled(False)

    def lockRecord(self):
        if self.ui.actionLock.isEnabled():
            # Stops text from being edited
            self.ui.lineEdit_birthplace.setReadOnly(True)
            self.ui.lineEdit_caregiver.setReadOnly(True)
            self.ui.lineEdit_diagnosis.setReadOnly(True)
            self.ui.lineEdit_family.setReadOnly(True)
            self.ui.lineEdit_name1.setReadOnly(True)
            self.ui.lineEdit_name2.setReadOnly(True)
            self.ui.lineEdit_name3.setReadOnly(True)
            self.ui.lineEdit_nationality.setReadOnly(True)
            self.ui.radioFemale.setEnabled(False)
            self.ui.radioMale.setEnabled(False)
            self.ui.radioOther.setEnabled(False)
            self.ui.dateBirth.setReadOnly(True)
            self.ui.lineEdit_block.setReadOnly(True)
            self.ui.lineEdit_house.setReadOnly(True)
            self.ui.lineEdit_lane.setReadOnly(True)
            self.ui.lineEdit_street.setReadOnly(True)
            self.ui.lineEdit_village.setReadOnly(True)
            self.ui.lineEdit_wallaya.setReadOnly(True)
            self.ui.lineEdit_contactMobile.setReadOnly(True)
            self.ui.lineEdit_contactName.setReadOnly(True)
            self.ui.lineEdit_contactRelation.setReadOnly(True)
            self.ui.actionEdit.setEnabled(True)
            self.ui.actionLock.setEnabled(False)

            # Turns text into a document
            birthdate = self.ui.dateBirth.dateTime()
            self.birthdate = self.ui.dateBirth.textFromDateTime(birthdate)
            with open('documents/record.txt', 'w+') as doc:
                doc.write(
                    "<head><meta http-equiv=\"Content-Type\""
                    + "content=\"text/html; charset=utf-8\">"
                    + "</head>\n<body>\n"
                    + "<p><b>Given Names:</b> " 
                    + self.ui.lineEdit_name1.text() + " "
                    + self.ui.lineEdit_name2.text() + " "
                    + self.ui.lineEdit_name3.text() + "</p>\n"
                    + "<p><b>Family Name:</b> "
                    + self.ui.lineEdit_family.text() + "</p>\n"
                    + "<p><b>Date of birth:</b> "
                    + self.birthdate + "</p>\n"
                    + "<p><b>Birthplace:</b> "
                    + self.ui.lineEdit_birthplace.text() + "</p>\n"
                    + "<p><b>Caregiver:</b> "
                    + self.ui.lineEdit_caregiver.text() + "</p>\n"
                    + "<p><b>Diagnosis:</b> "
                    + self.ui.lineEdit_diagnosis.text() + "</p>\n"
                    + "<p><b>Nationality:</b> "
                    + self.ui.lineEdit_nationality.text() + "</p>\n</body>")

                if self.ui.radioFemale.isChecked():
                    doc.write("<p><b>Sex:</b> Female</p>\n")
                elif self.ui.radioMale.isChecked():
                    doc.write("<p><b>Sex:</b> Male</p>\n")
                elif self.ui.radioOther.isChecked():
                    doc.write("<p><b>Sex:</b> Other</p>\n")
                else:
                    doc.write("<p><b>Sex:</b> </p>\n")
                    
                doc.write(
                    "<p><b>Address:</b> " 
                    + self.ui.lineEdit_wallaya.text()
                    + ", " + self.ui.lineEdit_village.text()
                    + ", " + self.ui.lineEdit_block.text()
                    + ", " + self.ui.lineEdit_street.text()
                    + " street, " + self.ui.lineEdit_lane.text()
                    + " lane, house" + self.ui.lineEdit_house.text() 
                    + "</p>\n"
                    + "<p><b>Emergency contact:</b> "
                    + self.ui.lineEdit_contactName.text()
                    + " (" + self.ui.lineEdit_contactRelation.text() + ") "
                    + self.ui.lineEdit_contactMobile.text() + "</p>\n")

            with open('documents/record.txt', 'r+') as doc:
                self.html = doc.read()

            self.document = QtGui.QTextDocument()
            self.document.setHtml(self.html)

    def printStudents(self):
        if self.ui.actionLock.isEnabled():
            warn = QtWidgets.QMessageBox()
            warn.setIcon(QtWidgets.QMessageBox.Critical)
            warn.setWindowTitle("Warning")
            warn.setText(
                "Please lock the record before printing.")
            warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
            warn.exec_()
        else:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec_() == QtWidgets.QDialog.Accepted:
                self.document.print_(printDialog.printer())

    def exportDocx(self):
        # If the document isn't locked, ask to lock
        # Lock is needed to build doc for export
        if self.ui.actionLock.isEnabled():
            warn = QtWidgets.QMessageBox()
            warn.setIcon(QtWidgets.QMessageBox.Critical)
            warn.setWindowTitle("Warning")
            warn.setText(
                "Please lock the record before printing.")
            warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
            warn.exec_()
        # If document is locked ask to save file
        else:
            exportDialog = QtWidgets.QFileDialog.getSaveFileName(
                self, "Save as...",
                QtCore.QDir.currentPath(),
                "Text files (*.txt *.docx *.odt)")
            if exportDialog:
                with open(exportDialog[0] + ".docx", 'w') as f:
                    f.write(self.document.toPlainText())

    def assessBattele(self):
        # Placeholder for Battele assessment
        pass

    def assessBehaviour(self):
        # Placeholder for behavioural assessment
        pass

    def assessPhysio(self):
        # Placeholder for physiotherapy assessment
        pass

    def assessSensory(self):
        # Placeholder for sensory assessment
        pass

    def assessSpeech(self):
        # Placeholder for speech assessment
        pass

    def checkResults(self):
        # Placeholder for checking results
        pass

    def viewPlan(self):
        self.plan = Plan(selected)
        self.plan.show()


class AssessBat():
    def __init__(self):
        super().__init__()
        # Placeholder until therapy section is generated
        pass


class Plan(QtWidgets.QWidget):
    def __init__(self, selected):
        super().__init__()
        self.ui = plan.Ui_Form()
        self.ui.setupUi(self)

        # Load the data and input the existing plan
        self.table = QtSql.QSqlTableModel()
        self.table.setTable('student_list')
        self.table.select()
        record = self.table.record(selected)
        self.table.wRecord = record
        self.ui.textEdit.setHtml(record.value(18))

    def save(self):
        # Overwrites selected record with new plan
        self.table.wRecord.setValue(18, self.ui.textEdit.toHtml())
        self.table.setRecord(selected, self.table.wRecord)

    def warn(self):
        # To warn user before closing
        warn = QtWidgets.QMessageBox()
        warn.setIcon(QtWidgets.QMessageBox.Warning)
        warn.setText(
            "Any unsaved changes to the text will be lost, are you sure?")
        warn.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if warn.exec_() == 16384:   # If "yes" is pressed
            self.hide()

    def bold(self):
        if self.ui.textEdit.fontWeight() == 50:
            self.ui.textEdit.setFontWeight(100)
        else:
            self.ui.textEdit.setFontWeight(50)

    def header(self):
        if self.ui.textEdit.fontPointSize() == 11.0:
            self.ui.textEdit.setFontPointSize(20)
        else:
            self.ui.textEdit.setFontPointSize(11)

    def italic(self):
        if self.ui.textEdit.fontItalic():
            self.ui.textEdit.setFontItalic(False)
        else:
            self.ui.textEdit.setFontItalic(True)

    def orderedList(self):
        cursor = self.ui.textEdit.textCursor()
        cursorList = cursor.currentList()
        if cursorList is None:  # If the block isn't a list
            cursor.createList(QtGui.QTextListFormat.ListDecimal)
            self.ui.textEdit.setTextCursor(cursor)
        elif cursorList.format().style() != -4:  # If the block isn't numbered
            cursor.createList(QtGui.QTextListFormat.ListDecimal)
            self.ui.textEdit.setTextCursor(cursor)
        else:
            newCursor = cursor.selectedText()
            newCursor = newCursor.replace("\u2029", "\n")
            blockFormat = cursor.blockFormat()
            blockFormat.setObjectIndex(-1)
            cursor.setBlockFormat(blockFormat)
            self.ui.textEdit.setTextCursor(cursor)

    def unorderedList(self):
        cursor = self.ui.textEdit.textCursor()
        cursorList = cursor.currentList()
        if cursorList is None:   # If the block is not a list
            cursor.createList(QtGui.QTextListFormat.ListSquare)
            self.ui.textEdit.setTextCursor(cursor)
        elif cursorList.format().style() != -3:   # If the block isn't bulleted
            cursor.createList(QtGui.QTextListFormat.ListSquare)
            self.ui.textEdit.setTextCursor(cursor)
        else:
            newCursor = cursor.selectedText()
            newCursor = newCursor.replace("\u2029", "\n")
            blockFormat = cursor.blockFormat()
            blockFormat.setObjectIndex(-1)
            cursor.setBlockFormat(blockFormat)
            self.ui.textEdit.setTextCursor(cursor)

    def underline(self):
        if self.ui.textEdit.fontUnderline():
            self.ui.textEdit.setFontUnderline(False)
        else:
            self.ui.textEdit.setFontUnderline(True)


class Stats(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = stats.Ui_Form()
        self.ui.setupUi(self)


class Guide(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = guide.Ui_Form()
        self.ui.setupUi(self)


class About(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = about.Ui_Form()
        self.ui.setupUi(self)


# Define QT5 app and launch login dialog
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    start = About()
    start.show()
    app.exec_()
