import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
app = QApplication(sys.argv)

class Subject(QDialog):
    def __init__(self, *args):
        super().__init__()

        uic.loadUi("subject.ui", self)

    def subject_table(self):
        pass

    def createnew(self):
        pass



form = Subject()
form.show()
sys.exit(app.exec_())
