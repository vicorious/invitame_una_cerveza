from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from entities.entity import Entity
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class UserBeer(Entity, Base):
    __tablename__ = 'USER_BEER'

    beer_id                 = Column(Integer, ForeignKey('BEER.id'), nullable=False)
    user_id                 = Column(Integer, ForeignKey('USER.id'), nullable=False)
    pay_type_id                = Column(Integer, ForeignKey('PAY_TYPE.id'), nullable=False)
    climate_id                = Column(Integer, ForeignKey('CLIMATE.id'), nullable=False)
    visit_date                = Column(DateTime, nullable=False)
    _token                    = Column(String, nullable=False)    
    payment_product            = Column(String, nullable=False)
    qr                        = Column(String, nullable=False)

    def __init__(self, beer_id, user_id, pay_type_id, climate_id, visit_date, _token, qr, created_by):
        Entity.__init__(self, created_by)
        self.beer_id = beer_id
        self.user_id = user_id
        self.pay_type_id = pay_type_id
        self.climate_id = climate_id
        self.visit_date = visit_date
        self._token = _token
        self.payment_product = payment_product
        self.qr = qr