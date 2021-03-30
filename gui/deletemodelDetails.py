from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection  as db
class DeleteModel(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("deletemodelDetails.ui",self)
        self.con=db.createconnection()
        self.cursor=self.con.cursor()
        self.btndelete.clicked.connect(self.deleteData)

    def deleteData(self):
        self.mnumber = self.txtnum.text()
        btnstatus = self.showDialog("Do you wish to Delete")
        if btnstatus==QMessageBox.Yes:
            print("deletion goes here")
            rowstatus = self.searchData(self.mnumber)
            if rowstatus>0:
                print("in if")
                strdelete="delete from modeldetails where modelNumber=%s"
                self.cursor.execute(strdelete,(self.mnumber,))
                self.con.commit()



            else:
                msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setWindowTitle("Deletion")
                msgbox.setText("Model Number does not Exist")
                msgbox.exec_()
    def searchData(self,mnumber):              # search data that primary key(email) is exist in database or not
        strsql = "select * from modeldetails where modelNumber=%s"
        print(mnumber)
        self.cursor.execute(strsql, (self.mnumber,))  # in where clause after column name comma is necessary
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
    dele = DeleteModel()
    dele.show()
    app.exec_()


if __name__ == '__main__':main()
