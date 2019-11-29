import json
import datetime
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

    defaultConnection = None
    def __init__(self, engine):
        self.defaultConnection = DefaultConnection(engine)
    
    def create_dml(self):
        now = datetime.datetime(2009, 5, 5)
        now.strftime('%Y-%m-%d %H:%M:%S')        
        _data = [1, [2,3], {'a': [4,5]}]
        _my_json = json.dumps(_data)
        beer_type = BeerType("IPA", Constant.user)
        pay_type = PayType("TARJETA_CREDITO", Constant.user)
        bar = Bar("Melas", now, "12", "24", "6", "a", "MELAS BAR", "http://servidor/melas.jpg", "Calle 72 #11-07", "5", "https://facebook/melas", "https://twitter/@melas", "https://instragram/melas", "123", Constant.user)
        self.defaultConnection.getBeerConnection().session.add(beer_type)
        self.defaultConnection.getBeerConnection().session.add(pay_type)
        self.defaultConnection.getBeerConnection().session.add(bar)
        self.defaultConnection.getBeerConnection().session.flush()
        beer = Beer("Atomic IIPA", 16000, 10000, 75000, 38000, bar.id , beer_type.id, "10%", "82", "40", "Doble IIPA", "http://imagen/assets/images/dobleIIpa.jpg", "1", "1", "1", "1", Constant.user)
        user = User("alejo.lindarte@outlook.com", now, "Kasdasda76sshd6a3naksjda_asda", "100000", "http://servidor/foto.jpg", "0", Constant.user)
        self.defaultConnection.getBeerConnection().session.add(beer)
        self.defaultConnection.getBeerConnection().session.add(user)
        self.defaultConnection.getBeerConnection().session.flush()
        pairing = Pairing("Chorizo", "http://servidor/foto_pairing.jpg", beer.id, Constant.user)
        promotion = Promotion(beer.id, Constant.user)
        taste = Taste("taste", beer.id, Constant.user)
        climate = Climate(_my_json, Constant.user)
        self.defaultConnection.getBeerConnection().session.add(pairing)
        self.defaultConnection.getBeerConnection().session.add(promotion)
        self.defaultConnection.getBeerConnection().session.add(taste)
        self.defaultConnection.getBeerConnection().session.add(climate)
        self.defaultConnection.getBeerConnection().session.commit()
        self.defaultConnection.getBeerConnection().session.close() 
