from sqlalchemy import Column, String, DateTime
from .entity import Entity, Base

class User(Entity, Base):
    __tablename__ = 'USER'

    mail 					= Column(String)
    borning_date 			= Column(DateTime)
	password_token			= Column(String)
	positive_balance		= Column(String)
	photo					= Column(String)
	credits					= Column(String)	

    def __init__(self, mail, borning_date, password_token, positive_balance, photo, credits, created_by):
        Entity.__init__(self, created_by)
        self.mail = mail
        self.borning_date = borning_date
		self.password_token = password_token
		self.positive_balance = positive_balance
		self.photo = photo
		self.credits = credits