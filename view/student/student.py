import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType



app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')
form_class, base_class = loadUiType('mstudent.ui')


class Student(QDialog, form_class):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        #uic.loadUi("mstudent.ui", self)



    def btn_student(self):
        pass

    def addEndPeriod(self):
        pass

    def addStartPeriod(self):
        pass

    def addStudent(self):
        pass


if __name__ == '__main__':
    form = Student()
    form.setWindowTitle('Corse-Work.git')
    form.show()
    sys.exit(app.exec_())
