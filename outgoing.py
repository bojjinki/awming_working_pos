from PyQt5 import QtCore, QtGui, QtWidgets
from no_barcode import Ui_Dialog
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AwmingPOS123",
    database="Awming"
)
mycursor = mydb.cursor()

class Ui_salesWin(object):
    def openDialogue(self):
        self.dialog= QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
    
    def saveIncoming(self, salesWin, item_num):
        for item in item_num.keys():
            sqlFormula = "SELECT * From Inventory Where Barcode = %s"
            mycursor.execute(sqlFormula, (item,))
            item_lookup = mycursor.fetchall()
            
            item_tuple = []
            item_record = []

            if (item_lookup!=[]):
                for i in item_lookup:
                    new_stocks = i[4] - item_num[item]
                    now = datetime.now()
                    item_tuple.append((new_stocks, item))
                    item_record.append((item, i[4], item_num[item], new_stocks, now.date(), now.time()))

        sqlFormula2 = "UPDATE Inventory SET Stocks = %s WHERE Barcode = %s"
        mycursor.executemany(sqlFormula2, item_tuple)

        sqlFormula3 = "INSERT INTO Outgoing SET Barcode = %s, Previous_Stocks = %s, Removed_Stocks = %s, New_Total_Stocks = %s, Date = %s, Time = %s"
        mycursor.executemany(sqlFormula3, item_record)
        mydb.commit()

        salesWin.hide()

    def setupUi(self, salesWin):
        self.item_list = []
        self.items_prices = []
        self.item_dict = {}
        self.item_num = {}
        salesWin.setObjectName("salesWin")
        salesWin.resize(762, 413)
        self.centralwidget = QtWidgets.QWidget(salesWin)
        self.centralwidget.setObjectName("centralwidget")
        self.labelBarcode = QtWidgets.QLabel(self.centralwidget)
        self.labelBarcode.setGeometry(QtCore.QRect(30, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelBarcode.setFont(font)
        self.labelBarcode.setObjectName("labelBarcode")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.saveIncoming(salesWin, self.item_num))
        self.pushButton.setGeometry(QtCore.QRect(620, 20, 111, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 451, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.hitEnter)

        self.items = QtWidgets.QLabel(self.centralwidget)
        self.items.setGeometry(QtCore.QRect(30, 60, 351, 331))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.items.setFont(font)
        self.items.setFrameShape(QtWidgets.QFrame.Box)
        self.items.setText("")
        self.items.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.items.setObjectName("items")
        self.prices = QtWidgets.QLabel(self.centralwidget)
        self.prices.setGeometry(QtCore.QRect(380, 60, 351, 331))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prices.setFont(font)
        self.prices.setFrameShape(QtWidgets.QFrame.Box)
        self.prices.setText("")
        self.prices.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.prices.setObjectName("prices")
        salesWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(salesWin)
        QtCore.QMetaObject.connectSlotsByName(salesWin)

    def hitEnter(self):
        sqlFormula = "SELECT * From Inventory Where Barcode = %s"
        mycursor.execute(sqlFormula, (self.lineEdit.text(),))
        item_lookup = mycursor.fetchall()

        if (item_lookup!=[]):
            for i in item_lookup:
                item_name = i[1]

            if (item_name in self.item_dict.keys()): 
                self.item_dict[item_name] = self.item_dict[item_name] + 1 
                self.item_num[self.lineEdit.text()] = self.item_num[self.lineEdit.text()] + 1
            else:
                self.item_dict[item_name] = 1 
                self.item_num[self.lineEdit.text()] = 1
        else:
            self.openDialogue()

        self.lineEdit.clear()
        self.items.setText('\n'.join(map(str,self.item_dict.keys())))
        self.prices.setText('\n'.join(map(str,self.item_num.values())))

    def retranslateUi(self, salesWin):
        _translate = QtCore.QCoreApplication.translate
        salesWin.setWindowTitle(_translate("salesWin", "MainWindow"))
        self.labelBarcode.setText(_translate("salesWin", "Barcode"))
        self.pushButton.setText(_translate("salesWin", "Confirm Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    salesWin = QtWidgets.QMainWindow()
    ui = Ui_salesWin()
    ui.setupUi(salesWin)
    salesWin.show()
    sys.exit(app.exec_())
