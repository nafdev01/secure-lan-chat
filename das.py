from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize UI elements
        self.setWindowTitle('Chat')
        self.setGeometry(100, 100, 600, 400)

    def closeEvent(self, event):
        # Display a confirmation message box
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # If the user confirms, close the window
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication([])
    chat_window = ChatWindow()
    chat_window.show()
    app.exec_()
