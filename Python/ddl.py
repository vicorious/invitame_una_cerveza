from sqlalchemy import Column, String, Integer, DateTime, MetaData, Table, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import JSONB

class DDL:
    metadata = None
    def __init__(self):
        self.metadata = MetaData()

    def data_definition_language(self, engine):
    #UserBeer
        Table('USER_BEER', self.metadata,
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
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('_token', name='_token_unique_user_beer_constraint'),
    UniqueConstraint('qr', name='qr_unique_user_beer_constraint'))
        Table('USER', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('borning_date', DateTime, nullable=False),
    Column('email', String, nullable=False),
    Column('password_token', String, nullable=False),
    Column('positive_balance', String, nullable=False),
    Column('photo', String, nullable=False),
    Column('credits', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('email', name='email_unique_user_constraint'),
    UniqueConstraint('password_token', name='password_token_unique_user_constraint'),
    UniqueConstraint('photo', name='photo_unique_user_constraint'))
    #BeerType
        Table('BEER_TYPE', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('name', name='name_unique_beer_type_constraint'))
    #PayType
        Table('PAY_TYPE', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('name', name='name_unique_pay_type_constraint'))
    #Beer
        Table('BEER', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('pint_price', Integer, nullable=False),
    Column('cup330_price', Integer, nullable=False),
    Column('giraffe_price', Integer, nullable=False),
    Column('pitcher_price', Integer, nullable=False),
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
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('name', name='name_unique_beer_constraint'),
    UniqueConstraint('image', name='image_unique_beer_constraint'))
    #Bar
        Table('BAR', self.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('open_date', DateTime, nullable=False),
    Column('opening_hour', Integer, nullable=False),
    Column('close_hour', Integer, nullable=False),
    Column('open_days', Integer, nullable=False),
    Column('payment_product', String, nullable=False),
    Column('description', String, nullable=False),
    Column('image', String, nullable=False),
    Column('address', String, nullable=False),
    Column('points', Integer, nullable=False),
    Column('facebook', String),
    Column('twitter', String),
    Column('instagram', String),
    Column('emergency_number', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('image', name='image_unique_bar_constraint'),
    UniqueConstraint('address', name='address_unique_bar_constraint'),
    UniqueConstraint('facebook', name='facebook_unique_bar_constraint'),
    UniqueConstraint('twitter', name='twitter_unique_bar_constraint'),
    UniqueConstraint('instagram', name='instagram_unique_bar_constraint'),
    CheckConstraint('opening_hour >= 0', name='chk_opening_zero'),
    CheckConstraint('opening_hour <= 24', name='chk_opening_closed'),
    CheckConstraint('open_days > 0', name='chk_open_days_zero'),
    CheckConstraint('open_days <= 7', name='chk_open_days_closed'),
    CheckConstraint('close_hour >= 0', name='chk_close_hour_zero'),
    CheckConstraint('close_hour <= 24', name='chk_close_hour_closed'))
    #Pairing
        Table('PAIRING', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('image', String, nullable=False),
    Column('beer_id', Integer, ForeignKey('BEER.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('image', name='image_unique_pairing_constraint'),
    UniqueConstraint('name', name='name_unique_pairing_constraint'))
    #Taste
        Table('TASTE', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('beer_id', Integer, ForeignKey('BEER.id'), nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False),
    UniqueConstraint('name', name='name_unique_taste_constraint'))
    #Climate
        Table('CLIMATE', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('json', JSONB, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
    #Promotion
        Table('PROMOTION', self.metadata,
    Column('id', Integer, primary_key=True),
    Column('beer_id', Integer, ForeignKey('BEER.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('last_updated_by', String, nullable=False))
        self.metadata.create_all(engine)
        