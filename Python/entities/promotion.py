"""
Promotion entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from entities.beer import Beer
from entities.entity import Entity
Base = declarative_base()

class Promotion(Entity, Base):
    """
    Promotion class
    """
    __tablename__ = 'PROMOTION'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    beer_id = Column(Integer, ForeignKey(Beer.id), nullable=False)
    def __init__(self, beer_id, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.beer_id = beer_id