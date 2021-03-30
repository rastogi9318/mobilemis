from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection as db
from gui.Counsellordash import CounsellorDash
from gui.Admindash_1 import AdminDash1


class Login(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("login.ui",self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.checkLogin)
    def checkLogin(self):
        self.uid=self.txtuser.text()
        self.upass=self.txtpass.text()
        strsql="select * from logindetails where UserId=%s and Password=%s"
        self.cursor.execute(strsql,(self.uid,self.upass,))
        self.data = self.cursor.fetchone()
        self.status = self.cursor.rowcount
        print(self.status)
        id = len(self.uid.strip())
        ps = len(self.upass.strip())
        if id == 0 or ps == 0:
            print("you are in wrong way")
        elif self.status > 0:
            print("Id exist")
            self.type = self.data[2]
            print(self.type)

            if self.type == "Console":
                self.cn = CounsellorDash()
                self.cn.show()
                self.close()
            if self.type == "Admin":
                self.cn = AdminDash1()
                self.cn.show()
                self.close()

        else:
            self.showDialog("Id Does not Exist")

    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Updation details")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()


def main():
    app=QApplication(sys.argv)
    lg=Login()
    lg.show()
    app.exec_()
if __name__=='__main__':main()