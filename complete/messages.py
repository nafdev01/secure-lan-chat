import sqlite3

class Message:
    def __init__(self):
        self.sender = None
    
    def set_sender(self, username):
        self.sender = username
    
    def send_message(self, recipient, content):
        # connect to the database
        conn = sqlite3.connect("secure_chat.db")
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "INSERT INTO user_messages (sender, recipient, content) VALUES (?, ?, ?)",
            (self.sender, recipient, content),
        )
        # commit the changes to the database
        conn.commit()
        # close the database connection
        conn.close()


    
    def reset(self):
        self.__init__()

        