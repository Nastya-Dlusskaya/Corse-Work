import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')
form_class, base_class = loadUiType('general.ui')

class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)

    def studentShow(self):


        pass




if __name__ == '__main__':
    form = MainWindow()
    form.setWindowTitle('Day - Book')
    form.show()
    sys.exit(app.exec_())
