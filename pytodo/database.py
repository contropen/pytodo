import sqlite3 #library for database

class DatabaseConnection:
 
    def __init__(self):
        self.con = sqlite3.connect("generated_data.db") 
        self.con.commit()
    def insert_data(self, portal_name, creation_date):
        self.creation_date = creation_date
        self.portal_name = portal_name
        self.con.commit()
    def delete_data(self, portal_name):
        self.portal_name = portal_name
        self.con.commit()
    def show_data(self, portal_name):
        self.portal_name = portal_name
        self.con.commit()
    def update_data(self,portal_name):
        self.portal_name = portal_name
        self.con.commit()
    def show_all_data(self):
        self.con.commit()
