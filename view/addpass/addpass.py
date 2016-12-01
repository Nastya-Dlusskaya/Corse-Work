import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

app = QApplication(sys.argv)

class Pass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('D:\\course_work\\Work\\Corse-Work.git\\view\\addpass\\pass.ui', self)
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Student.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()
        f = open(r"/course_work/Work/Corse-Work.git/view/addSubject/Subject.txt", "r")
        for line in f:
            self.comboBox_2.addItem(line)
        f.close()


    def addPass(self):
        pass

    def addStudent(self):
        return self.comboBox.currentText()

    def addSubject(self):
         return self.comboBox_2.currentText()

    def addDate(self):
        return self.dateEdit.date()

if __name__ == '__main__':
    form = Pass()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
