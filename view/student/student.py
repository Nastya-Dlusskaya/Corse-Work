import sys
import time
from os import path

ICON_DIR = path.dirname(__file__)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from view.baseconnect.baseconnect import Base

app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')


class Student(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("D:\\course_work\\Work\\Corse-Work.git\\view\\student\\mstudent.ui", self)
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Student.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def btn_student(self):
        self.search = Base()
        self.search.makeListStudent(self.addStudent())
        self.close()

    def addStudent(self):
        return  self.comboBox.currentText()



if __name__ == '__main__':
    form = Student()
    form.setWindowTitle('Corse-Work.git')
    form.show()
    sys.exit(app.exec_())
