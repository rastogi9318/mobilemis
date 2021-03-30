from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection  as db
class ModelTable(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Modeltable.ui", self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.fillTable()
    def fillTable(self):
        strsql = " select * from modeldetails "
        self.cursor.execute(strsql)
        self.dataset=self.cursor.fetchall()
        print(self.dataset)
        rowcnt = len(self.dataset)
        print(rowcnt)
        self.tbl.setRowCount(rowcnt)
        rownum = 0
        for row in self.dataset:
            for column in range(len(row)):
                print(row[column])
                self.tbl.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1
def main():
    app = QApplication(sys.argv)
    enq = ModelTable()
    enq.show()
    app.exec_()


if __name__ == '__main__':
    main()
