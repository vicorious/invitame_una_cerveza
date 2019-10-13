from sqlalchemy import Column, String, Integer
from .entity import Entity, Base

class Pairing(Entity, Base):
    __tablename__ = 'PAIRING'

    name                     = Column(String)
    image                     = Column(String)
    beer_id                     = Column(Integer, ForeignKey('BEER.id'))
    
    def __init__(self, name, image, beer_id, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.image = image
        self.beer_id = beer_id