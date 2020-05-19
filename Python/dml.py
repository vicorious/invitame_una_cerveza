"""
DataModelingLanguage module
"""
import json
import datetime
import logging
from entities.bar import Bar
from entities.beer import Beer
from entities.user import User
from entities.beer_type import BeerType
from entities.pay_type import PayType
from entities.pairing import Pairing
from entities.promotion import Promotion
from entities.taste import Taste
from entities.climate import Climate
from constant import Constant
from default_connection import DefaultConnection

class DML:
    """
    DataModelingLanguage class
    """
    default_connection = None
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    def __init__(self, engine):
        """
        Constructor
        """
        self.default_connection = DefaultConnection(engine)

    def create_dml(self):
        """
        Create datamodelinglanguage
        """
        logging.debug("DataModelingLanguage begin!")
        now = datetime.datetime(2009, 5, 5)
        now.strftime('%Y-%m-%d %H:%M:%S')
        _data = [1, [2, 3], {'a': [4, 5]}]
        _my_json = json.dumps(_data)
        logging.debug("dumps")
        beer_type = BeerType("IPA", Constant.user)
        pay_type = PayType("TARJETA_CREDITO", Constant.user)
        bar = Bar("Melas", now, "12", "24", "6", "a", "MELAS BAR", "http://servidor/melas.jpg",
                  "Calle 72 #11-07", "5", "https://facebook/melas", "https://twitter/@melas",
                  "https://instragram/melas", "123", Constant.user)
                  
        self.default_connection.get_beer_connection().session.add(beer_type)
        self.default_connection.get_beer_connection().session.add(pay_type)
        self.default_connection.get_beer_connection().session.add(bar)
        self.default_connection.get_beer_connection().session.flush()
        beer = Beer("Atomic IIPA", 16000, 10000, 75000, 38000, bar.id, beer_type.id,
                    "10%", "82", "40", "Doble IIPA",
                    "http://imagen/assets/images/dobleIIpa.jpg", "1", "1",
                    "1", "1", Constant.user)
        user = User("alejo.lindarte@outlook.com", now, "Kasdasda76sshd6a3naksjda_asda",
                    "100000", "http://servidor/foto.jpg", "0", Constant.user)
        self.default_connection.get_beer_connection().session.add(beer)
        self.default_connection.get_beer_connection().session.add(user)
        self.default_connection.get_beer_connection().session.flush()
        pairing = Pairing("Chorizo", "http://servidor/foto_pairing.jpg", beer.id, Constant.user)
        promotion = Promotion(8, beer.id, Constant.user)
        taste = Taste("taste", beer.id, Constant.user)
        climate = Climate(_my_json, Constant.user)
        self.default_connection.get_beer_connection().session.add(pairing)
        self.default_connection.get_beer_connection().session.add(promotion)
        self.default_connection.get_beer_connection().session.add(taste)
        self.default_connection.get_beer_connection().session.add(climate)
        self.default_connection.get_beer_connection().session.commit()
        self.default_connection.get_beer_connection().session.close()
        logging.debug("DataModelingLanguage created!")

    def __str__(self):
        return self.__class__.__name__
