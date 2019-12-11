"""
BeerType Entity
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
Base = declarative_base()
class BeerType(Entity, Base):
    """
    BeerType class
    """
    __tablename__ = 'BEER_TYPE'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    def __init__(self, name, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.created_by))
