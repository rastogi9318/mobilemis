from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
from databaseinfo.dbconnection import DbConnection as db
from gui.modelDetails import ModelDetails
from gui.updatemodelDetails import UpdateModelDetails
from gui.deletemodelDetails import DeleteModel
import sys
class MCounsellorDash(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("counsellordash_2.ui",self)
        self.actionAdd.triggered.connect(lambda:self.loadFrame(self.actionAdd))
        self.actionUpdate.triggered.connect(lambda: self.loadFrame(self.actionUpdate))
        self.actionDelete.triggered.connect(lambda: self.loadFrame(self.actionDelete))


    def loadFrame(self,menuitem):
        caption=menuitem.text()
        if caption == "Add":
            self.model = ModelDetails()
            self.model.show()
        if caption == "Update":
            self.model = UpdateModelDetails()
            self.model.show()
        if caption == "Delete":
            self.model = DeleteModel()
            self.model.show()
        print("hello")

def main():
    app=QApplication(sys.argv)
    counsellor=MCounsellorDash()
    counsellor.show()
    app.exec_()
if __name__=='__main__':main()