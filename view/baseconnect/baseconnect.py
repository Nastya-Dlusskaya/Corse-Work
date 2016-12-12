import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtSql
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


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
            line = []
            sub = query.value('subject')
            data = query.value('data')
            stud = query.value('student')
            line.append(stud)
            line.append(data)
            line.append(sub)
            lst.append(line)
        self.table(lst)
        con.close()

    def makeListSubject(self, subject):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM my_base WHERE subject = '" + subject + "'")
        lst = []
        while query.next():
            line = []
            sub = query.value('subject')
            data = query.value('data')
            stud = query.value('student')
            line.append(stud)
            line.append(data)
            line.append(sub)
            lst.append(line)
        self.table(lst)
        con.close()

    def makeListDate(self, date):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM my_base WHERE data = '" + date + "'")
        lst = []
        while query.next():
            line = []
            sub = query.value('subject')
            data = query.value('data')
            stud = query.value('student')
            line.append(stud)
            line.append(data)
            line.append(sub)
            lst.append(line)
        self.table(lst)
        con.close()

    def table(self, lst):
        self.window = uic.loadUi('D:\\course_work\\Work\Corse-Work.git\\view\\baseconnect\\baseconnect.ui')
        self.window.tableWidget.clear()
        self.window.tableWidget.setColumnCount(3)
        self.window.tableWidget.setRowCount(len(lst))
        for i in range(len(lst)):
            line  = lst[i]
            for j in range(len(line)):
                self.window.tableWidget.setItem(i, j, QTableWidgetItem(line[j]))
        self.window.show()




if __name__ == '__main__':
    form = Base()
    form.makeListSubject()
    sys.exit(app.exec_())
