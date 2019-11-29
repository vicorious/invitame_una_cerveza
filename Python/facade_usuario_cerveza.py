import json
import logging
from default_connection import DefaultConnection
from entities.user_beer import UserBeer
from proxy import ProxyConfiguration

class UserBeerFacade:

    default_connection = None
    beer_connection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ####### Constructor ############
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        try:
            #Conexion a postgre
            self.default_connection = DefaultConnection(self.proxy.engine)
            self.beer_connection = self.defaultConnection.get_beer_connection()
        except Exception as exception:
            logging.debug('Error getting "UserBeerFacade" cursor %s', exception)
            raise Exception('Error no controlado: {}'.format(exception.args[0]))
        finally:
            pass

 ############ User for visit ####################################################
    def user_for_visit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.id == _json_entrada["id"])
            return results
        except Exception as exception:
            logging.debug('Exception: %s"', exception)
        finally:
            self.beer_connection.session.close()

    ########### Insert User for visit #################################################
    def insert_user_for_visit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            user_beer = UserBeer(_json_entrada["beer_id"], _json_entrada["user_id"], _json_entrada["pay_type_id"], _json_entrada["climate_id"], _json_entrada["visit_date"], _json_entrada["_token"], _json_entrada["qr"], _json_entrada["created_by"])
            self.beer_connection.session.add(user_beer)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try add UserByVisit: %s"', exception)
        finally:            
            self.beer_connection.session.close()
            
 ############ Update beer for visit ####################################################
    def user_beer_for_visit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"])
            return results
        except Exception as exception:
            logging.debug('Exception: %s"', exception)
        finally:
            self.beer_connection.session.close()

 ############ getUserBeerForPayment ####################################################
    def user_beer_pay_type_for_visit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as exception:
            logging.debug('Exception: %s"', exception)
        finally:
            self.beer_connection.session.close()

 ############ getUserPayType ####################################################
    def user_pay_type_for_visit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as exception:
            logging.debug('Exception: %s"', exception)
        finally:
            self.beer_connection.session.close()