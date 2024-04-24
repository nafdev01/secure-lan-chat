import mariadb
from validation_backend import *
import os

current_dir = os.getcwd()


class Session:
    def __init__(self):
        self.server_address = None
        self.config = None
        self.username = None
        self.status = None
        self.active_users = None

    def check_database_accessibility(self):
        try:
            conn = mariadb.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            conn.close()
            return True
        except mariadb.Error as e:
            return False

    def initialize_tables_if_not_exists(self):
        try:
            conn = mariadb.connect(**self.config)
            cursor = conn.cursor()

            for query in [
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
            """,
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
            """,
                """
            CREATE TABLE IF NOT EXISTS  `user_logs` (
            `log_id` int(11) NOT NULL AUTO_INCREMENT,
            `user` varchar(255) NOT NULL,
            `action` text NOT NULL,
            PRIMARY KEY (`log_id`)
            )
            """,
                """
            CREATE TABLE IF NOT EXISTS `user_sessions` (
            `session_id` int(11) NOT NULL AUTO_INCREMENT,
            `username` varchar(255) NOT NULL,
            `status` enum('offline','online') NOT NULL DEFAULT 'offline',
            PRIMARY KEY (`session_id`),
            KEY `username` (`username`),
            CONSTRAINT `user_sessions_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
            )
            """,
            ]:
                cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            return True

        except mariadb.Error as e:
            print(f"Error while initializing database tables: {e}")
            return False

    def initialize_server(self, server_address):
        self.server_address = server_address
        self.config = {
            "user": os.environ.get("DB_USER", "secure_admin"),
            "password": os.environ.get("DB_PASSWORD", "Annda8*j3s_Dje"),
            "host": server_address,
            "database": os.environ.get("DB_NAME", "secure_chat"),
            "port": int(os.environ.get("DB_PORT", 3306)),
        }

    def set_online(self, username):
        self.status = "online"
        self.update_session(username, self.status)

    def set_username(self, username):
        self.username = username

    def set_offline(self):
        self.status = "offline"
        self.update_session(self.username, self.status)

    def start_session(self, username, status):
        self.username = username
        self.status = status
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # create a cursor object
        cursor = conn.cursor()
        # execute the update query
        cursor.execute(
            "INSERT INTO user_sessions (username, status) VALUES (%s, %s)",
            (username, status),
        )
        # commit the changes to the database
        conn.commit()
        # close the cursor
        cursor.close()

    def get_active_users(self):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        cursor = conn.cursor()
        # execute the select query to get the usernames of online users
        cursor.execute(
            "SELECT username FROM user_sessions WHERE status = ?;", ("online",)
        )
        # fetch the results
        results = cursor.fetchall()
        # create an array of usernames
        usernames = [result[0] for result in results]
        # assign the array of usernames to the class attribute
        self.active_users = usernames
        conn.commit()
        # close the cursor
        cursor.close()

    def update_session(self, username, status):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()

        # create a cursor object
        cursor = conn.cursor()
        # execute the update query
        cursor.execute(
            "UPDATE user_sessions SET status = ? WHERE username = ?;",
            (status, username),
        )
        # commit the changes to the database
        conn.commit()

        conn.commit()
        # close the cursor
        cursor.close()

    def reset(self):
        self.__init__()


class Log:
    def __init__(self) -> None:
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

    def submit_log(self, username, action):
        try:
            conn = mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
        # create a cursor object
        cursor = conn.cursor()
        # execute the update query
        cursor.execute(
            "INSERT INTO user_logs (user, action) VALUES (%s, %s)",
            (username, action),
        )
        # commit the changes to the database
        conn.commit()
        # close the cursor
        cursor.close()
