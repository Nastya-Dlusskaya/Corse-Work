import sys


from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from view.baseconnect.baseconnect import Base


app = QApplication(sys.argv)

class delStudent(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('D:\\course_work\\Work\\Corse-Work.git\\view\\delStudent\\delStudent.ui', self)
        self.loading()
        self.show()

    def loading(self):
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Student.txt", "r")
        for line in f:
            self.comboBox.addItem(line)
        f.close()

    def getting(self):
        base = Base()
        base.deleteStudent(self.comboBox.currentText())
        self.comboBox.removeItem(self.comboBox.currentIndex())
        f = open(r"/course_work/Work/Corse-Work.git/view/addStudent/Student.txt", "w")
        for i in range(self.comboBox.count()):
            f.write(self.comboBox.itemText(i))
        f.close()
        self.close()




if __name__ == '__main__':
    form = delStudent()
    form.show()
    sys.exit(app.exec_())
