# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CircularProgressBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BaseFrame = QtWidgets.QFrame(self.centralwidget)
        self.BaseFrame.setGeometry(QtCore.QRect(100, 100, 300, 300))
        self.BaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BaseFrame.setObjectName("BaseFrame")
        self.DialFrame = QtWidgets.QFrame(self.BaseFrame)
        self.DialFrame.setGeometry(QtCore.QRect(20, 20, 260, 260))
        self.DialFrame.setStyleSheet("\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.6 rgba(218,58,242,255), stop:0.595 rgba(225,255,255,0));\n"
"\n"
"border-radius:130px;")
        self.DialFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DialFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DialFrame.setObjectName("DialFrame")
        self.frame = QtWidgets.QFrame(self.DialFrame)
        self.frame.setGeometry(QtCore.QRect(10, 10, 240, 240))
        self.frame.setStyleSheet("background-color: rgb(119, 51, 164);\n"
"border-radius:120px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(50, 32, 141, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(113, 232, 238);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.progressValue = QtWidgets.QLabel(self.widget)
        self.progressValue.setStyleSheet("color: rgb(113, 232, 238);")
        self.progressValue.setObjectName("progressValue")
        self.gridLayout.addWidget(self.progressValue, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:1px solid  rgb(218, 58, 242); \n"
"background-color: rgba(250, 43, 63,0.3);\n"
"border-radius:10px;\n"
"color: rgb(45, 14, 81);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DialBaseFrame = QtWidgets.QFrame(self.BaseFrame)
        self.DialBaseFrame.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.DialBaseFrame.setStyleSheet("background-color: rgb(45, 14, 81);\n"
"border-radius:150px;")
        self.DialBaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DialBaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DialBaseFrame.setObjectName("DialBaseFrame")
        self.DialBaseFrame.raise_()
        self.DialFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dail"))
        self.progressValue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:26pt; vertical-align:super;\">%</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Loading.."))
        self.label_4.setText(_translate("MainWindow", "Harish "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
