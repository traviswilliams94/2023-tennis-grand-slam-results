from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename = 'players'

    id =  Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    ranking = Column(Integer())


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer(), primary_key=True)
    name = Column(String())


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    finish = Column(String())
    player_id = Column(Integer(), ForeignKey('players.id'))
    tournament_id = Column(Integer(), ForeignKey('tournaments.id'))