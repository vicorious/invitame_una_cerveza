"""
Promotion entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
from entities.beer import Beer
Base = declarative_base()

class Taste(Entity, Base):
    """
    Taste entity
    """
    __tablename__ = 'TASTE'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    beer_id = Column(Integer, ForeignKey(Beer.id), nullable=False)
    def __init__(self, name, beer_id, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name
        self.beer_id = beer_id

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.beer_id))
