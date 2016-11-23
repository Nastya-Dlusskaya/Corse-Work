import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from base.Connecting import Connect

app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')
form_class, base_class = loadUiType('baseconnect.ui')


class Base(QDialog, form_class):
    def __init__(self, *args):
        super(Base, self).__init__(*args)

        self.setupUi(self)
        self.load()

    def load(self):
        Connect()



if __name__ == '__main__':
    form = Base()
    form.setWindowTitle('Corse-Work.git')
    form.show()
    sys.exit(app.exec_())
