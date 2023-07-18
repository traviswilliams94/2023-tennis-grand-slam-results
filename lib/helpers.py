from db.models import Player, Tournament, Result
from prettytable import PrettyTable
import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/tournament_results.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def cli_start_menu():
        print('''
    [Player  (a)] -- Search for results by Player
    [Tournmament  (b)] -- Search by  Tournament
    [Finish  (c)] -- See which players have achieved a certain tournement finish
    [New Tourny (d)] -- Add a New Tournament
    [exit (e)] -- Exit
        ''')

def cli_start():
    select = ''
    cli_start_menu()
    while select != 'e':
        if (select == 'a'):
            search_by_player()
        if (select == 'b'):
            search_by_tournament()
        if (select == 'c'):
            search_by_finish()
        if (select == 'd'):
            add_new_tournament()

    select = click.prompt('Select Prompt')

def search_by_player():
    pass 

def search_by_tournament():
    pass

def search_by_finish():
    pass

def add_new_tournament():
    pass