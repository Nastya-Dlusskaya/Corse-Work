import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic, QtSql
from PyQt5.QSqlRecord import *
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)

class Base(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("baseconnect.ui", self)
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE3')
        self.con.setDatabaseName('Test2.bd')
        self.con.open()
        self.choose_table()
        self.counts()

    def choose_table(self):
        print(self.con.tables())

    def counts(self):

        print(self.count())


    def student_question(self):
        self.query = QtSql.QSqlQuery()
        self.query.prepare("")

if __name__ == '__main__':
    form = Base()
    form.show()
    sys.exit(app.exec_())
