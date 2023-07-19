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
    [(1)] -- Search a player to see their Grand Slam Results
    [(2)] -- Enter Tournament name to see the final four players
    [(3)] -- Search a Tounrament Round to which players were eliminated in that round
    [(4)] -- Add a New Tournament to the database
    [(5)] -- Update a Player's Ranking
    [(p)] -- See a list of all players in the database
    [(t)] -- See a list of the tournaments in the database
    [(r)] -- See a list of the possible tournament results a player can have
    [(x)] -- Return to main menu, or exit app from main menu
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
        if (select == '5'):
            update_ranking()
        if (select == 'p'):
            show_all_players()
        if (select == 't'):
            show_tournaments()
        if (select == 'r'):
            show_finish_options()
        select = click.prompt('Select Prompt')
    # if (select == 'x'):
    #     cli_start_menu()

    #     select = click.prompt('Select Prompt')

def search_by_player():
    player_name = click.prompt('\nEnter the Player\'s name you want to search for, or enter x to return to the main menu')

    if player_name == 'x':
        cli_start_menu()

    else:
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
    tournament_name = click.prompt('\n Enter the Tournament you want to search, or enter x to return to the main menu')

    if tournament_name == 'x':
        cli_start_menu()
    else:

        searched = (
                    session.query(Player.name, Player.gender, Player.ranking, Tournament.name.label('tournament_name'), Result.finish)
                    .join(Result, Player.id == Result.player_id)
                    .join(Tournament, Tournament.id == Result.tournament_id)
                    .filter(Tournament.name == tournament_name)
                    .filter(Result.finish != "First Round")
                    .filter(Result.finish != "Second Round")
                    .filter(Result.finish != "Third Round")
                    .filter(Result.finish != "Fourth Round")
                    .filter(Result.finish != "Quarters")
                    .filter(Result.finish != "DNP")
                    )

        table = PrettyTable()
        table.title = f'Final 4 Players at {tournament_name}'
        table.field_names = ['tournament_name', 'player_name', 'gender', 'finish', 'ranking']
        for player in searched:
            table.add_row([
                player.tournament_name,
                player.name,
                player.gender,
                player.finish,
                player.ranking
            ])
        print(table)

def search_by_finish():
    finish_name = click.prompt('\n Enter the Tournament Result you want to search, or enter x to return to the main menu')

    if finish_name == 'x':
        cli_start_menu()
    else:

        searched = (
                    session.query(Player.name, Player.gender, Player.ranking, Tournament.name.label('tournament_name'), Result.finish)
                    .join(Result, Player.id == Result.player_id)
                    .join(Tournament, Tournament.id == Result.tournament_id)
                    .filter(Result.finish == finish_name)
                    )

        table = PrettyTable()
        table.title = f'All Players who Finished in {finish_name}'
        table.field_names = ['tournament_name', 'player_name', 'gender', 'ranking', 'last_round_played']
        for player in searched:
            table.add_row([
                player.tournament_name,
                player.name,
                player.gender,
                player.ranking,
                player.finish
            ])
        print(table)

def add_new_tournament():
    pass

def update_ranking():
    player_to_update = click.prompt('\nEnter the name of the player whose ranking you want to update, or enter x to return to the main menu')
    if player_to_update == 'x':
        cli_start_menu()
    else:

        update_ranking = click.prompt(f'\nEnter the NEW ranking to assign to {player_to_update}, or enter x to return to the main menu')
        if update_ranking == 'x':
            cli_start_menu()
        else:

            session.query(Player).filter(Player.name == player_to_update).update({
                Player.ranking: f'{update_ranking}'
            })
            session.commit()
            print(f'{player_to_update}\'s ranking has been changed to {update_ranking}')

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
    cli_start_menu()

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
    cli_start_menu()

def show_finish_options():
    table = PrettyTable()
    options = ['First Round', 'Second Round', 'Third Round', 'Fourth Round', 'Quarters', 'Semis', 'Final', 'Winner', 'DNP']
    for i in options:
        print(i)
    cli_start_menu()
    