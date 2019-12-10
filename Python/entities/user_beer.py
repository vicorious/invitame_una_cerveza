"""
BeerType entity
"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from entities.entity import Entity
from entities.beer import Beer
from entities.user import User
from entities.pay_type import PayType
from entities.climate import Climate
Base = declarative_base()

class UserBeer(Entity, Base):
    """
    UserBeer entity
    """
    __tablename__ = 'USER_BEER'
    __table_args__ = {"schema": "public"}
    beer_id = Column(Integer, ForeignKey(Beer.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    pay_type_id = Column(Integer, ForeignKey(PayType.id), nullable=False)
    climate_id = Column(Integer, ForeignKey(Climate.id), nullable=False)
    visit_date = Column(DateTime, nullable=False)
    _token = Column(String, nullable=False)
    payment_product = Column(String, nullable=False)
    qr = Column(String, nullable=False)
    def __init__(self, beer_id, user_id, pay_type_id, climate_id, v_date, _token, qr, created_by):
        """
        Constructor
        """
        Entity.__init__(self, created_by)
        self.beer_id = beer_id
        self.user_id = user_id
        self.pay_type_id = pay_type_id
        self.climate_id = climate_id
        self.visit_date = v_date
        self._token = _token
        self.payment_product = payment_product
        self.qr = qr
