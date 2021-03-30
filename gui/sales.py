from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from databaseinfo.dbconnection import DbConnection as db


class Sales(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("sales.ui", self)
        self.con = db.createconnection()
        self.cursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.modelNumber = self.txtnumber.text()
        self.quantity = self.txtquan.text()
        self.customerName = self.txtname.text()
        self.email = self.txtmail.text()
        self.address = self.txtadd.text()
        self.phone = self.txtphone.text()
        self.dates=self.txtdate.text()
        # d = self.cal.selectedDate()
        # year = d.year()
        # month = d.month()
        # day = d.day()
        # print(type(year))
        # print(month)
        # print(day)
        # self.dt = str(day) + "/" + str(month) + "/" + str(year)
        # print("selected date is " + self.dt)
        # print(type(self.dt))
        strsql = "select * from modeldetails where modelNumber=%s"
        self.cursor.execute(strsql, (self.modelNumber,))
        self.data = self.cursor.fetchone()
        self.status = self.cursor.rowcount
        print(self.data)
        strcheck = "select Quantity from modeldetails where modelNumber=%s"
        self.cursor.execute(strcheck,(self.modelNumber,))
        self.datar = self.cursor.fetchall()
        # self.rstatus = self.cursor.rowcount
        print(self.datar)
        for self.row in self.datar:
            print(self.row)
            res = int(''.join(map(str, self.row)))
            print(res)
            print(type(res))




        mn = len(self.modelNumber.strip())
        qu = len(self.quantity.strip())
        cn = len(self.customerName.strip())
        em = len(self.email.strip())
        ad = len(self.address.strip())
        ph = len(self.phone.strip())
        dt = len(self.dates.strip())


        if mn == 0 or qu == 0 or cn == 0 or em == 0 or ad == 0 or ph == 0 or dt == 0:
            self.showDialog("You are not inserted the data")


        elif self.status > 0:
            print("Model Number exist")


            if res >= int(self.quantity):
                strinsert = "insert into saledetails(modelNumber,quantity,customerName,email,address,phone,date) values(%s,%s,%s,%s,%s,%s,%s)"
                self.cursor.execute(strinsert, (
                self.modelNumber, int(self.quantity), self.customerName, self.email, self.address, self.phone, self.dates))
                self.con.commit()

                newqty = int(self.quantity)
                print(newqty)

                strupdate="update modeldetails set Quantity=Quantity-%s where modelNumber=%s"
                self.cursor.execute(strupdate,(int(newqty),self.modelNumber))
                self.con.commit()
                self.showDialog("Data inserted Successfully")


                
                self.txtnumber.setText("")
                self.txtquan.setText("")
                self.txtname.setText("")
                self.txtmail.setText("")
                self.txtadd.setText("")
                self.txtphone.setText("")
                self.txtdate.setText("")
            else:
                self.showDialog("SORRY!!!!!!!! Currently product is not available")



        else:
            self.showDialog("Model Number Does not exist")




    def showDialog(self, msg):  # show inserted data dialog box insertion successfully
        msgbox = QMessageBox()  # msg variable is used for insertion and not inserted dialoge box alert massage
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Sales details")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    sa = Sales()
    sa.show()
    app.exec_()


if __name__ == '__main__':

    main()