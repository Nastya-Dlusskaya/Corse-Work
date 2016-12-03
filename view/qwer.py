from PyQt5 import QtCore, QtWidgets,QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSqlTableModel")
con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("D:\\course_work\\Work\\Corse-Work.git\\view\\baseconnect\\Test2.db")
con.open()
stm = QtSql.QSqlTableModel(parent = window)
stm.setTable('timetable')
stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.select()
stm.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
stm.setHeaderData(2, QtCore.Qt.Horizontal, "Count")
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Add")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Delete")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(300, 250)
window.show()
sys.exit(app.exec_())

