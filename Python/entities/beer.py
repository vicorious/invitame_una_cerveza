from sqlalchemy import Column, String, Integer, ForeignKey
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Beer(Entity, Base):
    __tablename__ = 'BEER'

    name                     = Column(String, nullable=False)
    price                     = Column(Integer, nullable=False)
    happy_hour_price        = Column(Integer, nullable=False)
    bar_id                    = Column(Integer, ForeignKey('BAR.id'), nullable=False)
    beer_type_id            = Column(Integer, ForeignKey('BEER_TYPE.id'), nullable=False)
    avb                        = Column(String, nullable=False)
    ibu                        = Column(String, nullable=False)
    srm                        = Column(String, nullable=False)
    description                = Column(String, nullable=False)
    image                    = Column(String, nullable=False)
    pint                    = Column(String, nullable=False)
    cup330                    = Column(String, nullable=False)
    giraffe                    = Column(String, nullable=False)
    pitcher                    = Column(String, nullable=False)

    def __init__(self, title, price, happy_hour_price, bar_id, beer_type_id, avb, ibu, srm, description, image, pint, cup330, giraffe, pitcher, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.price = price
        self.happy_hour_price = happy_hour_price
        self.bar_id = bar_id
        self.beer_type_id = beer_type_id
        self.avb = avb
        self.ibu = ibu
        self.srm = srm
        self.description = description
        self.image = image
        self.pint = pint
        self.cup330 = cup330
        self.giraffe = giraffe
        self.pitcher = pitcher