import sys

from view.student.student import Student
from view.subject.subject import Subject
from view.general.general_ui import Ui_Form
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
#form_class, base_class = loadUiType('general.ui')



class MainWindow(QDialog):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        Ui_Form.setupUi()


    def btnclickstudent(self):
        Student.setupUi()

    def btnclicksubject(self):
        Subject.setupUi()




