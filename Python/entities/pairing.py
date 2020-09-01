"""
Pairing entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
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
    def __init__(self, name, image, beer_id, created_by, id=None):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name
        self.image = image
        self.beer_id = beer_id

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.image, self.beer_id))

    def serialize(self, is_me: bool = False):
        return dict(id=self.id, 
                    name=self.name,  
                    image=self.image,                 
                    beer_id=self.beer_id)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'image', self.image
        yield 'beer_id', self.beer_id

