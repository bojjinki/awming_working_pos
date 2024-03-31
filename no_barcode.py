from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def closeDialog(self, Dialog):
        Dialog.done(0)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 132)
        self.noData = QtWidgets.QLabel(Dialog)
        self.noData.setGeometry(QtCore.QRect(30, 20, 271, 71))
        self.noData.setAlignment(QtCore.Qt.AlignCenter)
        self.noData.setWordWrap(True)
        self.noData.setObjectName("noData")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.closeDialog(Dialog))
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.noData.setText(_translate("Dialog", "Barcode not registered! Take note and report to Kim"))
        self.pushButton.setText(_translate("Dialog", "OKAY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
