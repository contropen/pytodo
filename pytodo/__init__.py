import click

from pytodo.todo import showall
from pytodo.todo import add
from pytodo.todo import savedata
from pytodo.todo import delete
from pytodo.todo import update
from pytodo.todo import showdata




@click.group()
def main():
    pass


main.add_command(showall)
main.add_command(add)
main.add_command(savedata)
main.add_command(showdata)
main.add_command(delete)
main.add_command(update)
   
if __name__ == "__main__":
    main()
