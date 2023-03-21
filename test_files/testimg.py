# Import necessary modules from PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


# Define the user interface class
class Ui_MainWindow(object):
    # Define the setupUi function to create and initialize the main window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a label widget to display an image
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(60, 20, 561, 321))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("img/metro.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("label")

        # Create a button to show metro
        self.showMetro = QtWidgets.QPushButton(self.centralwidget)
        self.showMetro.setGeometry(QtCore.QRect(160, 390, 171, 41))
        self.showMetro.setObjectName("showMetro")

        # Create a button to show wharf
        self.showWharf = QtWidgets.QPushButton(self.centralwidget)
        self.showWharf.setGeometry(QtCore.QRect(390, 390, 181, 41))
        self.showWharf.setObjectName("showWharf")

        # Set the central widget of the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Create a menu bar for the main window
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 24))
        self.menubar.setObjectName("menubar")

        # Set the menu bar of the main window
        MainWindow.setMenuBar(self.menubar)

        # Create a status bar for the main window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # Set the status bar of the main window
        MainWindow.setStatusBar(self.statusbar)

        # Call the retranslateUi function to set the text and labels of the widgets
        self.retranslateUi(MainWindow)

        # Connect signals to slots using the QMetaObject class
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the "clicked" signal of the "showWharf" button to the "show_wharf" function
        self.showWharf.clicked.connect(self.show_wharf)
        # Connect the "clicked" signal of the "showMetro" button to the "show_metro" function
        self.showMetro.clicked.connect(self.show_metro)

    # Define the retranslateUi function to set the text and labels of the widgets
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showMetro.setText(_translate("MainWindow", "Metro"))
        self.showWharf.setText(_translate("MainWindow", "Wharf"))

    # Define the "show_metro" function to display a picture of the metro
    def show_metro(self):
        self.photo.setPixmap(QtGui.QPixmap("img/metro.jpg"))

    # Define the "show_wharf" function to display a picture of the wharf
    def show_wharf(self):
        self.photo.setPixmap(QtGui.QPixmap("img/wharf.jpg"))


# Define the main function
if __name__ == "__main__":
    import sys

    # Create a QApplication instance
    app = QtWidgets.QApplication(sys.argv)

    # Create a QMainWindow instance
    MainWindow = QtWidgets.QMainWindow()

    # Create a Ui_MainWindow instance and set up the user interface
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Show the main window
    MainWindow.show()

    # Run the application and exit when finished
    sys.exit(app.exec_())
