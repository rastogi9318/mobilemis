from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
import sys
from gui.createaccount import CreateAccount
from gui.updateaccount import UpdateAccount

class AdminDash2(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Admindash.ui",self)
        self.actionCreate.triggered.connect(lambda:self.loadFrame(self.actionCreate))
        self.actionUpdate.triggered.connect(lambda: self.loadFrame(self.actionUpdate))

    def loadFrame(self, menuitem):
        caption = menuitem.text()
        if caption == "Create":
            self.enquiry = CreateAccount()
            self.enquiry.show()
        if caption == "Update":
            self.enquiry = UpdateAccount()
            self.enquiry.show()

def main():
   app = QApplication(sys.argv)
   admin = AdminDash2()
   admin.show()
   app.exec_()
if __name__ == '__main__': main()