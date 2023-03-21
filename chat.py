import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QTextOption
from PyQt5.QtCore import Qt


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Secure Chat Application")
        self.setGeometry(100, 100, 800, 600)

        # Create chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setAlignment(Qt.AlignRight)

        # Create message input box
        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(50)

        # Create send message button
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.chat_display)
        layout.addWidget(self.message_input)

        # Create horizontal layout for send button
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.send_button)
        button_layout.addStretch(1)

        layout.addLayout(button_layout)

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def send_message(self):
        # Get message from input box
        message = self.message_input.toPlainText()

        # Clear input box
        self.message_input.clear()

        # Add message to chat display
        self.chat_display.append("User: " + message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
