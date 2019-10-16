from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON, JSONB
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Climate(Entity, Base):
    __tablename__ = 'CLIMATE'

    json                     = Column(JSONB, nullable=False)

    def __init__(self, json, created_by):
        Entity.__init__(self, created_by)
        self.json = json