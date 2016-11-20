import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('Corse-Work.git')
form_class, base_class = loadUiType('subject.ui')


class Subject(QDialog, form_class):
    def __init__(self, *args):
        super(Subject, self).__init__(*args)

        self.setupUi(self)


if __name__ == '__main__':
    form = Subject()
    form.setWindowTitle('Corse-Work.git')
    form.show()
    sys.exit(app.exec_())