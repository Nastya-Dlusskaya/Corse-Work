import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from view.subject.subject_ui import Ui_Form

app = QApplication(sys.argv)
#form_class, base_class = loadUiType('subject.ui')


class Subject(QDialog):
    def __init__(self, *args):
        super(Subject, self).__init__(*args)

        Ui_Form()

form = Subject()
form.show()
sys.exit(app.exec_())
