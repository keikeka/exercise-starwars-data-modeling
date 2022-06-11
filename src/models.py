import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(40), nullable=False)
    favorites = relationship ("Favorite", backref="favers")

    def response(self):
        return f"User #{self.id}: {self.username}"

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)

    def response(self):
        return f"Planet #{self.id}: {self.name}"

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
   
    def response(self):
        return f"Character #{self.id}: {self.name}"

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    planet = Column(Integer, ForeignKey('planet.id'))
    character = Column(Integer, ForeignKey('character.id'))
    
    def response(self):
        return f"The user {self.user} marked {self.planet}{self.character} as favorite"

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')