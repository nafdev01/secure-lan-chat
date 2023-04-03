import hashlib
from validation_backend import *
import pyotp
import qrcode
import random
import string

import mariadb

# Set the database configuration parameters
config = {
    "user": "secure_admin",
    "password": "Annda8*j3s_Dje",
    "host": "192.168.241.103",
    "database": "secure_chat",
    "port": 3306,
    "ssl_ca": "/home/aegis/Code/team_project/cert/ca-cert.pem",
    "ssl_cert": "/home/aegis/Code/team_project/cert/client-cert.pem",
    "ssl_key": "/home/aegis/Code/team_project/cert/client-key.pem",
}


class SignUp:
    def __init__(self):
        self.username = None
        self.password = None
        self.confirm_password = None
        self.secret_key = None
        self.form_data = None
        self.hashed_password = None
        self.salt = self.generate_salt()
        self.VALIDATORS = [
            UserNameValidator,
            PasswordValidator,
            ConfirmPasswordValidator,
            SecretKeyValidator,
        ]
        self.errors = dict()
        self.is_valid = False

    def generate_salt(self):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(12))

    def process_form(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password,
            "secret_key": self.secret_key,
        }

    def validate_form(self):
        self.errors.clear()
        for validator_class in self.VALIDATORS:
            validator = validator_class(self.form_data)
            if not validator.is_valid():
                self.errors.update(validator.errors)

        if self.errors:
            # Handle validation errors
            self.is_valid = False
        else:
            # Process form data
            self.is_valid = True

    def generate(self, nickname):
        self.secret_key = pyotp.random_base32()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # The provisioning_uri is used to create the QR code
        provisioning_uri = pyotp.totp.TOTP(self.secret_key).provisioning_uri(
            name=f"{nickname}", issuer_name="Secure LAN Chat"
        )
        # Add the provisioning_uri data to the QR code object
        qr.add_data(provisioning_uri)
        qr.make(fit=True)
        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        return [img, self.secret_key]

    def get_user(self, username):
        try:
            conn = mariadb.connect(**config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return True
        else:
            return False

    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256(
            (self.password + self.salt).encode()
        ).hexdigest()
        return hashed_password

    def store_user_info(self):
        self.hashed_password = self.hash_password()
        try:
            conn = mariadb.connect(**config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        cursor = conn.cursor()

        query = "INSERT INTO users (username, password, salt, secret_key) VALUES (?, ?, ?, ?)"
        values = (self.username, self.hashed_password, self.salt, self.secret_key)

        try:
            cursor.execute(query, values)
            conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Error: {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def reset(self, username, password, confirm_password):
        self.__init__()
        username.setText("")
        password.setText("")
        confirm_password.setText("")


class LogIn:
    def __init__(self):
        self.username = None
        self.password = None
        self.db_password = None
        self.two_factor_code = None
        self.secret_key = None
        self.form_data = None
        self.errors = dict()
        self.is_valid = False
        self.user = None
        self.salt = None

    def process_form(self, username, password, two_factor_code):
        self.username = username
        self.password = password
        self.two_factor_code = two_factor_code

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "two_factor_code": self.two_factor_code,
        }

    def authenticate_2fa(self):
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

    def get_user(self):
        try:
            conn = mariadb.connect(**config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # Connect to the database
        cursor = conn.cursor()

        # Query the database for the user with the given username
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()
        # If the user was found, return their details as a dictionary
        if user is not None:
            self.username = user[1]
            self.db_password = user[2]
            self.salt = user[3]
            self.secret_key = user[4]
            return user
        else:
            return None

    def authenticate_user(self):
        authenticated = False
        user = self.get_user()
        if user:
            if self.hash_password() == self.db_password:
                tfa = self.authenticate_2fa()
                if tfa:
                    authenticated = True

        # If the user was not found, return None
        return authenticated

    def reset(self, username, password, two_factor_code):
        self.__init__()
        username.setText("")
        password.setText("")
        two_factor_code.setText("")


class Reset:
    def __init__(self):
        self.username = None
        self.password = None
        self.confirm_password = None
        self.secret_key = None
        self.form_data = None
        self.hashed_password = None
        self.two_factor_code = None
        self.salt = self.generate_salt()
        self.VALIDATORS = [
            UserNameValidator,
            PasswordValidator,
            ConfirmPasswordValidator,
            TwoFactorValidator,
        ]
        self.errors = dict()
        self.is_valid = False

    def generate_salt(self):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(12))

    def process_form(self, username, password, confirm_password, two_factor_code):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.two_factor_code = two_factor_code

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password,
            "two_factor_code": self.two_factor_code,
        }

    def validate_form(self):
        self.errors.clear()
        for validator_class in self.VALIDATORS:
            validator = validator_class(self.form_data)
            if not validator.is_valid():
                self.errors.update(validator.errors)

        if self.errors:
            # Handle validation errors
            self.is_valid = False
        else:
            # Process form data
            self.is_valid = True

    def get_user(self):
        try:
            conn = mariadb.connect(**config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # Connect to the database
        cursor = conn.cursor()

        # Query the database for the user with the given username
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()
        # If the user was found, return their details as a dictionary
        if user is not None:
            self.username = user[1]
            self.db_password = user[2]
            self.salt = user[3]
            self.secret_key = user[4]
            return user
        else:
            return None

    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256(
            (self.password + self.salt).encode()
        ).hexdigest()
        return hashed_password

    def store_user_info(self):
        self.hashed_password = self.hash_password()
        try:
            conn = mariadb.connect(**config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        cursor = conn.cursor()

        query = "UPDATE users SET password = ?, salt = ? WHERE username = ?"
        values = (self.hashed_password, self.salt, self.username)

        try:
            cursor.execute(query, values)
            conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Error: {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def authenticate_2fa(self):
        # Create the TOTP object
        totp = pyotp.TOTP(self.secret_key)
        # Verify the user's code
        if totp.verify(self.two_factor_code):
            return True
        else:
            return False

    def authenticate_user(self):
        authenticated = False
        user = self.get_user()
        if user:
            tfa = self.authenticate_2fa()
            if tfa:
                authenticated = True

        # If the user was not found, return None
        return authenticated

    def reset(self, username, password, confirm_password, two_factor_code):
        self.__init__()
        username.setText("")
        password.setText("")
        confirm_password.setText("")
        two_factor_code.setText("")
