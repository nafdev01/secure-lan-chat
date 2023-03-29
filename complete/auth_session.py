import sqlite3


class Session:
    def __init__(self):
        self.username = None
        self.status = None

    def set_online(self, username):
        self.username = username
        self.status = "online"
        self.update_session(username, self.status)

    def set_offline(self):
        self.status = "offline"
        self.update_session(self.username, self.status)

    def update_session(self, username, status):
        # connect to the database
        conn = sqlite3.connect("secure_chat.db")
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
        self.reset

    def reset(self):
        self.__init__()
