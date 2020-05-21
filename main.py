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
from PyQt5 import QtWidgets, QtSql

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

class ViewStudents(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = view_students.Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE", "documents/students.db")
        self.data.open()


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
