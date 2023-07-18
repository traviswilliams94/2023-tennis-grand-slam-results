from db.models import Player, Tournament, Result
from prettytable import PrettyTable
from helpers.py import cli_start

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ = '__main__':
    print('''
    Welcom to the 2023 Tennis Grnad Slam Results Finder!
        ''')
        cli_start()