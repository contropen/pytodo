import sqlite3 #library for database

class DatabaseConnection:
 
    def __init__(self):
        self.con = sqlite3.connect("generated_todo.db") 
        self.cursor_obj = self.con.cursor()
        self.cursor_obj.execute(
            """CREATE TABLE IF NOT EXISTS data(
            id integer PRIMARY KEY,task TEXT NOT NULL UNIQUE,
            creation_date varchar)
            """
        )
        self.con.commit()

    def insert_data(self, task, creation_date):
        self.creation_date = creation_date
        self.task = task
        self.cursor_obj.execute(
            """INSERT OR IGNORE INTO data
            (task, creation_date)
            VALUES (?, ?)""",
            (self.task, self.creation_date),
        )
        self.con.commit()

    def delete_data(self, task):
        self.task = task
        self.cursor_obj.execute(
            """DELETE from datas where task = ?""", (self.task,)
        )
        self.con.commit()

    def show_data(self, task):
        self.task = task
        self.cursor_obj.execute(
            """SELECT data FROM datas WHERE task=?""", (self.task,)
        )
        rows = self.cursor_obj.fetchall()

        for row in rows:
            return row[0]
    
        self.con.commit()

    def update_data(self,task):
        self.task = task
        self.cursor_obj.execute(
            """UPDATE datas SET data  =? WHERE task =?""",
            (self.data, self.task),
        )
        self.con.commit()

    def show_all_data(self):
        self.cursor_obj.execute("""SELECT * FROM data""")
        rows = self.cursor_obj.fetchall()
        return rows
        self.con.commit()
