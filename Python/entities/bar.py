from sqlalchemy import Column, String, Integer, DateTime
from .entity import Entity, Base

class Bar(Entity, Base):
    __tablename__ = 'BAR'

    name 					= Column(String)
    open_date 				= Column(DateTime)
	openinng_hour			= Column(String)
	close_hour				= Column(String)
	open_days				= Column(String)
	payment_product			= Column(String)
	description				= Column(String)
	image					= Column(String)
	address					= Column(String)
	points					= Column(Integer)
	facebook				= Column(String)
	twitter					= Column(String)
	instagram				= Column(String)
	emergency_number		= Column(String)

    def __init__(self, title, open_date, openinng_hour, close_hour, open_days, payment_product, description, image, address, points, facebook, twitter, instagram, emergency_number, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.open_date = open_date
		self.openinng_hour = openinng_hour
		self.close_hour = close_hour
		self.open_days = open_days
		self.payment_product = payment_product
		self.description = description
		self.image = image
		self.description = description
		self.image = image
		self.address = address
		self.points = points
		self.facebook = facebook
		self.twitter = twitter
		self.instagram = instagram
		self.emergency_number = emergency_number