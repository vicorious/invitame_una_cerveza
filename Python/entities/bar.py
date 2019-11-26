from sqlalchemy import Column, String, Integer, DateTime
from entities.entity import Entity
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Bar(Entity, Base):
    __tablename__ = 'BAR'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name                     = Column(String, nullable=False)
    open_date                 = Column(DateTime, nullable=False)
    openinng_hour            = Column(String, nullable=False)
    close_hour                = Column(String, nullable=False)
    open_days                = Column(String, nullable=False)
    payment_product            = Column(String, nullable=False)
    description                = Column(String, nullable=False)
    image                    = Column(String, nullable=False)
    address                    = Column(String, nullable=False)
    points                    = Column(Integer, nullable=False)
    facebook                = Column(String)
    twitter                    = Column(String)
    instagram                = Column(String)
    emergency_number        = Column(String, nullable=False)

    def __init__(self, name, open_date, openinng_hour, close_hour, open_days, payment_product, description, image, address, points, facebook, twitter, instagram, emergency_number, created_by):
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