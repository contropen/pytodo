import sqlite3 #library for database

class DatabaseConnection:
 
    def __init__(self):
        self.con = sqlite3.connect("generated_todo.db") 
        self.cursor_obj = self.con.cursor()
        self.cursor_obj.execute(
            """CREATE TABLE IF NOT EXISTS data(
            task_name text NOT NULL UNIQUE, 
            creation_date varchar, task varchar)
            """
        )
        self.con.commit()

    def insert_data(self, task_name, data, creation_date):
        self.creation_date = creation_date
        self.task_name = task_name
        self.data = data
        self.cursor_obj.execute(
            """INSERT INTO data
            (task_name, data, creation_date)
            VALUES (?, ?, ?)""",
            (self.task_name, self.data, self.creation_date),
        )
        self.con.commit()

    def delete_data(self, task_name):
        self.task_name = task_name
        self.cursor_obj.execute(
            """DELETE from data where task_name = ?""", (self.task_name,)
        )
        self.con.commit()

    def show_data(self, task_name):
        self.task_name = task_name
        self.cursor_obj.execute(
            """SELECT data FROM datas WHERE task_name=?""", (self.task_name,)
        )
        rows = self.cursor_obj.fetchall()

        for row in rows:
            return row[0]
    
        self.con.commit()

    def update_data(self,task_name):
        self.task_name = task_name
        self.cursor_obj.execute(
            """UPDATE data  =? WHERE task_name =?""",
            (self.data, self.task_name),
        )
        self.con.commit()

    def show_all_data(self):
        self.cursor_obj.execute("""SELECT * FROM data""")
        rows = self.cursor_obj.fetchall()
        return rows
        self.con.commit()
