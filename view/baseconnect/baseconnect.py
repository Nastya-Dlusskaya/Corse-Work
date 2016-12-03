import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic, QtSql
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlQuery

app = QApplication(sys.argv)

class Base(QWidget):
    def __init__(self):
        super().__init__()
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE3')
        self.con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        self.con.open()


    def student_question(self):
        self.query = QtSql.QSqlQuery()
        self.query.prepare("")

    def addPass(self, subject = "qwer", date = 12.03, student = "wertyui"):
        self.query = QtSql.QSqlQuery()
        self.query.prepare("Insert INTO table_name VALUES(?, ?, ?)")
        self.query.addBindValue(subject)
        self.query.addBindValue(date)
        self.query.addBindValue(student)
        self.con.commit()
        self.con.close()


if __name__ == '__main__':
    form = Base()
    form.addPass()
    sys.exit(app.exec_())
