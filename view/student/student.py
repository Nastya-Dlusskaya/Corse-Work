import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QIcon
from view.student.mstudent_ui import Ui_Form

app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')
#form_class, base_class = loadUiType('mstudent.ui')


class Student(QDialog):
    def __init__(self, *args):
        super(Student, self).__init__(*args)

        Ui_Form.setupUi()


    def btn_student(self):
        print(1)


if __name__ == "main":
    form = Student()
    form.show()
    sys.exit(app.exec_())
