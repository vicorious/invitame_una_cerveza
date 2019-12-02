"""
Beer entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
from entities.beer_type import BeerType
from entities.bar import Bar
Base = declarative_base()

class Beer(Entity, Base):
    """
    Beer class
    """
    __tablename__ = 'BEER'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    pint_price = Column(Integer, nullable=False)
    cup330_price = Column(Integer, nullable=False)
    giraffe_price = Column(Integer, nullable=False)
    pitcher_price = Column(Integer, nullable=False)
    bar_id = Column(Integer, ForeignKey(Bar.id), nullable=False)
    beer_type_id = Column(Integer, ForeignKey(BeerType.id), nullable=False)
    avb = Column(String, nullable=False)
    ibu = Column(String, nullable=False)
    srm = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    pint = Column(String, nullable=False)
    cup330 = Column(String, nullable=False)
    giraffe = Column(String, nullable=False)
    pitcher = Column(String, nullable=False)

    def __init__(self, name, pint_price, cup330_price, giraffe_price, pitcher_price,
                 bar_id, beer_type_id, avb, ibu, srm, description,
                 image, pint, cup330, giraffe, pitcher, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.name = name
        self.pint_price = pint_price
        self.cup330_price = cup330_price
        self.giraffe_price = giraffe_price
        self.pitcher_price = pitcher_price
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
