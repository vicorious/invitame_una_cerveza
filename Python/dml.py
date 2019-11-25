from entities.bar import Bar
from entities.beer import Beer
from entities.user import User
from entities.beer_type import BeerType
from entities.pairing import Pairing
from entities.promotion import Promotion
from entities.taste import Taste
from entities.climate import Climate
from constant import Constant
import json

import datetime
class DML:

    def __init__(self):
        pass
    
    def createDML(self, session):
    
        beer_type = BeerType("IPA", Constant.user)
        pay_type = PayType("TARJETA_CREDITO", Constant.user)
        promotion = Promotion(1, Constant.user)
        taste = Taste("taste", Constant.user)
        
        _data = [1, [2,3], {'a': [4,5]}]
        _my_json = json.dumps(_data)
        climate = Climate(_my_json, Constant.user)
        
        user = User("alejo.lindarte@outlook.com", datetime.datetime.utcnow, "Kasdasda76sshd6a3naksjda_asda", 
                        "100000", "http://servidor/foto.jpg", "0", 
                        Constant.user)
        bar = Bar("Melas", datetime.datetime.utcnow, "12", 
                    "24", "6", _json_entrada["payment_product"], 
                    "MELAS BAR", "http://servidor/melas.jpg", "Calle 72 #11-07",
                    _json_entrada["points"], "https://facebook/melas", "https://twitter/@melas",
                    "https://instragram/melas", "123", Constant.user)
        beer = Beer("Atomic IIPA", 16000, 10000, 75000, 38000, 1 , 1, "10%", 
                        "82", "40", "Doble IIPA",
                        "http://imagen/assets/images/dobleIIpa.jpg","1", "1",
                        "1", "1", Constant.user)
        pairing = Pairing("Chorizo", "http://servidor/foto_pairing.jpg", 1, Constant.user)
        session.add(beer_type)
        session.add(pay_type)
        session.add(pairing)
        session.add(promotion)
        session.add(taste)
        session.add(climate)
        session.add(user)
        session.add(bar)
        session.add(beer)
        session.commit()
        session.close() 
