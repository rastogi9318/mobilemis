import mysql.connector as mysql
class DbConnection:
    @staticmethod
    def createconnection():
        con = mysql.connect(host="localhost", database="mobilemis", user="root", password="")
        return con
