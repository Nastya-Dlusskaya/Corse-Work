import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from view.baseconnect.baseconnect import Base

app = QApplication(sys.argv)



class DateWork(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:\\course_work\\Work\\Corse-Work.git\\view\\date\\dateShow.ui", self)
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Date.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def btn_date(self):
        search = Base()
        search.makeListDate(self.addDate())
        self.close()

    def addDate(self):
        return  self.comboBox.currentText()


if __name__ == '__main__':
    form = DateWork()
    form.show()
    sys.exit(app.exec_())
