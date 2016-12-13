import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

from view.baseconnect.baseconnect import Base
app = QApplication(sys.argv)

class Passes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('D:\\course_work\\Work\\Corse-Work.git\\view\\addpass\\pass.ui', self)
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Student.txt", "r")
        for line in f:
            self.comboBox_2.addItem(line)
        f.close()
        f = open(r"/course_work/Work/Corse-Work.git/view/addSubject/Subject.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def addPass(self):
        self.base = Base()
        self.date = self.addDate()
        self.student = self.addStudent()
        self.subject = self.addSubject()
        self.base.addPass(self.subject, self.date, self.student)
        self.close()

    def addStudent(self):
        return self.comboBox.currentText()

    def addSubject(self):
         return self.comboBox_2.currentText()

    def addDate(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/date/Date.txt", "a")
        f.writelines(self.dateEdit.date().toString("yyyy.MM.dd"))
        f.write("\n")
        f.close()
        return self.dateEdit.date().toString("yyyy.MM.dd")


if __name__ == '__main__':
    form = Passes()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
