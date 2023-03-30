
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from client import Client

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Client")
        self.setGeometry(100, 100, 400, 150)

        # Create widgets
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setText("student")
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        # Create layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.username_label)
        input_layout.addWidget(self.username_input)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.send_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Initialize client
        self.client = Client()

    def send_message(self):
        username = self.username_input.text()
        message = "Hello from {}".format(username)
        self.client.get_username(username)
        self.client.create_key_pairs()
        self.client.send_message(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
