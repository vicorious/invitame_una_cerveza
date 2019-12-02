"""
Pairing entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
from entities.beer import Beer
Base = declarative_base()

class Pairing(Entity, Base):
    """
    Pairing class
    """
    __tablename__ = 'PAIRING'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    beer_id = Column(Integer, ForeignKey(Beer.id), nullable=False)
    def __init__(self, name, image, beer_id, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name
        self.image = image
        self.beer_id = beer_id