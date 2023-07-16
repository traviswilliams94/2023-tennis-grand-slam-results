from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename = 'players'

    id =  Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    ranking = Column(Integer())

    def __repr__(self):
        return f"ID: {self.id}, " \
            + f"Name: {self.name}," \
            + f"Gender: {self.gender}," \
            + f"Ranking: {self.ranking}"

class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"Tournament: {self.name}"

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    player = Column(String())
    tournament = Column(String())
    finish = Column(String())
    player_id = Column(Integer(), ForeignKey('players.id'))
    tournament_id = Column(Integer(), ForeignKey('tournaments.id'))