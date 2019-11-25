from sqlalchemy import Column, String, Integer, ForeignKey
from entities.entity import Entity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Taste(Entity, Base):
    __tablename__ = 'TASTE'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name                     = Column(String, nullable=False)
    beer_id                  = Column(Integer, ForeignKey('BEER.id'), nullable=False)
    def __init__(self, name, beer_id, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.beer_id = beer_id