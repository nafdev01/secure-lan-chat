import hashlib
import sqlite3
import re


class User:
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
        self.salt = self.generate_salt()
        self.hashed_password = self.hash_password()

    def generate_salt(self):
        # Generate salt by concatenating username, email and truncating rsulting string
        salt = self.username + self.email + self.password
        return salt[:5]
    
    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256((self.password + self.salt).encode()).hexdigest()
        return hashed_password
    
    def store_user_info(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (username text, email text, salt text, password text)''')
        c.execute("INSERT INTO users (username, email, salt, password) VALUES (?, ?, ?, ?)", 
                  (self.username, self.email, self.salt, self.hashed_password))
        conn.commit()
        conn.close()
        return "User information stored successfully"
    
class Authenticate:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.exists = self.get_user()

    def get_user(self):
        conn = sqlite3.connect('users.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT username FROM users WHERE username=?", (self.username,))
        user = c.fetchone()
        if user:
            return True
        else:
            return False
        conn.close()
    
    def check_password(self, user_password, db_password):
        if user_password == db_password:
            return True

    def authenticate(self):
        if self.exists:
            conn = sqlite3.connect('users.db')
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username=?", (self.username,))
            user = c.fetchone()
            user_password = hashlib.sha256((self.password + user['salt']).encode()).hexdigest()
            if self.check_password(user_password, user["password"]):
                print(f"User authenticated successfully")
                return True
            else:
                print("something went wrong")
            conn.close()
            
        
    