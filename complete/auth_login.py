import hashlib
import sqlite3
import pyotp


class LogIn:
    def __init__(self):
        self.username = None
        self.password = None
        self.two_factor_code = None
        self.secret_key = None
        self.form_data = None
        self.errors = dict()
        self.is_valid = False
        self.user = None

    def process_form(self, username, password, two_factor_code):
        self.username = username
        self.password = password
        self.two_factor_code = two_factor_code

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "two_factor_code": self.two_factor_code,
        }

    def authenticate(self):
        # Create the TOTP object
        totp = pyotp.TOTP(self.secret_key)
        # Verify the user's code
        if totp.verify(self.two_factor_code):
            return True
        else:
            return False

    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256(
            (self.password + self.salt).encode()
        ).hexdigest()
        return hashed_password

    def get_user(self, username):
        # Connect to the database
        conn = sqlite3.connect("secure_chat.db")
        c = conn.cursor()

        # Query the database for the user with the given username
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        # If the user was found, return their details as a dictionary
        if user is not None:
            self.username = user[1]
            self.password = user[2]
            self.salt = user[3]
            self.secret_key = user[4]
            return True
        # If the user was not found, return None
        else:
            return None

    def authenticate_user(self):
        user = self.get_user("")
        if not user:
            self.errors["username"] = "Invalid username or password"
            return False
        hashed_password = hashlib.sha256(
            (self.password + user["salt"]).encode()
        ).hexdigest()
        if hashed_password != user["password"]:
            self.errors["username"] = "Invalid username or password"
            return False
        self.user = user
        return True

    def reset(self, username, password, two_factor_code):
        self.__init__()
        username.setText("")
        password.setText("")
        two_factor_code.setText("")
