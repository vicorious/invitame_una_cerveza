from sqlalchemy import Column, String, ForeignKey
from entities.entity import Entity
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Taste(Entity, Base):
    __tablename__ = 'TASTE'

    name                     = Column(String, nullable=False)
    beer_id                  = Column(Integer, ForeignKey('BEER.id'), nullable=False)
    user_beers = relationship("Beer", back_populates = "TASTE")
    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name