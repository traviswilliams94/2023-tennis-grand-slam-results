import ipdb 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Player, Tournament, Result

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/tournament_results.db')
    Session = sessionmaker(bind=engine)
    session = Session()