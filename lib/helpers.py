import click
from db.models import Player, Tournament, Result, Base
from prettytable import PrettyTable
import time


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/tournament_results.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def cli_start_menu():
        print('''
    [(1)]   -- Search a player to see their Grand Slam Results
    [(2)]   -- Enter Tournament name to see the final four players
    [(3)]   -- Search a Tounrament Round to which players were eliminated in that round
    [(4)]   -- Add a NEW TOURNAMENT to the database
    [(5)]   -- Add a NEW PLAYER to the database
    [(6)]   -- Add a NEW RESULT to the database
    [(7)]   -- Update a Player's Ranking
    [(p)]   -- See a list of all players in the database
    [(t)]   -- See a list of the tournaments in the database
    [(r)]   -- See a list of the possible tournament results a player can have
    [(del)] -- Delete a record from the database
    [(x)]   -- Return to main menu, or exit app from main menu
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
            add_new_player()
        if (select == '6'):
            add_new_result()
        if (select == '7'):
            update_ranking()
        if (select == 'p'):
            show_all_players()
        if (select == 't'):
            show_tournaments()
        if (select == 'r'):
            show_finish_options()
        if (select == 'del'):
            cli_delete_menu()
        select = click.prompt('Select Prompt')

# search player name and see their results for each tournament
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
        time.sleep(1)
        print("\nWhen you are ready, try another search!")
        cli_start_menu()


#search by tournament name and see players who finisehd in semis, final or won the tournament
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
        time.sleep(1)
        print("\nWhen you are ready, try another search!")
        cli_start_menu()


# search round and receive list of players eliminated during that round
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
        time.sleep(1)
        print("\nWhen you are ready, try another search!")
        cli_start_menu()


# add a new tournament 
def add_new_tournament():
    print('''
    Thank you for improving our database by adding a new tournament! Please enter the tournament name when prompted below.
    Or enter x to return to the main menu.
    ''')
    time.sleep(3)

    enter_new_tournament = str(input('Enter the name of the Tournament you would like to add: '))
    if enter_new_tournament == 'x':
        cli_start_menu()
    else:

        new_tournament = Tournament(name= enter_new_tournament)

        session.add(new_tournament)
        # session.commit()

        time.sleep(3)
        print(f'\nThank you for adding the {enter_new_tournament} tournament to our database! What would you like to do next?')
        cli_start_menu()


# add a new player
def add_new_player():
    print('''
    Thank you for improving our database by adding a new player! Please enter the required info when prompted below.
    Or enter x at any time to return to the main menu.
    ''')
    time.sleep(3)

    new_player_name = str(input('Enter the NAME of the player you would like to add: '))
    if new_player_name == 'x':
        cli_start_menu()
    else:
        time.sleep(1)
        new_player_gender = str(input('Enter the player\'s GENDER. Must be male or female: '))
        if new_player_gender == 'x':
            cli_start_menu()
        else:
            time.sleep(1)
            new_player_ranking = click.prompt('\nEnter the player\'s current ranking as a number')
            if new_player_ranking == 'x':
                cli_start_menu()
            else:

                new_player = Player(name= new_player_name, gender= new_player_gender, ranking= new_player_ranking)
                session.add(new_player)
                session.commit()

                time.sleep(3)
                print(f'\n Thank you for adding {new_player_name} to our players database! What would you like to do next?')
                cli_start_menu()

def add_new_result():
    pass


# update the ranking of an existing player
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
    time.sleep(1)
    print("\nWhen you are ready, try another search!")
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
    time.sleep(1)
    print("\nWhen you are ready, try another search!")
    cli_start_menu()

def show_finish_options():
    table = PrettyTable()
    options = ['First Round', 'Second Round', 'Third Round', 'Fourth Round', 'Quarters', 'Semis', 'Final', 'Winner', 'DNP']
    for i in options:
        print(i)

    time.sleep(1)
    print("\nWhen you are ready, try another search!")
    cli_start_menu()
    

# delete records section

def cli_delete_menu():
    print('''
    [(del-p)]  -- Delete a Player Record
    [(del-t)]  -- Delete a Tournament Record
    [(del-r)]  -- Delete a Result record
    [(x)]      -- Return to  the main menu
    ''')

def cli_delete():
    select = ''
    cli_delete_menu()
    while select != 'x':
        if (select == 'del-p'):
            delete_player()
        if (select == 'del-t'):
            delete_tournament()
        if (select == 'del-r'):
            delete_result()
        select = click.prompt('Select Prompt')

def delete_player():
    pass

def delete_tournament():
    pass

def delete_result():
    pass