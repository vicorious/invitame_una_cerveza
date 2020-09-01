"""
Beer entity
"""
from sqlalchemy import Column, String, Integer, ForeignKey
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
                 image, pint, cup330, giraffe, pitcher, created_by, id=None):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.id = id
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

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.name, self.pint_price, self.cup330_price,
                     self.giraffe_price, self.pitcher_price,
                     self.bar_id, self.beer_type_id, self.avb,
                     self.ibu, self.srm,
                     self.description, self.image,
                     self.pint, self.cup330,
                     self.giraffe, self.pitcher))
                     
    def serialize(self, is_me: bool = False):
        return dict(id=self.id,
                    name=self.name,
                    pint_price=self.pint_price,
                    cup330_price=self.cup330_price,
                    giraffe_price=self.giraffe_price,
                    pitcher_price=self.pitcher_price,
                    bar_id=self.bar_id,
                    beer_type_id=self.beer_type_id,
                    avb=self.avb,
                    ibu=self.ibu,
                    srm=self.srm,
                    description=self.description,
                    image=self.image,
                    pint= self.pint,
                    cup330= self.cup330,
                    giraffe= self.giraffe,
                    pitcher= self.pitcher) 

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'pint_price', self.pint_price
        yield 'cup330_price', self.cup330_price 
        yield 'giraffe_price', self.giraffe_price 
        yield 'pitcher_price', self.pitcher_price 
        yield 'bar_id', self.bar_id 
        yield 'beer_type_id', self.beer_type_id 
        yield 'avb', self.avb 
        yield 'ibu', self.ibu 
        yield 'srm', self.srm 
        yield 'description', self.description
        yield 'image', self.image
        yield 'pint', self.pint
        yield 'cup330', self.cup330
        yield 'giraffe', self.giraffe
        yield 'pitcher', self.pitcher
