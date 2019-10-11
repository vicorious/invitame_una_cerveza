from sqlalchemy import Column, String
from .entity import Entity, Base

class PayType(Entity, Base):
    __tablename__ = 'PAY_TYPE'

    name                     = Column(String)
    
    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name