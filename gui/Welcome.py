from PyQt5.QtWidgets import  *
from PyQt5 import QtGui,QtCore     # QtCore is used for font color, size and style
from PyQt5.QtGui import QPixmap         # Qpixmap is used for images
import pyttsx3 as p          #pyttsx3 is used for speech which u want
import sys
from gui.login import Login
def main():
    app=QApplication(sys.argv)
    engine = p.init()              # initilize the speech engine
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1)
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Welcome To Mobo Software")
    splash = QSplashScreen()
    font = QtGui.QFont()
    font.setFamily("Algerian")
    font.setPointSize(45)
    splash.setFont(font)
    splash.showFullScreen()
    message = "Welcome To Mobo Software"
    splash.showMessage(message,QtCore.Qt.AlignCenter,QtGui.QColor.fromRgb(100, 200, 50))
    splash.show()
    import time
    time.sleep(0)
    engine.runAndWait()
    engine.stop()
    login = Login()
    login.show()
    splash.finish(login)
    app.exec_()
if __name__=='__main__':main()