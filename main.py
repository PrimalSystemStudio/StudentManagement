# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F

hours = 3

import sys, sqlite3
import login, landing, student_entry, view_students, report
import PyQt5

# Display login dialogue
login.play()

