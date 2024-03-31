from PyQt5 import QtCore, QtGui, QtWidgets
from complete import Ui_Dialog
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AwmingPOS123",
    database="Awming"
)
mycursor = mydb.cursor()

class Ui_confirmWindow(object):
    def openConfirmDialog(self, confirmWindow, salesWin=0, item_num = {}, item_dict = {}):
        self.dialog= QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        confirmWindow.hide()
        salesWin.hide()
        self.dialog.show()

        item_tuple = []
        item_record = []

        for item in item_num.keys():
            sqlFormula = "SELECT * From Inventory Where Barcode = %s"
            mycursor.execute(sqlFormula, (item,))
            item_lookup = mycursor.fetchall()
            
            if (item_lookup!=[]):
                for i in item_lookup:
                    item_remaining = i[4] - item_num[item]
                    item_tuple.append((item_remaining, item))

        sqlFormula2 = "UPDATE Inventory SET Stocks = %s WHERE Barcode = %s"
        mycursor.executemany(sqlFormula2, item_tuple)

        now = datetime.now()
        

        sqlFormula4 = "SELECT * FROM Sales ORDER BY Transaction_No DESC LIMIT 1"
        mycursor.execute(sqlFormula4)
        trans_no = mycursor.fetchall()

        if (trans_no!=[]):
            for i in trans_no:
                if (i[3] == now.date()):
                    add_tr = i[0] + 1
                else:
                    add_tr = 1
        else:
            add_tr = 1
        
        item_record.append((add_tr, str(item_num), sum(item_dict.values()), now.date(), now.time()))
    
        sqlFormula3 = "INSERT INTO Sales SET Transaction_No = %s, Items = %s, Total_Paid = %s, Date = %s, Time = %s"
        mycursor.executemany(sqlFormula3, item_record)
        mydb.commit()

    
    def closeWindow(self, confirmWindow):
        confirmWindow.hide()

    def hitEnter(self):
        self.label_6.setText(str(int(self.lineEdit.text()) - int(self.label_4.text())))
    
    def setupUi(self, confirmWindow, salesWin=0, item_num = {}, item_dict = {}):
        confirmWindow.setObjectName("confirmWindow")
        confirmWindow.resize(332, 256)
        self.centralwidget = QtWidgets.QWidget(confirmWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 141, 31))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.hitEnter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(254, 40, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 120, 141, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 160, 141, 31))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openConfirmDialog(confirmWindow, salesWin, item_num, item_dict))
        self.pushButton_2.setGeometry(QtCore.QRect(110, 200, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.closeWindow(confirmWindow))
        self.pushButton_3.setGeometry(QtCore.QRect(180, 200, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        confirmWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(confirmWindow)
        QtCore.QMetaObject.connectSlotsByName(confirmWindow)

    def retranslateUi(self, confirmWindow):
        _translate = QtCore.QCoreApplication.translate
        confirmWindow.setWindowTitle(_translate("confirmWindow", "MainWindow"))
        self.label.setText(_translate("confirmWindow", "Payment Tendered"))
        self.label_2.setText(_translate("confirmWindow", "Mode of Payment"))
        self.comboBox.setItemText(0, _translate("confirmWindow", "Cash"))
        self.comboBox.setItemText(1, _translate("confirmWindow", "GCash"))
        self.comboBox.setItemText(2, _translate("confirmWindow", "Bank Transfer"))
        self.comboBox.setItemText(3, _translate("confirmWindow", "Others"))
        self.pushButton.setText(_translate("confirmWindow", "SELECT"))
        self.label_3.setText(_translate("confirmWindow", "Item Total"))
        self.label_5.setText(_translate("confirmWindow", "Change"))
        self.pushButton_2.setText(_translate("confirmWindow", "OK"))
        self.pushButton_3.setText(_translate("confirmWindow", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmWindow = QtWidgets.QMainWindow()
    ui = Ui_confirmWindow()
    ui.setupUi(confirmWindow)
    confirmWindow.show()
    sys.exit(app.exec_())
