import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QPushButton,
    QVBoxLayout,
)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tab Widget Example")

        # Create a tab widget and add some tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(QWidget(), "Tab 1")
        self.tabs.addTab(QWidget(), "Tab 2")
        self.tabs.addTab(QWidget(), "Tab 3")

        # Create a button to change tabs
        self.button = QPushButton("Change Tab")
        self.button.clicked.connect(self.change_tab)

        # Create a layout and add the tab widget and button to it
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(self.button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_tab(self):
        # Increment the current index of the tab widget
        self.tabs.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
