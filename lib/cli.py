from db.models import Player, Tournament, Result
from helpers import cli_start

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    print('''
    Welcome to the 2023 Tennis Grand Slam Results Finder!

                      ___________
                     /|_|_|_|_|_|\ 
                    /_|_|_|_|_|_|_\ 
                   /|_|_|_|_|_|_|_|\ 
                  |_|_|_|_|_|_|_|_|_|           <-- it's a tennis racquet okay. just go with it
                  |_|_|_|_|_|_|_|_|_|
                   \|_|_|_|_|_|_|_|/
                    \_|_|_|_|_|_|_/
                     \|_|_|_|_|_|/  
                          |_| 
                          |_|
                          |_|
                          |_|
                          |_|


        ''')
    cli_start()
    # cli_delete()