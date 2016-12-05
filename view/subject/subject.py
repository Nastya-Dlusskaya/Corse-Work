import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from view.baseconnect.baseconnect import Base


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
        self.base = Base()
        self.base.makeListSubject(self.addSubject())
        self.close()


    def chooseSubject(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addSubject/Subject.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def addSubject(self):
        return self.comboBox.currentText()


if __name__ == '__main__':
    form = Subject()
    form.show()
    sys.exit(app.exec_())








