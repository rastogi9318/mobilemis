from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
class UpdateAccount(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("updateaccount.ui",self)
        self.con =db.createconnection()
        self.cursor = self.con.cursor()
        self.populateCombo()
        self.cmb.currentTextChanged.connect(self.fetchData)

        self.btnsubmit.clicked.connect(self.updateData)


    def populateCombo(self):
        # dropdown me value show karna
        strsql="select UserId from logindetails"
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        # print(self.dataset)
        for data in self.dataset:
            # print(data[0])
            self.cmb.addItem(data[0])



    def fetchData(self):
        # in  dropdown which email is selected its phone number show
        print("combo is clicked")
        self.UserId=self.cmb.currentText()
        print(self.UserId)
        strsql = "select Password from logindetails where UserId=%s"
        self.cursor.execute(strsql,(self.UserId,))
        self.data = self.cursor.fetchone()
        print(self.data[0])
        self.txtpass.setText(self.data[0])



    def updateData(self):
        self.pr = self.txtpass.text()
        print(self.pr)
        strupdate = "update logindetails set Password=%s where UserId=%s"
        self.cursor.execute(strupdate,(self.pr,self.UserId))
        self.con.commit()
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
    Up = UpdateAccount()
    Up.show()
    app.exec_()


if __name__ == '__main__':
    main()
