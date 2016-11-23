import sqlite3

class Connect:

    def __init__(self):
        self.connect()

    def connect(self):
        con = sqlite3.connect("Test2.db")
        cur = con.cursor()






