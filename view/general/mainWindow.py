import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QSplashScreen
from PyQt5 import uic
from view.student.student import Student
from view.subject.subject import Subject
from view.addpass.addpass import Pass
from view.addStudent.addStud import AddStud
from view.addSubject.addSub import AddSub


app = QApplication(sys.argv)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:\\course_work\\Work\\Corse-Work.git\\view\\general\\general.ui", self)
        self.window = None

    def subjectShow(self):
        self.window = Subject()


    def studentShow(self):
        self.window = Student()

    def addPass(self):
        self.window = Pass()

    def AddStudent(self):
        self.window = AddStud()

    def AddSubject(self):
        self.window = AddSub()










if __name__ == '__main__':
    form = MainWindow()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
