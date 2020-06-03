import click
from datetime import date
from beautifultable import BeautifulTable

from pytodo.database import DatabaseConnection

db_obj = DatabaseConnection()
table = BeautifulTable()
table.left_border_char = "|"
table.right_border_char = "|"
table.top_border_char = "="
table.header_separator_char = "="
table.column_headers = ["task_name_", "data", "date"]


@click.command(help="show all data")
def showall():
    show_all = db_obj.show_all_data()
    if show_all == []:
        print("Empty")
    for row in show_all:
        table.append_row([row[0], row[1], row[2]])
    print(table)
    
@click.command(help="add data")
def add():
    task_name = click.prompt("Enter the task name")

    data = click.prompt("Enter the data")
    creation_date = date.today()
    db_obj.insert_data(
        task_name=task_name,
        creation_date = creation_date,
        data=data,
    )    

@click.command(help="delete data")
def delete():
    task_name = click.prompt("Enter data name", default="None")
    value_check = db_obj.show_data(task_name)
    if value_check is None:
        print("No records found")
    else:
        db_obj.delete_data(task_name=task_name)

@click.command(help="update the data")
def update():
    task_name = click.prompt("Enter data name", default="None")
    mod_check = db_obj.show_data(task_name)
    if mod_check is None:
        print("No records found")
    else:
        mod = click.prompt("Enter new data", default="None", hide_input=True)
        db_obj.update_data(task_name=task_name, data=mod)

@click.command(help="save existing data")
def savedata():
    task_name = click.prompt("Enter task name",default='None')
    dta = click.prompt("Enter your data", default="None")
    creation_date = date.today()
    db_obj.insert_data(
        task_name=task_name,
        data=dta,
        creation_date=creation_date,
    )

@click.command(help="Show data")
def showdata():
    task_name = click.prompt("Enter task name", default="None")
    spass = db_obj.show_data(task_name)
    if spass is None:
        print("No records found")
    else:
        print(spass)
