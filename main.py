# ---------------------------------------------------------- #
# ----- Early Intervention Student Management Database ----- #
# ----------- Created by Red&Black Technical  -------------- #
# ---------------------------------------------------------- #

# Export as pyinstaller main.py -F

hours = 4

import sys, sqlite3
import login, landing, student_entry, view_students, report

# Display login dialogue
login.play()

