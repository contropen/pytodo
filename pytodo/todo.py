import click
from datetime import date

from pytodo.database import DatabaseConnection

db_obj = DatabaseConnection()

@click.command(help="show all data")
def showall():
    show_all = db_obj.show_all_data()
    if show_all == []:
        print("Empty")
    
@click.command(help="add data")
def add():
    portal_name = click.prompt("Enter the portal name")
    portal_name = click.prompt("Enter data")
    creation_date = date.today()
    db_obj.insert_data(
        portal_name=portal_name,
        creation_date = creation_date,
    )    

@click.command(help="delete data")
def delete():
    portal_name = click.prompt("Enter data name", default="None")
    value_check = db_obj.show_data(portal_name)
    if value_check is None:
        print("No records found")
    else:
        db_obj.delete_data(portal_name=portal_name)

@click.command(help="update the data")
def update():
    portal_name = click.prompt("Enter data name", default="None")
    mod_check = db_obj.show_data(portal_name)
    if mod_check is None:
        print("No records found")
    else:
        mod = click.prompt("Enter new data", default="None", hide_input=True)
        db_obj.update_data(portal_name=portal_name, data=mod)

@click.command(help="save existing data")
def savedata():
    portal_name = click.prompt("Enter portal name",default='None')
    creation_date = date.today()
    db_obj.insert_data(
        portal_name=portal_name,
        creation_date=creation_date,
    )

@click.command(help="Show data")
def showdata():
    portal_name = click.prompt("Enter portal name", default="None")
    spass = db_obj.show_data(portal_name)
    if spass is None:
        print("No records found")
    else:
        print(spass)
