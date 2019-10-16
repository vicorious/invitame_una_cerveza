from sqlalchemy                 import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import JSON, JSONB
from default_connection import DefaultConnection

class DDL:

    metadata = None
    defaultConnection = None

    def dataDefinitionLanguage():
        user = Table('USER', metadata,
    Column('id', Integer, primary_key=True),
    Column('borning_date', DateTime, nullable=False),
    Column('password_token', String, nullable=False),
    Column('positive_balance', String, nullable=False),
    Column('photo', String, nullable=False),
    Column('credits', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #BeerType
        beer_type = Table('BEER_TYPE', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #PayType
        pay_type = Table('PAY_TYPE', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #UserBeer
        user_beer = Table('USER_BEER', metadata,
    Column('id', Integer, primary_key=True),
    Column('beer_id', Integer, ForeignKey('BEER.id'), nullable=False),
    Column('user_id', Integer, ForeignKey('USER.id'), nullable=False),
    Column('pay_type_id', Integer, ForeignKey('PAY_TYPE.id'), nullable=False),
    Column('climate_id', Integer, ForeignKey('CLIMATE.id'), nullable=False),
    Column('visit_date', DateTime, nullable=False),
    Column('_token', String, nullable=False),
    Column('payment_product', String, nullable=False),
    Column('qr', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Beer
        beer = Table('BEER', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('price', Integer, nullable=False),
    Column('happy_hour_price', Integer, nullable=False),
    Column('bar_id', Integer, ForeignKey('BAR.id'), nullable=False),
    Column('beer_type_id', Integer, ForeignKey('BEER_TYPE.id'), nullable=False),
    Column('avb', String, nullable=False),
    Column('ibu', String, nullable=False),
    Column('srm', String, nullable=False),
    Column('description', String, nullable=False),
    Column('image', String, nullable=False),
    Column('pint', String, nullable=False),
    Column('cup330', String, nullable=False),
    Column('giraffe', String, nullable=False),
    Column('pitcher', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Bar
        bar = Table('BAR', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('open_date', DateTime, nullable=False),
    Column('openinng_hour', String, nullable=False),
    Column('close_hour', String, nullable=False),
    Column('open_days', String, nullable=False),
    Column('payment_product', String, nullable=False),
    Column('description', String, nullable=False),
    Column('image', String, nullable=False),
    Column('address', String, nullable=False),
    Column('points', Integer, nullable=False),
    Column('facebook', String),
    Column('twitter', String),
    Column('instagram', DateTime),
    Column('emergency_number', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Pairing
        pairing = Table('PAIRING', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('image', String, nullable=False),
    Column('beer_id', Integer, ForeignKey('BEER.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Taste
        taste = Table('TASTE', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Climate
        climate = Table('CLIMATE', metadata,
    Column('id', Integer, primary_key=True),
    Column('json', JSONB, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))

    def __init__(self):
        self.metadata = MetaData()
        self.defaultConnection = DefaultConnection()
        self.metadata.create_all(self.defaultConnection.getBeerConnection().engine)
        print("DDL Created!")