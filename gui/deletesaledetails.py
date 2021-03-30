from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection  as db
class DeleteSale(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("deletesaledetails.ui",self)
        self.con=db.createconnection()
        self.cursor=self.con.cursor()
        self.btndelete.clicked.connect(self.deleteData)

    def deleteData(self):
        self.id = self.txtid.text()
        btnstatus = self.showDialog("Do you wish to Delete")
        if btnstatus==QMessageBox.Yes:
            print("deletion goes here")
            rowstatus = self.searchData(self.id)
            if rowstatus>0:
                print("in if")
                strdelete="delete from saledetails where transactionId=%s"
                self.cursor.execute(strdelete,(self.id,))
                self.con.commit()
                self.showDialog("Data deleted Successfully")




            else:
                msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setWindowTitle("Deletion")
                msgbox.setText("Id does not Exist")
                msgbox.exec_()
    def searchData(self,id):              # search data that primary key(email) is exist in database or not
        strsql = "select * from saledetails where transactionId=%s"
        print(id)
        self.cursor.execute(strsql, (self.id,))  # in where clause after column name comma is necessary
        self.rowdata = self.cursor.fetchone()     # return tuple

        rowstatus = self.cursor.rowcount   # positive vlaue of rowdata means data is already exist
        print(rowstatus)
        return rowstatus
    def showDialog(self,msg):           # show inserted data dialog box insertion successfully
        msgbox=QMessageBox()            # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setWindowTitle("Deletion")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        btnstatus = msgbox.exec_()
        return btnstatus
    def showMessage(self,msg):
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setStandardButton(QMessageBox.Ok)
        msgbox.setWindowTitle("Deletion")
        msgbox.setText(msg)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    dele = DeleteSale()
    dele.show()
    app.exec_()


if __name__ == '__main__':main()
