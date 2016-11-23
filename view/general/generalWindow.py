import sys

from view.student.student import Student
from view.subject.subject import Subject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
form_class, base_class = loadUiType('general.ui')



class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Day Book")
        self.setWindowIcon(QIcon("images.png"))

    def btnclickstudent(self):
        form_class = loadUiType(QDialog,'mstudent.ui')
        self.Student(QDialog, form_class)

    def btnclicksubject(self):
        form_class = loadUiType(QDialog, 'subject.ui')
        self.Subject(QDialog, form_class)


MainWindow()


