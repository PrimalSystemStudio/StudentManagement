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
from PyQt5 import QtWidgets

hours = 8


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
                main_Ui = Landing()
                main_Ui.__init__()
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
            print("quit")
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
        self.show()

# Define QT5 app and launch login dialog
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login()
    app.exec_()
