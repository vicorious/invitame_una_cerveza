"""
Climate entity
"""
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
Base = declarative_base()

class Climate(Entity, Base):
    """
    Climate class
    """
    __tablename__ = 'CLIMATE'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    json = Column(JSONB, nullable=False)
    def __init__(self, json, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.json = json
