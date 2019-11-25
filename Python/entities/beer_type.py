from sqlalchemy import Column, String, Integer
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BeerType(Entity, Base):
    __tablename__ = 'BEER_TYPE'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name                     = Column(String, nullable=False)
    
    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name