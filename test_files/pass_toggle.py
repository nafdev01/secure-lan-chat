from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class PasswordToggle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Toggle")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 400, 200)
        
        layout = QVBoxLayout()
        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Enter Password")
        self.password_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_field)
        
        self.show_password_checkbox = QCheckBox("Show Password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password)
        layout.addWidget(self.show_password_checkbox)
        
        self.setLayout(layout)
    
    def toggle_password(self, state):
        if state == Qt.Checked:
            self.password_field.setEchoMode(QLineEdit.Normal)
        else:
            self.password_field.setEchoMode(QLineEdit.Password)

if __name__ == '__main__':
    app = QApplication([])
    toggle_password = PasswordToggle()
    toggle_password.show()
    app.exec_()
