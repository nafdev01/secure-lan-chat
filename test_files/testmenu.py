# Import necessary modules from PyQt5 library
from PyQt5 import QtCore, QtGui, QtWidgets


# Define the main UI class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set up the main window object
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 387)

        # Create a central widget for the window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a label widget and set its properties
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Set the central widget of the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Create a menu bar for the window
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 24))
        self.menubar.setObjectName("menubar")

        # Create two menus for the menu bar
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        # Add the menus to the menu bar
        MainWindow.setMenuBar(self.menubar)

        # Create a status bar for the window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # add the status bar to the window
        MainWindow.setStatusBar(self.statusbar)

        # Create four actions for the menus
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        # Add the actions to the menus
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        # Set up translations for the UI elements
        self.retranslateUi(MainWindow)

        # Connect the signals and slots of the UI elements
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the 'triggered' signal of each QAction object to a lambda function that takes a string argument.
        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))

    # Define a method to set up translations for the UI elements
    def retranslateUi(self, MainWindow):
        # Create a reference to the QtCore.translate method and assign it to the variable _translate
        _translate = QtCore.QCoreApplication.translate

        # Use _translate to set the window title to "MainWindow"
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Use _translate to set the label text to "TextLabel"
        self.label.setText(_translate("MainWindow", "TextLabel"))

        # Use _translate to set the menu title to "File"
        self.menuFile.setTitle(_translate("MainWindow", "File"))

        # Use _translate to set the menu title to "Edit"
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))

        # Use _translate to set the action text to "New", status tip to "Create a new file", and shortcut to "Ctrl+N"
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

        # Use _translate to set the action text to "Save", status tip to "Save this file", and shortcut to "Ctrl+S"
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save this file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

        # Use _translate to set the action text to "Copy", status tip to "Copy", and shortcut to "Ctrl+C"
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))

        # Use _translate to set the action text to "Paste", status tip to "Paste", and shortcut to "Ctrl+V"
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))

    # define a clicked fucntion that is called when an action is triggerred
    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys

    # Create a QApplication object with the command line arguments passed to the script
    app = QtWidgets.QApplication(sys.argv)

    # Create a QMainWindow object and assign it to the variable MainWindow
    MainWindow = QtWidgets.QMainWindow()

    # Create a Ui_MainWindow object and assign it to the variable ui
    ui = Ui_MainWindow()

    # Call the setupUi method of ui and pass MainWindow as an argument
    ui.setupUi(MainWindow)

    # Call the show method of MainWindow to display the window
    MainWindow.show()
    # Execute the event loop of the application
    sys.exit(app.exec_())
