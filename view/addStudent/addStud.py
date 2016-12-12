import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

app = QApplication(sys.argv)

class AddStud(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('D:\\course_work\\Work\\Corse-Work.git\\view\\addStudent\\aStud.ui', self)
        self.show()

    def gettexting(self):
        self.f = open("D:\\course_work\\Work\\Corse-Work.git\\view\\addStudent\\Student.txt", "a")
        self.f.writelines(self.lineEdit.text() + "\n")
        self.f.close()
        self.close()


if __name__ == '__main__':
    form = AddStud()
    form.show()
    sys.exit(app.exec_())
