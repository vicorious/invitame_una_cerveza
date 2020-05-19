"""
Bar entity
"""
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
from entities.beer import Beer
Base = declarative_base()

class Bar(Entity, Base):
    """
    Bar class
    """
    __tablename__ = 'BAR'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    open_date = Column(DateTime, nullable=False)
    opening_hour = Column(String, nullable=False)
    close_hour = Column(String, nullable=False)
    open_days = Column(String, nullable=False)
    payment_product = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    address = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
    facebook = Column(String)
    twitter = Column(String)
    instagram = Column(String)
    emergency_number = Column(String, nullable=False)

    def __init__(self, name, open_date, opening_hour, close_hour, open_days,
                 payment_product, description, image, address, points, facebook,
                 twitter, instagram, emergency_number, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name
        self.open_date = open_date
        self.opening_hour = opening_hour
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

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.open_date, self.opening_hour,
                     self.close_hour, self.open_days,
                     self.payment_product, self.description, self.image,
                     self.address, self.points,
                     self.facebook, self.twitter,
                     self.instagram, self.emergency_number))

    def serialize(self, is_me: bool = False):
        return dict(id=self.id,
                    name=self.name,
                    open_date=self.open_date,
                    close_hour=self.close_hour,
                    open_days=self.open_days,
                    payment_product=self.payment_product,
                    description=self.description,
                    image=self.image,
                    address=self.address,
                    points=self.points,
                    facebook=self.facebook,
                    twitter=self.twitter,
                    instagram=self.instagram,
                    emergency_number= self.emergency_number)                    
        
