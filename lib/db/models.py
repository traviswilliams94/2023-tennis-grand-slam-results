from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
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
    tournament_name = Column(String())

    def __repr__(self):
        return f"Tournament: {self.name}"

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    player_id = Column(Integer(), ForeignKey('players.id'))
    tournament_id = Column(Integer(), ForeignKey('tournaments.id'))
    finish = Column(String())

    player = relationship('Player', backref=backref("players"))
    tournament = relationship('Tournament', backref=backref("tournaments"))

    def __repr__(self):
        return f"{self.id}," \
            + f"Player Id: {self.player_id}," \
            + f"Tournament ID: {self.tournament_id}," \
            + f"Finish: {self.finish}"