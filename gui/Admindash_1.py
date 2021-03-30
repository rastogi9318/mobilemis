from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
from gui.Admindash import AdminDash2
from gui.Admindetails import AdminDetails

class AdminDash1(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Admindash_1.ui",self)
        self.actionAccount.triggered.connect(lambda:self.loadFrame(self.actionAccount))
        self.actionDetails.triggered.connect(lambda: self.loadFrame(self.actionDetails))

    def loadFrame(self, menuitem):
        caption = menuitem.text()
        if caption == "Accounts":
            self.enquiry = AdminDash2()
            self.enquiry.show()
        if caption == "Details":
            self.enquiry = AdminDetails()
            self.enquiry.show()

def main():
   app = QApplication(sys.argv)
   admin = AdminDash1()
   admin.show()
   app.exec_()


if __name__ == '__main__':

    main()