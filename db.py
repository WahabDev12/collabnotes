import sqlite3
import datetime

currentDateTime = datetime.datetime.now() # Gets the current datetime
today_date = currentDateTime.strftime('%d-%m-%Y') # Returns only month,year and day
print(today_date)


class Database:
    '''A database to create a table for the notes, select data for action like delete, update, and insert'''
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title text, description text, date text)")
        self.conn.commit()

    def fetch_data(self):
        self.cur.execute("SELECT * FROM notes")
        rows = self.cur.fetchall()
        return rows

    def insert_data(self, title, description, date_created = today_date):
        self.cur.execute("INSERT INTO notes VALUES (NULL, ?, ?, ?)",
                         (title, description,date_created))
        self.conn.commit()

    def delete_data(self, id):
        self.cur.execute("DELETE FROM notes WHERE id=?", (id,))
        self.conn.commit()

    def update_data(self, id, title, description,date = today_date):
        self.cur.execute("UPDATE notes SET title = ?, description = ?, date = ? WHERE id = ?",
                         (title, description,date,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


