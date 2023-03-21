from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QVBoxLayout
from auth_signup import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 402)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(250, 250, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("signupButton")
        self.inputNickname = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNickname.setGeometry(QtCore.QRect(280, 50, 151, 41))
        self.inputNickname.setObjectName("inputNickname")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(185, 60, 81, 31))
        self.label.setObjectName("label")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(280, 110, 151, 41))
        self.inputPassword.setObjectName("inputPassword")
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 81, 31))
        self.label_2.setObjectName("label_2")
        self.inputConfirmPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConfirmPassword.setGeometry(QtCore.QRect(280, 170, 151, 41))
        self.inputConfirmPassword.setObjectName("inputConfirmPassword")
        self.inputConfirmPassword.setEchoMode(QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 131, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew_Chat = QtWidgets.QAction(MainWindow)
        self.actionNew_Chat.setObjectName("actionNew_Chat")
        self.actionLog_out = QtWidgets.QAction(MainWindow)
        self.actionLog_out.setObjectName("actionLog_out")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuAccount.addAction(self.actionNew_Chat)
        self.menuAccount.addAction(self.actionLog_out)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signupButton.clicked.connect(self.loginMeIn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signupButton.setText(_translate("MainWindow", "Signup"))
        self.label.setText(_translate("MainWindow", "Nickname"))
        self.label_2.setText(_translate("MainWindow", "Passsword"))
        self.label_3.setText(_translate("MainWindow", "Confirm Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew_Chat.setText(_translate("MainWindow", "New Chat"))
        self.actionLog_out.setText(_translate("MainWindow", "Log out"))

    def loginMeIn(self):
        username = self.inputNickname.text()
        password = self.inputPassword.text()
        confirm_password = self.inputConfirmPassword.text()
        signup_form = SignUpForm(username, password, confirm_password)
        signup_form.process_form()
        signup_form.validate_form()
        if signup_form.is_valid:
            self.signupButton.setText("Sign Up Successful")
            self.signupButton.adjustSize()
        else:
            formErrors = str()
            errorBox = QMessageBox()
            errorBox.setWindowTitle("Signup Errors")
            errorBox.setText("This is the main text")
            errorBox.setIcon(QMessageBox.Warning)
            errorBox.setStandardButtons(QMessageBox.Retry)
            # errorBox.setDefaultButton(QMessageBox.Retry)
            errorBox.setInformativeText("There were errors in this form")
            for field, error in signup_form.errors.items():
                formErrors += f"{field}: {error}"
            errorBox.setDetailedText(formErrors)

            self.signupButton.setText("Try Again")
            self.signupButton.adjustSize()

            x = errorBox.exec_()

            # print("There were errors in the form:\n")
            # for field, error in signup_form.errors.items():
            #     print(f"{field}: {error}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
