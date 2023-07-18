import click
from db.models import Player, Tournament, Result, Base
from prettytable import PrettyTable


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/tournament_results.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def cli_start_menu():
        print('''
    [Player      (1)] -- Search for results by Player Name
    [Tournmament (2)] -- Enter Tournament name to see the final four players
    [Finish      (3)] -- See which players have achieved a certain tournement finish
    [New Tourny  (4)] -- Add a New Tournament
    [All Players (p)] -- See a list of all players in the database
    [All Trnmts  (t)] -- See a list of the tournaments in the database
    [Finishes    (f)] -- See a list of the possible finishes
        ''')

def cli_start():
    select = ''
    cli_start_menu()
    while select != 'x':
        if (select == '1'):
            search_by_player()
        if (select == '2'):
            search_by_tournament()
        if (select == '3'):
            search_by_finish()
        if (select == '4'):
            add_new_tournament()
        if (select == 'p'):
            show_all_players()
        if (select == 't'):
            show_tournaments()
        if (select == 'f'):
            show_finish_options()
        select = click.prompt('Select Prompt')
    # if (select == 'x'):
    #     cli_start_menu()

    #     select = click.prompt('Select Prompt')

def search_by_player():
    player_name = click.prompt('\nEnter the Player\'s name you want to search for')

    searched = (
                session.query(Player.name, Tournament.name.label('tournament_name'), Result.finish)
                .join(Result, Player.id == Result.player_id)
                .join(Tournament, Tournament.id == Result.tournament_id)
                .filter(Player.name == player_name)
                )

    table = PrettyTable()
    table.title = f'Results for {player_name}'
    table.field_names = ['player_name', 'tournament', 'finish']
    for player in searched:
        table.add_row([
            player.name,
            player.tournament_name,
            player.finish
        ])
    print(table)


    


def search_by_tournament():
    tournament_name = click.prompt('\n Enter the Tournament you want to search')

    table = PrettyTable()
    table.title = f'Final 4 Players at {tournament_name}'
    table.field_names = ['player_name', "finish"]

        # table.add_row([
        #     player.name,
        #     result.finish
        # ])
    print(table)

def search_by_finish():
    pass

def add_new_tournament():
    pass

def show_all_players():
    table = PrettyTable()
    players = session.query(Player).all()
    table.title = "All Players"
    table.field_names = ['id', 'name', 'gender', 'ranking']
    for player in players:
        table.add_row([
            player.id,
            player.name,
            player.gender,
            player.ranking
        ])
    print(table)

def show_tournaments():
    table = PrettyTable()
    tournaments = session.query(Tournament).all()
    table.title = "All Tournaments"
    table.field_names = ['id', 'name']
    for t in tournaments:
        table.add_row([
            t.id,
            t.name
        ])
    print(table)

def show_finish_options():
    table = PrettyTable()
    options = ['First Round', 'Second Round', 'Third Round', 'Fourth Round', 'Quarters', 'Semis', 'Final', 'Winner', 'DNP']
    for i in options:
        print(i)