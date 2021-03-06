from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
class UpdateModelDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("updatemodelDetails.ui",self)
        self.con =db.createconnection()
        self.cursor = self.con.cursor()
        self.populateCombo()
        self.cmb.currentTextChanged.connect(self.fetchData)

        self.btnsubmit.clicked.connect(self.updateData)


    def populateCombo(self):
        # dropdown me value show karna
        strsql="select modelNumber from modeldetails"
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        # print(self.dataset)
        for data in self.dataset:
            # print(data[0])
            self.cmb.addItem(data[0])



    def fetchData(self):
        # in  dropdown which email is selected its phone number show
        print("combo is clicked")
        self.modelNumber=self.cmb.currentText()
        print(self.modelNumber)
        strsql = "select price from modeldetails where modelNumber=%s"
        self.cursor.execute(strsql,(self.modelNumber,))
        self.data = self.cursor.fetchone()
        print(self.data[0])
        self.price.setText(str(self.data[0]))



    def updateData(self):
        self.pr = self.price.text()
        print(self.pr)
        strupdate = "update modeldetails set price=%s where modelNumber=%s"
        self.cursor.execute(strupdate,(int(self.pr),self.modelNumber))
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
    Up = UpdateModelDetails()
    Up.show()
    app.exec_()


if __name__ == '__main__':
    main()
