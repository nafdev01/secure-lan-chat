import mariadb
import os

current_dir = os.getcwd()

# Set the database configuration parameters
# Set the database configuration parameters


class Message:
    def __init__(self):
        self.sender = None
        self.server_address = None
        self.config = None

    def initialize_server(self, server_address):
        self.server_address = server_address
        self.config = {
            "user": os.environ.get("DB_USER", "secure_admin"),
            "password": os.environ.get("DB_PASSWORD", "Annda8*j3s_Dje"),
            "host": server_address,
            "database": os.environ.get("DB_NAME", "secure_chat"),
            "port": int(os.environ.get("DB_PORT", 3306)),
        }

    def set_sender(self, username):
        self.sender = username

    def send_message(self, recipient, content):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # create a cursor object
        cursor = conn.cursor()
        # execute the update query
        cursor.execute(
            "INSERT INTO user_messages (sender, recipient, content) VALUES (%s, %s, %s)",
            (self.sender, recipient, content),
        )
        # commit the changes to the database
        conn.commit()
        # close the cursor
        cursor.close()
        conn.close()

    def reset(self):
        self.__init__()


class Archive:
    def __init__(self):
        self.username = None
        self.server_address = None
        self.config = None

    def initialize_server(self, server_address):
        self.server_address = server_address
        self.config = {
            "user": os.environ.get("DB_USER", "secure_admin"),
            "password": os.environ.get("DB_PASSWORD", "Annda8*j3s_Dje"),
            "host": server_address,
            "database": os.environ.get("DB_NAME", "secure_chat"),
            "port": int(os.environ.get("DB_PORT", 3306)),
        }

    def set_username(self, username):
        self.username = username

    def get_messages(self):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # Connect to the database
        cursor = conn.cursor()

        # Query the database for the user with the given username
        cursor.execute(
            "SELECT recipient, content FROM user_messages WHERE sender=?",
            (self.username,),
        )
        user = cursor.fetchall()

        cursor.close()
        conn.close()
        # If the user was found, return their details as a dictionary
        if user is not None:
            self.messages = user
            return self.messages
        else:
            return None

    def delete_messages(self):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # create a cursor object
        cursor = conn.cursor()
        # execute the update query
        query = "DELETE FROM user_messages WHERE sender = ?;"
        values = (self.username,)

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
