import sqlite3
import datetime

currentDateTime = datetime.datetime.now()
today_date = currentDateTime.strftime('%d-%m-%Y')
print(today_date)


class Database:
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

    def update_data(self, id, title, description):
        self.cur.execute("UPDATE notes SET title = ?, description = ? WHERE id = ?",
                         (title, description,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


