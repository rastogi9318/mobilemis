from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
from gui.Branddetails import BrandDetails
from gui.Modeltable import ModelTable
from gui.saletable import SaleTable
from gui.logindetails import LoginDetails

class AdminDetails(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Admindetails.ui",self)
        self.actionBrand_Details.triggered.connect(lambda:self.loadFrame(self.actionBrand_Details))
        self.actionModel_Details.triggered.connect(lambda: self.loadFrame(self.actionModel_Details))
        self.actionSale_Details.triggered.connect(lambda: self.loadFrame(self.actionSale_Details))
        self.actionLogIn_Details.triggered.connect(lambda: self.loadFrame(self.actionLogIn_Details))

    def loadFrame(self, menuitem):
        caption = menuitem.text()
        if caption == "Brand Details":
            self.enquiry = BrandDetails()
            self.enquiry.show()
        if caption == "Model Details":
            self.enquiry = ModelTable()
            self.enquiry.show()
        if caption == "Sale Details":
            self.enquiry = SaleTable()
            self.enquiry.show()
        if caption == "LogIn Details":
            self.enquiry = LoginDetails()
            self.enquiry.show()

def main():
   app = QApplication(sys.argv)
   admin = AdminDetails()
   admin.show()
   app.exec_()
if __name__ == '__main__': main()