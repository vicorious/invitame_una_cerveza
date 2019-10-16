from sqlalchemy import Column, String
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class PayType(Entity, Base):
    __tablename__ = 'PAY_TYPE'

    name                     = Column(String, nullable=False)
    
    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name