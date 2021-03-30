from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection as db
class CreateAccount(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("createaccount.ui",self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.userid = self.txtid.text()
        self.userpass = self.txtpass.text()
        self.usertype = self.cmb.currentText()
        print(self.usertype)
        id = len(self.userid.strip())  # strip is used in string function for remove the starting and ending space
        ps = len(self.userpass.strip())
        #ty = len(self.usertype.strip())
        if id == 0 or ps == 0:
            print("data required in all fields")
        else:
            strinsert = "insert into logindetails(UserId,Password, Usertype)values(%s,%s,%s)"
            self.cursor.execute(strinsert, (self.userid, self.userpass, self.usertype))
            self.con.commit()
            self.txtid.setText("")
            self.txtpass.setText("")
           # self.cmb.setText("")
            self.showDialog("Data Updated Successfully")

    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Updation details")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()

def main():
    app = QApplication(sys.argv)
    cr = CreateAccount()
    cr.show()
    app.exec_()
if __name__=='__main__':main()