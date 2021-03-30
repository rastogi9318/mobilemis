from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
from gui.counsellordash_1 import BCounsellorDash
from gui.counsellordash_2 import MCounsellorDash
from gui.counsellordash_3 import SCounsellorDash
import sys
class CounsellorDash(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Counsellordash.ui",self)
        self.actionBrand_Dash.triggered.connect(lambda:self.loadFrame(self.actionBrand_Dash))
        self.actionModel_Dash.triggered.connect(lambda: self.loadFrame(self.actionModel_Dash))
        self.actionSales_Dash.triggered.connect(lambda: self.loadFrame(self.actionSales_Dash))


    def loadFrame(self,menuitem):
        caption=menuitem.text()
        if caption == "Brand Dash":
            self.mobile = BCounsellorDash()
            self.mobile.show()
        if caption == "Model Dash":
            self.mobile = MCounsellorDash()
            self.mobile.show()
        if caption == "Sales Dash":
            self.mobile = SCounsellorDash()
            self.mobile.show()
        print("hello")

def main():
    app=QApplication(sys.argv)
    counsellor=CounsellorDash()
    counsellor.show()
    app.exec_()
if __name__=='__main__':main()