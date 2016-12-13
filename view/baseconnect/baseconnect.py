import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtSql
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


app = QApplication(sys.argv)


class Base(QWidget):

    def addPass(self, subject, date, student):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        s = "INSERT INTO group10701215 VALUES('" + str(student) + "','" + str(date) + "','" + str(subject)+ "')"
        QtSql.QSqlQuery().exec(s)
        con.close()

    def makeListStudent(self, student):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM group10701215 WHERE student = '" + str(student) + "'")
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
        print(subject)
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM group10701215 WHERE subject ='" + subject + "'")
        lst = []
        while query.next():
             line = []
             line.append(query.value('student'))
             line.append(query.value('data'))
             line.append(query.value('subject'))
             lst.append(line)
        self.table(lst)
        con.close()

    def makeListDate(self, dates):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        query = QtSql.QSqlQuery("SELECT * FROM group10701215 WHERE data = '" + dates + "'")
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

    def deleteStudent(self, student):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        query = QtSql.QSqlQuery("DELETE FROM group10701215 WHERE student = '" + student + "'")
        con.close()

    def deleteSubject(self, subject):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Student_list.db')
        con.open()
        query = QtSql.QSqlQuery("DELETE FROM group10701215 WHERE subject = '" + subject + "'")
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
    form.makeListSubject('ЭВМ')
    sys.exit(app.exec_())
