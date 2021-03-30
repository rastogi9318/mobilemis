from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection as db


class Brand(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("demo.ui", self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.sbm.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.brandId = self.txtid.text()
        self.brandName = self.txtname.text()
        id = len(self.brandId.strip())
        nm = len(self.brandName.strip())
        if id == 0 or nm == 0:
            self.showDialog("You are not inserted the data")
        else:
            strinsert = "insert into demo(Id,Name)values(%s,%s)"
            self.cursor.execute(strinsert, (self.brandId, self.brandName))
            self.con.commit()
            self.txtid.setText("")
            self.txtname.setText("")
            self.showDialog("Data inserted Successfully")

    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Mobile Brand details")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    br = Brand()
    br.show()
    app.exec_()


if __name__ == '__main__':
    main()