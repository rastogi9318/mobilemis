from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
class UpdateBrand(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("updateBrand.ui",self)
        self.con =db.createconnection()
        self.cursor = self.con.cursor()
        self.populateCombo()
        self.cmbid.currentTextChanged.connect(self.fetchData)
        self.btnsubmit.clicked.connect(self.updateData)
    def populateCombo(self):                 # dropdown me value show karna
        strsql="select brandId from branddetails"
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        # print(self.dataset)
        for data in self.dataset:
            # print(data[0])
            self.cmbid.addItem(data[0])

    def fetchData(self):           # in  dropdown which email is selected its phone number show
        print("combo is clicked")
        self.brandId=self.cmbid.currentText()
        print(self.brandId)
        strsql = "select brandName from branddetails where brandId=%s"
        self.cursor.execute(strsql,(self.brandId,))
        self.data = self.cursor.fetchone()
        print(self.data[0])
        self.txtname.setText(self.data[0])
    def updateData(self):
        self.brandName = self.txtname.text()
        strupdate = "update branddetails set brandName=%s where brandId=%s"
        self.cursor.execute(strupdate,(self.brandName,self.brandId))
        self.con.commit()
        self.showDialog("Data Updated Successfully")


    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Updationdeails")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()






def main():
    app = QApplication(sys.argv)
    br = UpdateBrand()
    br.show()
    app.exec_()
if __name__=='__main__':main()
