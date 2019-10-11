from sqlalchemy import Column, String, Integer
from .entity import Entity, Base

class Beer(Entity, Base):
    __tablename__ = 'BEER'

    name                     = Column(String)
    price                     = Column(Integer)
    happy_hour_price        = Column(Integer)
    bar_id                    = Column(Integer, ForeignKey('BAR.id'))
    beer_type_id            = Column(Integer)
    avb                        = Column(String)
    ibu                        = Column(String)
    srm                        = Column(String)
    description                = Column(String)
    image                    = Column(String)
    pint                    = Column(String)
    cup330                    = Column(String)
    giraffe                    = Column(String)
    pitcher                    = Column(String)

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