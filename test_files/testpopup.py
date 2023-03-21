from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 370)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.popupButton = QtWidgets.QPushButton(self.centralwidget)
        self.popupButton.setGeometry(QtCore.QRect(140, 110, 211, 71))
        self.popupButton.setObjectName("popupButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.popupButton.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.popupButton.setText(_translate("MainWindow", "Show Pop Up"))

    def show_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Tutorial on PyQT5")
        message.setText("This is the main text")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(
            QMessageBox.Cancel
            | QMessageBox.Retry
            | QMessageBox.YesToAll
            | QMessageBox.Ignore
        )
        message.setDefaultButton(QMessageBox.YesToAll)
        message.setInformativeText("This is informative text")
        message.setDetailedText("Detailed text will be included here")
        message.buttonClicked.connect(self.popup_button)

        x = message.exec_()

    def popup_button(self, i):
        print(f"{i.text()}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
