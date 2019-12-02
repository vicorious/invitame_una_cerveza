"""
Pay type entity
"""
from sqlalchemy import Column, String, Integer
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class PayType(Entity, Base):
    """
    PayType class
    """
    __tablename__ = 'PAY_TYPE'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)    
    def __init__(self, name, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name