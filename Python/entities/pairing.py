from sqlalchemy import Column, String, Integer, ForeignKey
from entities.entity import Entity
from entities.beer import Beer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Pairing(Entity, Base):
    __tablename__ = 'PAIRING'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name                     = Column(String, nullable=False)
    image                     = Column(String, nullable=False)
    beer_id                 = Column(Integer, ForeignKey(Beer.id), nullable=False)
    def __init__(self, name, image, beer_id, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.image = image
        self.beer_id = beer_id