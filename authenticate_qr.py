import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from two_factor import TwoFactorAuth
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Generate QR code image for two factor authentication
        self.two_factor_auth = TwoFactorAuth()
        img = self.two_factor_auth.generate()
        self.secret_key = self.two_factor_auth.secret_key

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.verifyButton.setGeometry(QtCore.QRect(298, 370, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.verifyButton.setFont(font)
        self.verifyButton.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.verifyButton.setObjectName("verifyButton")
        self.codeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.codeInput.setGeometry(QtCore.QRect(100, 370, 151, 31))
        self.codeInput.setObjectName("codeInput")

        image = ImageQt(img.convert("RGBA"))

        self.QRCode = QtWidgets.QLabel(self.centralwidget)
        self.QRCode.setGeometry(QtCore.QRect(90, 30, 300, 300))
        self.QRCode.setText("")
        self.QRCode.setPixmap(QtGui.QPixmap.fromImage(image))
        self.QRCode.setScaledContents(True)
        self.QRCode.setObjectName("QRCode")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.verifyButton.clicked.connect(self.authenticate_qr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.verifyButton.setText(_translate("MainWindow", "Verify Code"))

    def authenticate_qr(self):
        code = self.codeInput.text()
        status = self.two_factor_auth.authenticate(code)
        if status:
            self.verifyButton.setText("Authenticated")
            self.verifyButton.adjustSize()
        else:
            self.verifyButton.setText("Not Authenticated")
            self.verifyButton.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
