import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from view.student.student import Student
from view.subject.subject import Subject
from view.addpass.addpass import Passes
from view.addStudent.addStud import AddStud
from view.addSubject.addSub import AddSub
from view.date.Date import DateWork
from view.baseconnect.baseconnect import Base
from view.delSubject.deleteSubject import delSubject
from view.delStudent.deleteStudent import delStudent

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
        self.window = Passes()

    def AddStudent(self):
        self.window = AddStud()

    def AddSubject(self):
        self.window = AddSub()

    def deleteStudent(self):
        self.window = delStudent()

    def deleteSubject(self):
        self.window = delSubject()

    def dateShow(self):
        self.window = DateWork()











if __name__ == '__main__':
    form = MainWindow()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
