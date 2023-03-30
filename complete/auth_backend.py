import sqlite3
import hashlib
from validation import *
import pyotp
import qrcode
import sqlite3
import random
import string

import mariadb

# Set the database configuration parameters
config = {
    "user": "secure_admin",
    "password": "Annda8*j3s_Dje",
    "host": "10.1.46.237",
    "database": "secure_chat",
    "port": 3306,
}

# Connect to the remote database server
try:
    conn = mariadb.connect(**config)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    exit()


def initialize_tables_if_not_exists():
    c = conn.cursor()
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS `users` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) DEFAULT NULL,
    `password` text DEFAULT NULL,
    `salt` text DEFAULT NULL,
    `secret_key` text DEFAULT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE KEY `username` (`username`)
    )
    """
    )
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS `user_messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(255) NOT NULL,
  `recipient` varchar(255) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`message_id`),
  KEY `sender` (`sender`),
  KEY `recipient` (`recipient`),
  CONSTRAINT `user_messages_ibfk_1` FOREIGN KEY (`sender`) REFERENCES `users` (`username`),
  CONSTRAINT `user_messages_ibfk_2` FOREIGN KEY (`recipient`) REFERENCES `users` (`username`)
)
    """
    )
    c.execute(
        """
         CREATE TABLE IF NOT EXISTS  `user_logs` (
            `log_id` int(11) NOT NULL AUTO_INCREMENT,
            `user` varchar(255) NOT NULL,
            `action` text NOT NULL,
            PRIMARY KEY (`log_id`),
            KEY `user` (`user`),
            CONSTRAINT `user_logs_ibfk_1` FOREIGN KEY (`user`) REFERENCES `users` (`username`)
)
    """
    )
    c.execute(
        """
     CREATE TABLE IF NOT EXISTS `user_sessions` (
  `session_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `status` enum('offline','online') NOT NULL DEFAULT 'offline',
  PRIMARY KEY (`session_id`),
  KEY `username` (`username`),
  CONSTRAINT `user_sessions_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
)
        """
    )
    c.close()
    conn.close()


class Session:
    def __init__(self):
        self.username = None
        self.status = None
        self.active_users = None

    def set_online(self, username):
        self.username = username
        self.status = "online"
        self.update_session(username, self.status)

    def set_offline(self):
        self.status = "offline"
        self.update_session(self.username, self.status)

    def get_active_users(self):
        # create a cursor object
        c = conn.cursor()
        # execute the select query to get the usernames of online users
        c.execute("SELECT username FROM user_sessions WHERE status = ?", ("online",))
        # fetch the results
        results = c.fetchall()
        # close the cursor
        c.close()
        # close the database connection
        conn.close()
        # create an array of usernames
        usernames = [result[0] for result in results]
        # return the array of usernames
        self.active_users = usernames

    def update_session(self, username, status):
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "UPDATE user_sessions SET status = ? WHERE username = ?", (status, username)
        )
        # commit the changes to the database
        conn.commit()
        # close the database connection
        conn.close()

    def reset(self):
        self.__init__()


class Log:
    def submit_log(self, username, action):
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "INSERT INTO user_logs (username, action) VALUES (%s, %s)",
            (username, action),
        )
        # commit the changes to the database
        conn.commit()
        # close the cursor
        c.close()


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
        c = conn.cursor()
        c.execute("SELECT username FROM users WHERE username=?", (username,))
        user = c.fetchone()
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
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (username, password, salt, secret_key) VALUES (?, ?, ?, ?)",
            (
                self.username,
                self.hashed_password,
                self.salt,
                self.secret_key,
            ),
        )
        c.execute(
            "INSERT INTO user_sessions (username, status) VALUES (?, ?)",
            (self.username, "offline"),
        )
        conn.commit()
        conn.close()
        return "User information stored successfully"

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
        # Connect to the database
        c = conn.cursor()

        # Query the database for the user with the given username
        c.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = c.fetchone()

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
