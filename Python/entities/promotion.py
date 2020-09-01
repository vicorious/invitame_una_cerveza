"""
Promotion entity
"""
from sqlalchemy import Column, Integer, ForeignKey
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
    duration = Column(Integer, nullable=False)
    beer_id = Column(Integer, ForeignKey(Beer.id), nullable=False)

    def __init__(self, id=None, duration, beer_id, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.id = id
        self.beer_id = beer_id
        self.duration = duration

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.duration))

    def serialize(self, is_me: bool = False):
        return dict(id=self.id, 
                    duration=self.duration,                   
                    beer_id=self.beer_id)

    def __iter__(self):
        yield 'id', self.id
        yield 'duration', self.duration
        yield 'beer_id', self.beer_id

