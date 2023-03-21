import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 400, 300)

        # Create labels and text fields
        username_label = QLabel("Username:")
        self.username_text = QLineEdit()

        password_label = QLabel("Password:")
        self.password_text = QLineEdit()
        self.password_text.setEchoMode(QLineEdit.Password)

        # Create buttons
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.show_signup_page)

        # Create layouts
        form_layout = QFormLayout()
        form_layout.addRow(username_label, self.username_text)
        form_layout.addRow(password_label, self.password_text)

        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(signup_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        # Set layout
        self.setLayout(main_layout)

    def login(self):
        # Get username and password from text fields
        username = self.username_text.text()
        password = self.password_text.text()

        # Perform login logic here

    def show_signup_page(self):
        # Hide the login page and show the signup page
        self.hide()
        signup_page.show()

class SignupPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Signup Page")
        self.setGeometry(100, 100, 400, 300)

        # Create labels and text fields
        username_label = QLabel("Username:")
        self.username_text = QLineEdit()

        password_label = QLabel("Password:")
        self.password_text = QLineEdit()
        self.password_text.setEchoMode(QLineEdit.Password)

        confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_text = QLineEdit()
        self.confirm_password_text.setEchoMode(QLineEdit.Password)

        # Create buttons
        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.signup)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.show_login_page)

        # Create layouts
        form_layout = QFormLayout()
        form_layout.addRow(username_label, self.username_text)
        form_layout.addRow(password_label, self.password_text)
        form_layout.addRow(confirm_password_label, self.confirm_password_text)

        button_layout = QHBoxLayout()
        button_layout.addWidget(signup_button)
        button_layout.addWidget(login_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        # Set layout
        self.setLayout(main_layout)

    def signup(self):
        # Get username, password, and confirmation password from text fields
        username = self.username_text.text()
        password = self.password_text.text()
        confirm_password = self.confirm_password_text.text()

        # Perform signup logic here

    def show_login_page(self):
        # Hide the signup page and show the login page
        self.hide()
        login_page.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    signup_page = SignupPage()
    login_page.show()
    sys.exit(app.exec_())
