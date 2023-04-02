import mariadb

# Set the database configuration parameters
config = {
    "user": "secure_admin",
    "password": "Annda8*j3s_Dje",
    "host": "192.168.177.103",
    "database": "secure_chat",
    "port": 3306,
    "ssl_ca": "/home/aegis/Code/team_project/cert/ca-cert.pem",
    "ssl_cert": "/home/aegis/Code/team_project/cert/client-cert.pem",
    "ssl_key": "/home/aegis/Code/team_project/cert/client-key.pem",
}


class Message:
    def __init__(self):
        self.sender = None

    def set_sender(self, username):
        self.sender = username

    def send_message(self, recipient, content):
        try:
            conn = mariadb.connect(**config)
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

    def set_username(self, username):
        self.username = username

    def get_messages(self):
        try:
            conn = mariadb.connect(**config)
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
            conn = mariadb.connect(**config)
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
