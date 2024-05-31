from flask import g
import sqlite3

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS usermessage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  message TEXT,
  email TEXT
);
"""


def get_database():
    if not hasattr(g, 'userdata_db'):
        g.userdata_db = connect_to_database()
        with g.userdata_db as connection:  # Ensure connection is closed properly
            cursor = connection.cursor()
            try:
                cursor.execute(CREATE_USERS_TABLE)
                connection.commit()  # Commit changes to persist the table
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")  # Log any errors
    return g.userdata_db  # Return the connection object stored in g


def connect_to_database():
    sql = sqlite3.connect('userdata.db')
    sql.row_factory = sqlite3.Row
    return sql