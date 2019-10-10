from sqlalchemy import Column, JSONB
from .entity import Entity, Base

class Climate(Entity, Base):
    __tablename__ = 'CLIMATE'

    json 					= Column(JSONB)	

    def __init__(self, json, created_by):
        Entity.__init__(self, created_by)
        self.json = json