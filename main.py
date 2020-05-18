# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F
# Username and password are both "admin"

hours = 7

import sys
from PyQt5 import QtCore, QtWidgets
import login, landing, student_entry, view_students, report

# Define QT5 app

app = QtWidgets.QApplication(sys.argv)

# Define login dialogue

class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        
        # Check if username/password combo is correct, if it is open landing page
        if (self.exec_() == QtWidgets.QDialog.Accepted and self.ui.usernameLine.text() == 'admin' and self.ui.passwordLine.text() == 'admin'):
            self.close()
        else:
            warn = QtWidgets.QMessageBox()
            warn.setIcon(QtWidgets.QMessageBox.Warning)
            warn.setText(
               "Username and password combination is incorrect, try again")
            warn.setStandardButtons(
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            warn.exec()
            self.ui.setupUi(self)
            self.show()
            
class Landing(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = landing.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show
    
# Display login dialog
window = Login()
window.show



sys.exit(app.exec_())
