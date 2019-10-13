from sqlalchemy import Column, String
from .entity import Entity, Base

class Taste(Entity, Base):
    __tablename__ = 'TASTE'

    name                     = Column(String)
    beer_id                  = Column(Integer, ForeignKey('BEER.id'))
    
    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name