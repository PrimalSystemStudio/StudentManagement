# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F
# Username and password are both "admin"
import sys
import login
import landing
import student_entry
import view_students
import report
from PyQt5 import QtCore, QtWidgets, QtGui, QtSql

# How many hours been spent on this project (for personal use)
hours = 31


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
        self.newreport = NewReport()
        self.newreport.show()

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
        for x in range(8, 20):
            self.ui.tableView.setColumnHidden(x, True)
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

    def deleteEntry(self):++++
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

        # Grey out all actions until the student is saved
        self.ui.actionExport_as_PDF.setEnabled(False)
        self.ui.actionExport_as_Word_document.setEnabled(False)
        self.ui.actionSensory.setEnabled(False)
        self.ui.actionResults.setEnabled(False)
        self.ui.actionPlan.setEnabled(False)
        self.ui.menuTools.setEnabled(False)

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

            # Insert new record into the table
            self.table.insertRecord(-1, self.table.newRecord)

            # After the record is inserted all the actions to be used
            self.ui.actionExport_as_PDF.setEnabled(True)
            self.ui.actionExport_as_Word_document.setEnabled(True)
            self.ui.actionSensory.setEnabled(True)
            self.ui.actionResults.setEnabled(True)
            self.ui.actionPlan.setEnabled(True)
            self.ui.actionBattele.setEnabled(True)
            self.ui.actionPhysio.setEnabled(True)
            self.ui.actionBehavior.setEnabled(True)
            self.ui.actionSpeech.setEnabled(True)
            self.ui.menuTools.setEnabled(True)

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

    def printStudents():
        # Placeholder for print function
        pass

    def exportPDF():
        # Placeholder for PDF exporting
        pass

    def exportDocx():
        # Placeholder for .docx exporting
        pass

    def assessBattele():
        # Placeholder for behavioural assessment
        pass

    def assessBehaviour():
        # Placeholder for behavioural assessment
        pass

    def assessPhysio():
        # Placeholder for physiotherapy assessment
        pass

    def assessSensory():
        # Placeholder for sensory assessment
        pass

    def assessSpeech():
        # Placeholder for speech assessment
        pass


# Window for editing data for a new student
class Student(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = student_entry.Ui_MainWindow()
        self.ui.setupUi(self)

        self.table = QtSql.QSqlTableModel()
        self.table.setTable('student_list')
        self.table.select()
        try:
            selected
        except NameError:
            record = self.table.record(0)
        else:
            record = self.table.record(selected)

        # Populate the entries with data from the database
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
        elif record.value(7) == "Male":
            self.ui.radioMale.setChecked(True)
            self.ui.radioFemale.setChecked(False)
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

        # Record starts off locked
        self.ui.actionLock.setEnabled(False)
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

        # "Lock record" is greyed out until the record is locked
        self.ui.actionEdit.setEnabled(True)
        self.ui.actionLock.setEnabled(False)

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

        self.table.wRecord.setValue(
            8, self.ui.lineEdit_contactRelation.text())
        self.table.wRecord.setValue(
            9, self.ui.lineEdit_contactName.text())
        self.table.wRecord.setValue(
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

    def printStudents(self):
        # Placeholder for print function
        pass

    def exportPDF(self):
        pass

    def exportDocx(self):
        pass

    def assessBattele(self):
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


class Therapy():
    def __init__(self):
        super().__init__()
        # Placeholder until therapy section is generated
        pass


class NewReport(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = report.Ui_Form()
        self.ui.setupUi(self)


class Stats(QtWidgets.QMainWindow):
    def __init__(self):
        # Placeholder until UI for stats page is generated
        pass


class Guide(QtWidgets.QMainWindow):
    def __init__(self):
        # Placeholder until UI for guide page is generated
        pass


class About(QtWidgets.QMainWindow):
    def __init__(self):
        # Placeholder until UI for about page is generated
        pass


# Define QT5 app and launch login dialog
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    start = ViewStudents()
    start.show()
    app.exec_()
