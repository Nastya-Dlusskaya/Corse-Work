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
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addSubject/Subject.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def subject_table(self):
        pass

    def chooseSubject(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addSubject/Subject.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def addStart(self):
        return self.dateEdit_2.date()

    def addEnd(self):
        return self.dateEdit.date()









