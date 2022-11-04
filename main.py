import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from CircularProgressBar import Ui_MainWindow
import time 


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #######################################
        ######### Test the progress bar 
        ######################################
        self.progressBar(90)

        #######################################
        ######### Display the application 
        ######################################
        
        ## ==> REMOVE STANDARD TITLE BAR
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        self.show()

    def progressBar(self,value):
        #######################################
        ######### Progress bar style sheet 
        ######################################

        # ## ==> APPLY DROP SHADOW EFFECT
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 120))
        # self.ui.DialBaseFrame.setGraphicsEffect(self.shadow)

        self.dialReading(value) # pass the value to dial reading 

        styleSheet ="""QFrame{
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop_1} rgba(218,58,242,255), stop:{stop_2} rgba(225,255,255,0));
            border-radius:130px;}
            """

        stop1 = str((100 - value)/100) # Invert the value   
        stop2 = str(((100 - value)/100) - 0.0035) # Invert the value   

        newStyleSheet = styleSheet.replace("{stop_1}",stop1).replace("{stop_2}",stop2) # Replace the dial values in the Stylesheet string 

        self.ui.DialFrame.setStyleSheet(newStyleSheet)
    
    def dialReading(self,value):
        
        htmlText = """<html><head/><body><p><span style=" font-size:72pt;">{Value}</span><span style=" font-size:36pt; vertical-align:super;">%</span></p></body></html>"""
        # REPLACE VALUE
        newHtml = htmlText.replace("{Value}", str(value))

        #set the value 
        self.ui.progressValue.setText(newHtml)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())