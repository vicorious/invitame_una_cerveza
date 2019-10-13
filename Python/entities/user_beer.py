from sqlalchemy import Column, String, Integer, DateTime
from .entity import Entity, Base

class UserBeer(Entity, Base):
    __tablename__ = 'USER_BEER'

    beer_id                 = Column(Integer, ForeignKey('BEER.id'))
    user_id                 = Column(Integer, ForeignKey('USER.id'))
    pay_type_id                = Column(Integer, ForeignKey('PAY_TYPE.id'))
    climate_id                = Column(Integer, ForeignKey('CLIMATE.id'))
    visit_date                = Column(DateTime)
    _token                    = Column(String)    
    payment_product            = Column(String)
    qr                        = Column(String)

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