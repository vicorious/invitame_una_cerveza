from sqlalchemy import Column, String, Integer, ForeignKey
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Promotion(Entity, Base):
    __tablename__ = 'PROMOTION'
    id = Column(Integer, primary_key=True, autoincrement=True)
    beer_id            = Column(Integer, ForeignKey('BEER.id'), nullable=False)

    def __init__(self, beer_id, created_by):
        Entity.__init__(self, created_by)
        self.beer_id = beer_id