from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
from gui.sales import Sales
from gui.deletesaledetails import DeleteSale
import sys
class SCounsellorDash(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("counsellordash_3.ui",self)
        self.actionAdd.triggered.connect(lambda:self.loadFrame(self.actionAdd))
        self.actionDelete.triggered.connect(lambda: self.loadFrame(self.actionDelete))


    def loadFrame(self,menuitem):
        caption=menuitem.text()
        if caption == "Add":
            self.model = Sales()
            self.model.show()
        if caption == "Delete":
            self.model = DeleteSale()
            self.model.show()

def main():
    app=QApplication(sys.argv)
    counsellor=SCounsellorDash()
    counsellor.show()
    app.exec_()
if __name__=='__main__':main()