import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minimize Example')

        # Create a button to minimize the window
        self.button = QPushButton('Minimize', self)
        self.button.clicked.connect(self.minimize)

    def minimize(self):
        # Minimize the window
        self.showMinimized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
