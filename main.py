from PyQt5 import QtCore, QtGui, QtWidgets
from sales import Ui_salesWin
from incoming import Ui_salesWin as Ui_salesWin2
from outgoing import Ui_salesWin as Ui_salesWin3

import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AwmingPOS123"
)
mycursor = mydb.cursor()

class Ui_MainWindow(object):
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_salesWin3()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_salesWin2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_salesWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow3())
        self.pushButton.setGeometry(QtCore.QRect(370, 50, 151, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2())
        self.pushButton_2.setGeometry(QtCore.QRect(220, 50, 151, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow1())
        self.pushButton_3.setGeometry(QtCore.QRect(70, 50, 151, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OUTGOING"))
        self.pushButton_2.setText(_translate("MainWindow", "INCOMING"))
        self.pushButton_3.setText(_translate("MainWindow", "SALES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
