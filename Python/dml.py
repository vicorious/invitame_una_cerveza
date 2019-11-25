from entities.bar import Bar
from entities.beer import Beer
from entities.user import User
from entities.beer_type import BeerType

import datetime
class DML:

    def __init__(self):
        pass
    
    def createDML(self, session):
    
        beer_type = BeerType("IPA")
        pay_type = PayType("TARJETA_CREDITO")
        user = User("alejo.lindarte@outlook.com", datetime.datetime.utcnow, "Kasdasda76sshd6a3naksjda_asda", 
                        "100000", "http://servidor/foto.jpg", "0", 
                        "Alejo")
        bar = Bar("Melas", datetime.datetime.utcnow, "12", 
                    "24", "6", _json_entrada["payment_product"], 
                    "MELAS BAR", "http://imagen/assets/images/melas.jpg", "Calle 72 #11-07",
                    _json_entrada["points"], "https://facebook/melas", "https://twitter/@melas",
                    "https://instragram/melas", "123", "Alejo")
        beer = Beer("Atomic IIPA", 16000, 10000, 75000, 38000, 1 , 1, "10%", 
                        "82", "40", "Doble IIPA",
                        "http://imagen/assets/images/melas.jpg","1", "1",
                        "1", "1", "Alejo")
