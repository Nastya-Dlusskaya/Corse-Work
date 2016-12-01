import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from view.student.student import Student


app = QApplication(sys.argv)

class Subject(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("D:\\course_work\\Work\\Corse-Work.git\\view\\subject\\subject.ui", self)
        self.show()

    def subject_table(self):
        st = Student()


    def createnew(self):
        pass






#form = Subject()
#form.show()
#sys.exit(app.exec_())
