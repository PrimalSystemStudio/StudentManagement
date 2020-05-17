# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F

hours = 7

import sys
from PyQt5 import QtCore, QtWidgets
import login, landing, student_entry, view_students, report

# Define QT5 app

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()


# Display login dialogue

logger = login.Login()
logger.setupUi(dialog)
dialog.show()



lander = landing.Ui_MainWindow()
lander.setupUi(mainWindow)
# mainWindow.show()

sys.exit(app.exec_())
