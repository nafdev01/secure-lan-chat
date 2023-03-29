import sqlite3


class Logs:
    def submit_log(self, username, action):
        # connect to the database
        conn = sqlite3.connect("secure_chat.db")
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "INSERT INTO user_logs (username, action) VALUES (?, ?)",
            (username, action),
        )
        # commit the changes to the database
        conn.commit()
        # close the database connection
        conn.close()
