import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

app = QApplication(sys.argv)

class Pass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('D:\\course_work\\Work\\Corse-Work.git\\view\\addpass\\pass.ui')
        self.show()


if __name__ == '__main__':
    form = Pass()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
