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

hours = 12


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
                print("success")
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
        self.data.exec_("SELECT *")
        self.data.lastError()
        self.model = QtSql.QSqlQueryModel()
        self.model.setQuery("SELECT *")
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Given Names")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Family Name")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Date of Birth")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Birth Place")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Hospital Diagnosis")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Hospital Name")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Nationality")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Gender")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Primary Caregiver")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Date of Admission")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal, "Emergency Contact Name")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "Emergency Contact Mobile")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal, "Emergency Contact Home")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal, "Emergency Contact Office")
        self.model.setHeaderData(16, QtCore.Qt.Horizontal, "Relation To Student")

        #Show the data in the table
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.show()

# Window for inputting data for a new student
class NewStudent(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = student_entry.Ui_MainWindow()
        self.ui.setupUi(self)


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
