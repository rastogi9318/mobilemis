from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
from gui.brand import Brand
from gui.updateBrand import UpdateBrand
from gui.deletebrand import DeleteBrand
import sys
class BCounsellorDash(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("counsellordash_1.ui",self)
        self.actionAdd.triggered.connect(lambda:self.loadFrame(self.actionAdd))
        self.actionUpdate.triggered.connect(lambda: self.loadFrame(self.actionUpdate))
        self.actionDelete.triggered.connect(lambda: self.loadFrame(self.actionDelete))


    def loadFrame(self,menuitem):
        caption=menuitem.text()
        if caption == "Add":
            self.brand = Brand()
            self.brand.show()
        if caption == "Update":
            self.brand = UpdateBrand()
            self.brand.show()
        if caption == "Delete":
            self.brand = DeleteBrand()
            self.brand.show()
        print("hello")

def main():
    app=QApplication(sys.argv)
    counsellor=BCounsellorDash()
    counsellor.show()
    app.exec_()
if __name__=='__main__':main()