from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection as db
class ModelDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("modelDetails.ui", self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.modelNumber = self.txtmodel.text()
        self.brandId = self.txtid.text()
        self.modelName = self.txtname.text()
        self.price = self.txtprice.text()
        self.Features = self.txtfeatures.text()
        self.Quantity = self.txtquan.text()
        no = len(self.modelNumber.strip())
        id = len(self.brandId.strip())
        nm = len(self.modelName.strip())
        pr = len(self.price.strip())
        fe = len(self.Features.strip())
        qu = len(self.Quantity.strip())

        if no == 0 or id == 0 or nm == 0 or pr == 0 or fe == 0 or qu == 0:
            self.showDialog("You are in wrong way")
        else:
            strinsert = " insert into modeldetails(modelNumber,brandId,modelName,price,Features,Quantity)values(%s,%s,%s,%s,%s,%s) "
            self.cursor.execute(strinsert, (self.modelNumber, self.brandId, self.modelName, float(self.price), self.Features, int(self.Quantity)))
            self.con.commit()
            self.txtmodel.setText("")
            self.txtid.setText("")
            self.txtname.setText("")
            self.txtprice.setText("")
            self.txtfeatures.setText("")
            self.txtquan.setText("")
            self.showDialog("data inserted successfully")
    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Model Details")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()
def main():
    app = QApplication(sys.argv)
    md = ModelDetails()
    md.show()
    app.exec_()


if __name__ == '__main__':
    main()
