import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic, QtSql, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableView
from PyQt5.QtSql import QSqlQuery

app = QApplication(sys.argv)

class Base(QWidget):

    def addPass(self, subject, date, student):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        con.open()
        s = "INSERT INTO my_base VALUES('" + str(subject) + "','" + str(date) + "','" + str(student)+ "')"
        QtSql.QSqlQuery().exec(s)
        con.close()

    def makeListStudent(self, student):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM my_base WHERE student = '" + student + "'")
        lst = []
        while query.next():
            stud = query.value('student')
            data = query.value('data')
            sub = query.value('sub')
            lst.append(str(stud) + " " + str(data) + " " + str(sub))
        self.table(lst)
        con.close()

    def makeListSubject(self, subject):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM my_base WHERE subject = '" + subject + "'")
        lst = []
        while query.next():
            sub = query.value('subject')
            data = query.value('data')
            stud = query.value('student')
            lst.append(stud + " " + data + " " + sub)
        self.table(lst)
        con.close()

    def table(self, lst):
        self.window = uic.loadUi('D:\\course_work\\Work\Corse-Work.git\\view\\baseconnect\\baseconnect.ui')
        if lst == []:
            self.window.textEdit.setText("None")
            print("none")
        for line in lst:
            self.window.textEdit.setText(line)
            print(line)
        self.window.show()




if __name__ == '__main__':
    form = Base()
    form.makeListSubject("ЭВМ")
    sys.exit(app.exec_())
