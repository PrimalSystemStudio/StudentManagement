# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F
# Username and password are both "admin"
import sys
import sqlite3
import login
import landing
import student_entry
import view_students
import report
from PyQt5 import QtCore, QtWidgets, QtSql

# How many hours been spent on this project (for personal use)
hours = 23


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
        print("browse button pressed")

    def guide(self):
        print("guide button pressed")

    def register(self):
        self.newstudent = NewStudent()
        self.newstudent.show()
        print("guide button pressed")

    def report(self):
        self.newreport = NewReport()
        self.newreport.show()
        print("report button pressed")

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
        self.data.table = QtSql.QSqlTableModel()
        self.data.table.setTable('student_list')
        self.data.table.select()

        # Database headers
        self.data.table.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.data.table.setHeaderData(1, QtCore.Qt.Horizontal, "Given Names")
        self.data.table.setHeaderData(2, QtCore.Qt.Horizontal, "Family Name")
        self.data.table.setHeaderData(3, QtCore.Qt.Horizontal, "Date of Birth")
        self.data.table.setHeaderData(4, QtCore.Qt.Horizontal, "Birth Place")
        self.data.table.setHeaderData(5, QtCore.Qt.Horizontal, "Hospital Diagnosis")
        self.data.table.setHeaderData(7, QtCore.Qt.Horizontal, "Nationality")
        self.data.table.setHeaderData(8, QtCore.Qt.Horizontal, "Gender")
        self.data.table.setHeaderData(9, QtCore.Qt.Horizontal, "Primary Caregiver")
        self.data.table.setHeaderData(10, QtCore.Qt.Horizontal, "Contact Name")
        self.data.table.setHeaderData(11, QtCore.Qt.Horizontal, "Contact Mobile")

        # Show the data in the table
        self.ui.tableView.setModel(self.data.table)
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


# Window for inputing data for a new student
class NewStudent(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = student_entry.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Record starts off editable
        # "Edit record" is greyed out until the record is locked
        self.ui.actionEdit.setEnabled(False)
        
        # Define the database
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("documents/students.db")
        self.data.open()
        self.data.table = QtSql.QSqlTableModel()
        self.data.table.setTable('student_list')
        self.data.table.select()

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
            self.data.table.last_id = QtSql.QSqlQuery("SELECT MAX(ID) FROM student_list")
            self.data.table.last_id.last()

            # Get info entered and put into a new record
            self.data.table.newRecord = self.data.table.primaryValues(0)
            self.data.table.newRecord.setValue(0, self.data.table.last_id.value(0) + 1)
            self.data.table.newRecord.setValue(
                1, self.ui.lineEdit_name1.text() +
                " " + self.ui.lineEdit_name2.text() +
                " " + self.ui.lineEdit_name3.text())
            self.data.table.newRecord.setValue(2, self.ui.lineEdit_family.text())
            self.birthdate = self.ui.dateBirth.dateTime()
            self.data.table.newRecord.setValue(3,
                self.ui.dateBirth.textFromDateTime(self.birthdate))
            self.data.table.newRecord.setValue(4, self.ui.lineEdit_birthplace.text())
            self.data.table.newRecord.setValue(5, self.ui.lineEdit_diagnosis.text())
            self.data.table.newRecord.setValue(6, self.ui.lineEdit_nationality.text())

            if self.ui.radioFemale.isChecked():
                self.data.table.newRecord.setValue(7, "Female")
            elif self.ui.radioMale.isChecked():
                self.data.table.newRecord.setValue(7, "Male")

            self.data.table.newRecord.setValue(8, self.ui.lineEdit_contactRelation.text())
            self.data.table.newRecord.setValue(9, self.ui.lineEdit_contactName.text())
            self.data.table.newRecord.setValue(10, self.ui.lineEdit_contactMobile.text())
            
            # Insert new record into the table
            self.data.table.insertRecord(-1, self.data.table.newRecord)
            self.hide()

    def editRecord(self):
        # Allows text to be edited
        if self.ui.actionEdit.isEnabled() == True:
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
        if self.ui.actionLock.isEnabled() == True:
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
        
        # Define the database
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("documents/students.db")
        self.data.open()
        
        # Record starts off locked
        # "Lock record" is greyed out until the record is locked
        self.ui.actionLock.setEnabled(False)
        
    def saveRecord(self):
        # Placeholder to save record
        pass

    def editRecord(self):
        # Allows text to be edited
        if self.ui.actionEdit.isEnabled() == True:
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
        if self.ui.actionLock.isEnabled() == True:
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
        
    def assessSpeech():
        # Placeholder for speech assessment
        pass


class Battele():
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
        # Placeholder until UI for stats page is generated
        pass


# Define QT5 app and launch login dialog
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    start = ViewStudents()
    start.show()
    app.exec_()
