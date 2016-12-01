import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')


class Student(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("D:\\course_work\\Work\\Corse-Work.git\\view\\student\\mstudent.ui", self)
        self.loading()
        self.show()

    def loading(self):
        f = open("D:\\course_work\\Work\\Corce-Work.git\\view\\addStudent\\Student.txt", "r")
        for line in f:
            self.ComboBox.addItems(line)
        f.close()

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
