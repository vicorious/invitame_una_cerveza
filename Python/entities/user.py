"""
User entity
"""
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
Base = declarative_base()

class User(Entity, Base):
    """
    User class
    """
    __tablename__ = 'USER'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    borning_date = Column(DateTime, nullable=False)
    password_token = Column(String, nullable=False)
    positive_balance = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    credits = Column(String, nullable=False)
    def __init__(self, email, borning_date, password_token, po_balance, photo, credits, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.email = email
        self.borning_date = borning_date
        self.password_token = password_token
        self.positive_balance = po_balance
        self.photo = photo
        self.credits = credits
