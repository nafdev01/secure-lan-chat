import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL.ImageQt import ImageQt
from session_backend import Session, Log, initialize_tables_if_not_exists
from message_backend import Message, Archive
from client_backend import Client
from auth_backend import SignUp, LogIn, Reset


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.signup_form = SignUp()
        self.reset_form = Reset()
        self.login_form = LogIn()
        self.session_manager = Session()
        self.log_manager = Log()
        self.message_manager = Message()
        self.client = Client()
        self.archive_manager = Archive()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageConnect = QtWidgets.QWidget()
        self.pageConnect.setObjectName("pageConnect")
        self.buttonConnServer = QtWidgets.QPushButton(self.pageConnect)
        self.buttonConnServer.setGeometry(QtCore.QRect(260, 220, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.buttonConnServer.setFont(font)
        self.buttonConnServer.setObjectName("buttonConnServer")
        self.stackedWidget.addWidget(self.pageConnect)
        self.pageAuth = QtWidgets.QWidget()
        self.pageAuth.setObjectName("pageAuth")
        self.authTabs = QtWidgets.QTabWidget(self.pageAuth)
        self.authTabs.setGeometry(QtCore.QRect(10, 10, 731, 501))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.authTabs.setFont(font)
        self.authTabs.setObjectName("authTabs")
        self.tabLogin = QtWidgets.QWidget()
        self.tabLogin.setObjectName("tabLogin")
        self.inputNickLog = QtWidgets.QLineEdit(self.tabLogin)
        self.inputNickLog.setGeometry(QtCore.QRect(310, 110, 241, 31))
        self.inputNickLog.setObjectName("inputNickLog")
        self.labelNickLog = QtWidgets.QLabel(self.tabLogin)
        self.labelNickLog.setGeometry(QtCore.QRect(170, 110, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelNickLog.setFont(font)
        self.labelNickLog.setObjectName("labelNickLog")
        self.inputPassLog = QtWidgets.QLineEdit(self.tabLogin)
        self.inputPassLog.setGeometry(QtCore.QRect(310, 160, 241, 31))
        self.inputPassLog.setText("")
        self.inputPassLog.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassLog.setObjectName("inputPassLog")
        self.labelPassLog = QtWidgets.QLabel(self.tabLogin)
        self.labelPassLog.setGeometry(QtCore.QRect(170, 160, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelPassLog.setFont(font)
        self.labelPassLog.setObjectName("labelPassLog")
        self.input2FALog = QtWidgets.QLineEdit(self.tabLogin)
        self.input2FALog.setGeometry(QtCore.QRect(310, 210, 241, 31))
        self.input2FALog.setText("")
        self.input2FALog.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input2FALog.setObjectName("input2FALog")
        self.label2FALog = QtWidgets.QLabel(self.tabLogin)
        self.label2FALog.setGeometry(QtCore.QRect(170, 210, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label2FALog.setFont(font)
        self.label2FALog.setObjectName("label2FALog")
        self.buttonLogin = QtWidgets.QPushButton(self.tabLogin)
        self.buttonLogin.setGeometry(QtCore.QRect(250, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.buttonLogin.setFont(font)
        self.buttonLogin.setObjectName("buttonLogin")
        self.labelTitleLog = QtWidgets.QLabel(self.tabLogin)
        self.labelTitleLog.setGeometry(QtCore.QRect(320, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleLog.setFont(font)
        self.labelTitleLog.setObjectName("labelTitleLog")
        self.labelInstructLog = QtWidgets.QLabel(self.tabLogin)
        self.labelInstructLog.setGeometry(QtCore.QRect(240, 60, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labelInstructLog.setFont(font)
        self.labelInstructLog.setObjectName("labelInstructLog")
        self.commandPassReset = QtWidgets.QCommandLinkButton(self.tabLogin)
        self.commandPassReset.setGeometry(QtCore.QRect(280, 330, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setUnderline(False)
        self.commandPassReset.setFont(font)
        self.commandPassReset.setObjectName("commandPassReset")
        self.authTabs.addTab(self.tabLogin, "")
        self.tabSignup = QtWidgets.QWidget()
        self.tabSignup.setObjectName("tabSignup")
        self.inputNickSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputNickSign.setGeometry(QtCore.QRect(220, 110, 231, 31))
        self.inputNickSign.setDragEnabled(True)
        self.inputNickSign.setPlaceholderText("")
        self.inputNickSign.setObjectName("inputNickSign")
        self.labelNickSign = QtWidgets.QLabel(self.tabSignup)
        self.labelNickSign.setGeometry(QtCore.QRect(70, 110, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelNickSign.setFont(font)
        self.labelNickSign.setObjectName("labelNickSign")
        self.inputPassSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputPassSign.setGeometry(QtCore.QRect(220, 160, 231, 31))
        self.inputPassSign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassSign.setObjectName("inputPassSign")
        self.labelPassSign = QtWidgets.QLabel(self.tabSignup)
        self.labelPassSign.setGeometry(QtCore.QRect(70, 160, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelPassSign.setFont(font)
        self.labelPassSign.setObjectName("labelPassSign")
        self.labelQRCode = QtWidgets.QLabel(self.tabSignup)
        self.labelQRCode.setGeometry(QtCore.QRect(520, 120, 161, 161))
        self.labelQRCode.setText("")
        self.labelQRCode.setPixmap(QtGui.QPixmap("UI_files/../img/chat_icon.png"))
        self.labelQRCode.setScaledContents(True)
        self.labelQRCode.setObjectName("labelQRCode")
        self.inputPassConfSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputPassConfSign.setGeometry(QtCore.QRect(220, 210, 231, 31))
        self.inputPassConfSign.setText("")
        self.inputPassConfSign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassConfSign.setObjectName("inputPassConfSign")
        self.labelPassConfSign = QtWidgets.QLabel(self.tabSignup)
        self.labelPassConfSign.setGeometry(QtCore.QRect(70, 210, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelPassConfSign.setFont(font)
        self.labelPassConfSign.setObjectName("labelPassConfSign")
        self.buttonSign = QtWidgets.QPushButton(self.tabSignup)
        self.buttonSign.setGeometry(QtCore.QRect(210, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.buttonSign.setFont(font)
        self.buttonSign.setObjectName("buttonSign")
        self.button2FAGen = QtWidgets.QPushButton(self.tabSignup)
        self.button2FAGen.setGeometry(QtCore.QRect(520, 320, 141, 31))
        self.button2FAGen.setObjectName("button2FAGen")
        self.labelTitleSign = QtWidgets.QLabel(self.tabSignup)
        self.labelTitleSign.setGeometry(QtCore.QRect(240, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleSign.setFont(font)
        self.labelTitleSign.setObjectName("labelTitleSign")
        self.labelQRCodeSign = QtWidgets.QLabel(self.tabSignup)
        self.labelQRCodeSign.setGeometry(QtCore.QRect(520, 40, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.labelQRCodeSign.setFont(font)
        self.labelQRCodeSign.setWordWrap(True)
        self.labelQRCodeSign.setObjectName("labelQRCodeSign")
        self.labelInstructSign = QtWidgets.QLabel(self.tabSignup)
        self.labelInstructSign.setGeometry(QtCore.QRect(170, 70, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labelInstructSign.setFont(font)
        self.labelInstructSign.setObjectName("labelInstructSign")
        self.authTabs.addTab(self.tabSignup, "")
        self.tabResetPass = QtWidgets.QWidget()
        self.tabResetPass.setObjectName("tabResetPass")
        self.label2FAReset = QtWidgets.QLabel(self.tabResetPass)
        self.label2FAReset.setGeometry(QtCore.QRect(120, 160, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label2FAReset.setFont(font)
        self.label2FAReset.setObjectName("label2FAReset")
        self.labelPassConfReset = QtWidgets.QLabel(self.tabResetPass)
        self.labelPassConfReset.setGeometry(QtCore.QRect(120, 210, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelPassConfReset.setFont(font)
        self.labelPassConfReset.setObjectName("labelPassConfReset")
        self.input2FAReset = QtWidgets.QLineEdit(self.tabResetPass)
        self.input2FAReset.setGeometry(QtCore.QRect(320, 160, 231, 31))
        self.input2FAReset.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input2FAReset.setObjectName("input2FAReset")
        self.inputPassConfReset = QtWidgets.QLineEdit(self.tabResetPass)
        self.inputPassConfReset.setGeometry(QtCore.QRect(320, 210, 231, 31))
        self.inputPassConfReset.setText("")
        self.inputPassConfReset.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassConfReset.setObjectName("inputPassConfReset")
        self.inputPassReset = QtWidgets.QLineEdit(self.tabResetPass)
        self.inputPassReset.setGeometry(QtCore.QRect(320, 260, 231, 31))
        self.inputPassReset.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassReset.setObjectName("inputPassReset")
        self.labelPassReset = QtWidgets.QLabel(self.tabResetPass)
        self.labelPassReset.setGeometry(QtCore.QRect(120, 260, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelPassReset.setFont(font)
        self.labelPassReset.setObjectName("labelPassReset")
        self.labelNickReset = QtWidgets.QLabel(self.tabResetPass)
        self.labelNickReset.setGeometry(QtCore.QRect(120, 100, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelNickReset.setFont(font)
        self.labelNickReset.setObjectName("labelNickReset")
        self.inputNickReset = QtWidgets.QLineEdit(self.tabResetPass)
        self.inputNickReset.setGeometry(QtCore.QRect(320, 100, 231, 31))
        self.inputNickReset.setText("")
        self.inputNickReset.setDragEnabled(True)
        self.inputNickReset.setObjectName("inputNickReset")
        self.labelTitleReset = QtWidgets.QLabel(self.tabResetPass)
        self.labelTitleReset.setGeometry(QtCore.QRect(240, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleReset.setFont(font)
        self.labelTitleReset.setObjectName("labelTitleReset")
        self.labelInstructReset = QtWidgets.QLabel(self.tabResetPass)
        self.labelInstructReset.setGeometry(QtCore.QRect(220, 60, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labelInstructReset.setFont(font)
        self.labelInstructReset.setObjectName("labelInstructReset")
        self.buttonReset = QtWidgets.QPushButton(self.tabResetPass)
        self.buttonReset.setGeometry(QtCore.QRect(250, 320, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.buttonReset.setFont(font)
        self.buttonReset.setObjectName("buttonReset")
        self.authTabs.addTab(self.tabResetPass, "")
        self.stackedWidget.addWidget(self.pageAuth)
        self.pageChatActive = QtWidgets.QWidget()
        self.pageChatActive.setObjectName("pageChatActive")
        self.buttonMessageSendActive = QtWidgets.QPushButton(self.pageChatActive)
        self.buttonMessageSendActive.setGeometry(QtCore.QRect(50, 500, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMessageSendActive.setFont(font)
        self.buttonMessageSendActive.setAutoDefault(True)
        self.buttonMessageSendActive.setFlat(False)
        self.buttonMessageSendActive.setObjectName("buttonMessageSendActive")
        self.inputMessageActive = QtWidgets.QTextEdit(self.pageChatActive)
        self.inputMessageActive.setGeometry(QtCore.QRect(20, 420, 721, 61))
        self.inputMessageActive.setObjectName("inputMessageActive")
        self.displayMessageActive = QtWidgets.QTextEdit(self.pageChatActive)
        self.displayMessageActive.setGeometry(QtCore.QRect(20, 40, 721, 361))
        self.displayMessageActive.setReadOnly(True)
        self.displayMessageActive.setObjectName("displayMessageActive")
        self.comboRecipientActive = QtWidgets.QComboBox(self.pageChatActive)
        self.comboRecipientActive.setGeometry(QtCore.QRect(590, 500, 131, 31))
        self.comboRecipientActive.setObjectName("comboRecipientActive")
        self.comboRecipientActive.addItem("")
        self.comboRecipientActive.addItem("")
        self.comboRecipientActive.addItem("")
        self.comboRecipientActive.addItem("")
        self.labelSendToActive = QtWidgets.QLabel(self.pageChatActive)
        self.labelSendToActive.setGeometry(QtCore.QRect(510, 500, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelSendToActive.setFont(font)
        self.labelSendToActive.setObjectName("labelSendToActive")
        self.buttonGoToArchive = QtWidgets.QPushButton(self.pageChatActive)
        self.buttonGoToArchive.setGeometry(QtCore.QRect(590, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.buttonGoToArchive.setFont(font)
        self.buttonGoToArchive.setAutoDefault(True)
        self.buttonGoToArchive.setFlat(False)
        self.buttonGoToArchive.setObjectName("buttonGoToArchive")
        self.buttonLogOut = QtWidgets.QPushButton(self.pageChatActive)
        self.buttonLogOut.setGeometry(QtCore.QRect(30, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.buttonLogOut.setFont(font)
        self.buttonLogOut.setAutoDefault(True)
        self.buttonLogOut.setFlat(False)
        self.buttonLogOut.setObjectName("buttonLogOut")
        self.stackedWidget.addWidget(self.pageChatActive)
        self.pageChatArchive = QtWidgets.QWidget()
        self.pageChatArchive.setObjectName("pageChatArchive")
        self.displayMessageArchive = QtWidgets.QTextEdit(self.pageChatArchive)
        self.displayMessageArchive.setGeometry(QtCore.QRect(20, 80, 721, 441))
        self.displayMessageArchive.setReadOnly(True)
        self.displayMessageArchive.setObjectName("displayMessageArchive")
        self.labelTitleArchive = QtWidgets.QLabel(self.pageChatArchive)
        self.labelTitleArchive.setGeometry(QtCore.QRect(260, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleArchive.setFont(font)
        self.labelTitleArchive.setObjectName("labelTitleArchive")
        self.buttonDeleteHistory = QtWidgets.QPushButton(self.pageChatArchive)
        self.buttonDeleteHistory.setGeometry(QtCore.QRect(620, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.buttonDeleteHistory.setFont(font)
        self.buttonDeleteHistory.setAutoDefault(True)
        self.buttonDeleteHistory.setFlat(False)
        self.buttonDeleteHistory.setObjectName("buttonDeleteHistory")
        self.buttonGoToActiveChat = QtWidgets.QPushButton(self.pageChatArchive)
        self.buttonGoToActiveChat.setGeometry(QtCore.QRect(30, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.buttonGoToActiveChat.setFont(font)
        self.buttonGoToActiveChat.setAutoDefault(True)
        self.buttonGoToActiveChat.setFlat(False)
        self.buttonGoToActiveChat.setObjectName("buttonGoToActiveChat")
        self.stackedWidget.addWidget(self.pageChatArchive)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionArchives = QtWidgets.QAction(MainWindow)
        self.actionArchives.setObjectName("actionArchives")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.authTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button listeners
        self.buttonConnServer.clicked.connect(self.connect_server)
        self.button2FAGen.clicked.connect(self.generate_qrcode)
        self.buttonLogin.clicked.connect(self.login)
        self.buttonMessageSendActive.clicked.connect(self.send_message)
        self.commandPassReset.clicked.connect(self.switch_reset)
        self.buttonGoToArchive.clicked.connect(self.go_to_archive)
        self.buttonGoToActiveChat.clicked.connect(self.go_to_active_chat)
        self.buttonLogOut.clicked.connect(self.logout)
        self.buttonSign.clicked.connect(self.sign_up)
        self.buttonReset.clicked.connect(self.reset_password)
        self.buttonDeleteHistory.clicked.connect(self.delete_messages)

    def connect_server(self):
        if initialize_tables_if_not_exists():
            successBox = QtWidgets.QMessageBox()
            successBox.setWindowTitle("Success")
            successBox.setText("You have successfully connected to the server")
            successBox.setIcon(QtWidgets.QMessageBox.Information)
            successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            successBox.exec_()
            self.stackedWidget.setCurrentIndex(1)
        else:
            successBox = QtWidgets.QMessageBox()
            successBox.setWindowTitle("Error Connecting to server")
            successBox.setText("Try Again")
            successBox.setIcon(QtWidgets.QMessageBox.Critical)
            successBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
            successBox.exec_()

    def generate_qrcode(self):
        nickname = self.inputNickSign.text()
        # Generate QR code image for two factor authentication
        img, secret_key = self.signup_form.generate(nickname)
        image = ImageQt(img.convert("RGBA"))
        self.labelQRCode.setPixmap(QtGui.QPixmap.fromImage(image))
        self.log_manager.submit_log(nickname, "Generated QRCode")

    def send_message(self):
        # set recipient to currently selected
        sender = self.message_manager.sender
        recipient = self.comboRecipientActive.currentText()
        # Get message from input box
        message = self.inputMessageActive.toPlainText()
        # Clear input box
        self.inputMessageActive.clear()
        # Add message to chat display
        self.displayMessageActive.append(
            f"{sender}: {message}........('Sent to {recipient}')"
        )
        self.message_manager.send_message(recipient, message)
        self.log_manager.submit_log(
            sender,
            f"Sent a message '{message[:15]}'... to {recipient}",
        )
        self.client.send_message(message)

    def switch_reset(self):
        # go to the reset tab
        self.authTabs.setCurrentIndex(2)

    def delete_messages(self):
        self.archive_manager.delete_messages()
        self.displayMessageArchive.clear()
        successBox = QtWidgets.QMessageBox()
        successBox.setWindowTitle("Deleted")
        successBox.setText("You have deleted your messages")
        successBox.setIcon(QtWidgets.QMessageBox.Information)
        successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        successBox.exec_()
        self.stackedWidget.setCurrentIndex(2)

    def go_to_archive(self):
        username = self.session_manager.username
        self.archive_manager.set_username(username)
        messages = self.archive_manager.get_messages()
        if messages:
            for message in self.archive_manager.messages:
                self.displayMessageArchive.append(f"{message[0]}: {message[1]}')")
            successBox = QtWidgets.QMessageBox()
            successBox.setWindowTitle("Archive")
            successBox.setText("You Are Viewing Archived Messages")
            successBox.setIcon(QtWidgets.QMessageBox.Information)
            successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.authTabs.setCurrentIndex(0)
            successBox.exec_()
        self.stackedWidget.setCurrentIndex(3)

    def go_to_active_chat(self):
        # go to the archives window
        self.displayMessageArchive.clear()
        self.stackedWidget.setCurrentIndex(2)

    def logout(self):
        self.displayMessageActive.clear()
        self.session_manager.set_offline()
        self.client.end_connection()
        self.stackedWidget.setCurrentIndex(1)

    def login(self):
        emptyInputFields = str()
        nickname = self.inputNickLog.text()
        password = self.inputPassLog.text()
        two_factor_code = self.input2FALog.text()
        self.login_form.process_form(nickname, password, two_factor_code)
        for field, value in self.login_form.form_data.items():
            if value == "":
                emptyInputFields += f"Fill in the {field} field\n"

        if emptyInputFields != "":
            errorBox = QtWidgets.QMessageBox()
            errorBox.setWindowTitle("Empty Fields")
            errorBox.setText(f"{emptyInputFields}")
            errorBox.setIcon(QtWidgets.QMessageBox.Critical)
            errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
            errorBox.exec_()
        else:
            user_athenticated = self.login_form.authenticate_user()
            if user_athenticated:
                _translate = QtCore.QCoreApplication.translate
                successBox = QtWidgets.QMessageBox()
                successBox.setWindowTitle("Success")
                successBox.setText(f"You Have Logged In Successfully")
                successBox.setIcon(QtWidgets.QMessageBox.Information)
                successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.client.get_username(nickname)
                self.client.set_display_field(self.displayMessageActive)
                self.client.create_connection()
                self.session_manager.set_username(nickname)
                self.session_manager.set_online(nickname)
                self.session_manager.get_active_users()
                user_index = 0
                for active_user in self.session_manager.active_users:
                    self.comboRecipientActive.setItemText(
                        user_index, _translate("MainWindow", f"{active_user}")
                    )
                    user_index += 1

                self.message_manager.set_sender(nickname)
                self.log_manager.submit_log(nickname, "Successfully logged in")
                self.signup_form.reset(
                    self.inputNickLog,
                    self.inputPassLog,
                    self.input2FALog,
                )
                self.stackedWidget.setCurrentIndex(2)
                successBox.exec_()
            else:
                self.log_manager.submit_log(nickname, "Failed log in")
                authErrors = str()
                for error, value in self.login_form.errors.items():
                    authErrors += f"{error}{value}\n"

                errorBox = QtWidgets.QMessageBox()
                errorBox.setWindowTitle("Wrong Credentials")
                errorBox.setText(
                    f"Please enter valid login credentials.\n All fields are case sensitive"
                )
                errorBox.setIcon(QtWidgets.QMessageBox.Critical)
                errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
                errorBox.exec_()

    def sign_up(self):
        nickname = self.inputNickSign.text()
        password = self.inputPassSign.text()
        confirm_password = self.inputPassConfSign.text()
        self.signup_form.process_form(nickname, password, confirm_password)
        self.signup_form.validate_form()
        if self.signup_form.is_valid:
            if not self.signup_form.get_user(nickname):
                create_user = self.signup_form.store_user_info()
                if create_user:
                    self.session_manager.start_session(nickname, "offline")
                    self.log_manager.submit_log(nickname, "Successful sign up")
                    self.signup_form.reset(
                        self.inputNickSign,
                        self.inputPassSign,
                        self.inputPassConfSign,
                    )
                    successBox = QtWidgets.QMessageBox()
                    successBox.setWindowTitle("Success")
                    successBox.setText("You Have Signed Up Successfully")
                    successBox.setIcon(QtWidgets.QMessageBox.Information)
                    successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.authTabs.setCurrentIndex(0)
                    successBox.exec_()
            else:
                self.log_manager.submit_log(nickname, "Failed duplicate sign up")
                errorBox = QtWidgets.QMessageBox()
                errorBox.setWindowTitle("Signup Errors")
                errorBox.setText("User with that nickname already exists")
                errorBox.setIcon(QtWidgets.QMessageBox.Critical)
                errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
                errorBox.exec_()
        else:
            formErrors = str()
            formErrorFields = str()
            errorBox = QtWidgets.QMessageBox()
            errorBox.setWindowTitle("Signup Errors")
            errorBox.setIcon(QtWidgets.QMessageBox.Critical)
            errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
            for field, error in self.signup_form.errors.items():
                formErrors += f"{error}\n"
                formErrorFields += f"{field}, "
            errorBox.setText(formErrors)
            errorBox.exec_()

    def reset_password(self):
        nickname = self.inputNickReset.text()
        password = self.inputPassReset.text()
        confirm_password = self.inputPassConfReset.text()
        two_factor_code = self.input2FAReset.text()
        self.reset_form.process_form(
            nickname, password, confirm_password, two_factor_code
        )
        self.reset_form.validate_form()
        if self.reset_form.is_valid:
            if self.reset_form.authenticate_user():
                create_user = self.reset_form.store_user_info()
                if create_user:
                    self.session_manager.start_session(nickname, "offline")
                    self.log_manager.submit_log(nickname, "Successful Password Reset")
                    self.reset_form.reset(
                        self.inputNickReset,
                        self.inputPassReset,
                        self.inputPassConfReset,
                        self.input2FAReset,
                    )
                    successBox = QtWidgets.QMessageBox()
                    successBox.setWindowTitle("Success")
                    successBox.setText("You Have Reset Your Password Successfully")
                    successBox.setIcon(QtWidgets.QMessageBox.Information)
                    successBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.authTabs.setCurrentIndex(0)
                    successBox.exec_()
            else:
                self.log_manager.submit_log(nickname, "Failed reset")
                errorBox = QtWidgets.QMessageBox()
                errorBox.setWindowTitle("Reset Errors")
                errorBox.setText("User with those credentials does not exist")
                errorBox.setIcon(QtWidgets.QMessageBox.Critical)
                errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
                errorBox.exec_()
        else:
            formErrors = str()
            formErrorFields = str()
            errorBox = QtWidgets.QMessageBox()
            errorBox.setWindowTitle("Signup Errors")
            errorBox.setIcon(QtWidgets.QMessageBox.Critical)
            errorBox.setStandardButtons(QtWidgets.QMessageBox.Retry)
            for field, error in self.reset_form.errors.items():
                formErrors += f"{error}\n"
                formErrorFields += f"{field}, "
            errorBox.setText(formErrors)
            errorBox.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Chat Client"))
        self.buttonConnServer.setText(_translate("MainWindow", "CONNECT"))
        self.inputNickLog.setPlaceholderText(
            _translate("MainWindow", "Enter your Nickname")
        )
        self.labelNickLog.setText(_translate("MainWindow", "Nickname"))
        self.inputPassLog.setPlaceholderText(
            _translate("MainWindow", "Enter your password")
        )
        self.labelPassLog.setText(_translate("MainWindow", "Password"))
        self.input2FALog.setPlaceholderText(
            _translate("MainWindow", "Enter your 6 digit 2FA Code")
        )
        self.label2FALog.setText(_translate("MainWindow", "2FA Code"))
        self.buttonLogin.setText(_translate("MainWindow", "LOG IN"))
        self.labelTitleLog.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">LOG IN</p></body></html>',
            )
        )
        self.labelInstructLog.setText(
            _translate(
                "MainWindow", "Fill in all the fields below using your credentials"
            )
        )
        self.commandPassReset.setText(_translate("MainWindow", "Forgot your password?"))
        self.authTabs.setTabText(
            self.authTabs.indexOf(self.tabLogin), _translate("MainWindow", "Login")
        )
        self.inputNickSign.setToolTip(
            _translate("MainWindow", "Nickname must be at least 6 characters long")
        )
        self.labelNickSign.setText(_translate("MainWindow", "Nickname"))
        self.inputPassSign.setToolTip(
            _translate(
                "MainWindow",
                "The password must be at least 8 character long, and include at least one undercase letter, one lowercase letter, one character and one special character",
            )
        )
        self.labelPassSign.setText(_translate("MainWindow", "Password"))
        self.inputPassConfSign.setToolTip(
            _translate(
                "MainWindow", "The confirm passsword fieldmust match the password field"
            )
        )
        self.labelPassConfSign.setText(_translate("MainWindow", "Confirm Password"))
        self.buttonSign.setText(_translate("MainWindow", "SIGN UP"))
        self.button2FAGen.setToolTip(_translate("MainWindow", "Generate A New QRCode"))
        self.button2FAGen.setText(_translate("MainWindow", "Generate QRCode"))
        self.labelTitleSign.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">SIGN UP</p></body></html>',
            )
        )
        self.labelQRCodeSign.setText(
            _translate(
                "MainWindow",
                "Generate the QRCode After Entering Your Nickname and Scan it using an Authenticator App to Set Up 2FA",
            )
        )
        self.labelInstructSign.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Fill in all the fields below as required</p></body></html>',
            )
        )
        self.authTabs.setTabText(
            self.authTabs.indexOf(self.tabSignup), _translate("MainWindow", "Signup")
        )
        self.label2FAReset.setText(_translate("MainWindow", "2FA Code"))
        self.labelPassConfReset.setText(
            _translate("MainWindow", "Confirm New Password")
        )
        self.input2FAReset.setToolTip(
            _translate(
                "MainWindow",
                "Enter the 6 digit code geenrated by the authenticator app",
            )
        )
        self.input2FAReset.setPlaceholderText(
            _translate("MainWindow", "Enter 6 digit Authenticator Code")
        )
        self.inputPassConfReset.setToolTip(
            _translate(
                "MainWindow",
                "The confirm new passsword fieldmust match the new password field",
            )
        )
        self.inputPassConfReset.setPlaceholderText(
            _translate("MainWindow", "Confirm Your New Password")
        )
        self.inputPassReset.setToolTip(
            _translate(
                "MainWindow",
                "The new password must be at least 8 character long, and include at least one undercase letter, one lowercase letter, one character and one special character.",
            )
        )
        self.inputPassReset.setPlaceholderText(
            _translate("MainWindow", "Enter Your New Password")
        )
        self.labelPassReset.setText(_translate("MainWindow", "New Password"))
        self.labelNickReset.setText(_translate("MainWindow", "Nickname"))
        self.inputNickReset.setToolTip(_translate("MainWindow", "Enter your nickname"))
        self.inputNickReset.setPlaceholderText(
            _translate("MainWindow", "Enter Your Nickname")
        )
        self.labelTitleReset.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">RESET PASSWORD</p></body></html>',
            )
        )
        self.labelInstructReset.setText(
            _translate(
                "MainWindow", "Fill in all the fields below to reset your password"
            )
        )
        self.buttonReset.setText(_translate("MainWindow", "RESET PASSWORD"))
        self.authTabs.setTabText(
            self.authTabs.indexOf(self.tabResetPass),
            _translate("MainWindow", "Reset Password"),
        )
        self.buttonMessageSendActive.setText(_translate("MainWindow", "SEND"))
        self.comboRecipientActive.setItemText(0, _translate("MainWindow", "Everyone"))
        self.comboRecipientActive.setItemText(1, _translate("MainWindow", "First User"))
        self.comboRecipientActive.setItemText(
            2, _translate("MainWindow", "Second User")
        )
        self.comboRecipientActive.setItemText(3, _translate("MainWindow", "Third Year"))
        self.labelSendToActive.setText(_translate("MainWindow", "Send To:"))
        self.buttonGoToArchive.setText(_translate("MainWindow", "Archived Messages"))
        self.buttonLogOut.setText(_translate("MainWindow", "Log Out"))
        self.labelTitleArchive.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">ARCHIVED MESSAGES</p></body></html>',
            )
        )
        self.buttonDeleteHistory.setText(_translate("MainWindow", "Delete History"))
        self.buttonGoToActiveChat.setText(_translate("MainWindow", "Back to Chat"))
        self.actionQuit.setText(_translate("MainWindow", "Refresh"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy Text"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Move Text"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste Text"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setStatusTip(
            _translate("MainWindow", "Refresh your Connection")
        )
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close the Application"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionArchives.setText(_translate("MainWindow", "Archives"))
        self.actionArchives.setStatusTip(_translate("MainWindow", "View Archives"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimize.setStatusTip(_translate("MainWindow", "Minimize this app"))


# Main window class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def closeEvent(self, event):
        # Ask for confirmation
        answer = QtWidgets.QMessageBox.question(self,
        "Confirm Exit...",
        "Are you sure you want to exit?\nAll data will be lost.",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        event.ignore()
        if answer == QtWidgets.QMessageBox.Yes:
            self.logout()
            event.accept()

# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())