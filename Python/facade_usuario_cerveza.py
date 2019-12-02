"""
User Beer module
"""
import json
import logging
from default_connection import DefaultConnection
from entities.user_beer import UserBeer
from proxy import ProxyConfiguration

class UserBeerFacade:
    """
    User beer facade
    """
    default_connection = None
    beer_connection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ####### Constructor ############
    def __init__(self):
        """
        Constructor
        """
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        """
        get cursor method
        """
        try:
            self.default_connection = DefaultConnection(self.proxy.engine)
            self.beer_connection = self.default_connection.get_beer_connection()
        except Exception as _excep:
            logging.debug('Error getting "UserBeerFacade" cursor %s', _excep)
            raise Exception('Error no controlado: {}'.format(_excep.args[0]))
        finally:
            pass

 ############ User for visit ####################################################
    def user_for_visit(self, _json):
        """
        user for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(
                UserBeer.id == _json_entrada["id"])
            return results
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.beer_connection.session.close()

    ########### Insert User for visit #################################################
    def insert_user_for_visit(self, _json):
        """
        insert user for visit
        """
        try:
            _json_entrada = json.loads(_json)
            user_beer = UserBeer(_json_entrada["beer_id"], _json_entrada["user_id"],
                                 _json_entrada["pay_type_id"], _json_entrada["climate_id"],
                                 _json_entrada["visit_date"], _json_entrada["_token"],
                                 _json_entrada["qr"], _json_entrada["created_by"])
            self.beer_connection.session.add(user_beer)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add UserByVisit: %s"', _excep)
        finally:
            self.beer_connection.session.close()

 ############ Update beer for visit ####################################################
    def user_beer_for_visit(self, _json):
        """
        get cursor
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"])
            return results
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.beer_connection.session.close()

 ############ getUserBeerForPayment ####################################################
    def user_beer_pay_type_for_visit(self, _json):
        """
        User beer pay type for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.beer_connection.session.close()

 ############ getUserPayType ####################################################
    def user_pay_type_for_visit(self, _json):
        """
        User pay type for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.beer_connection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.beer_connection.session.close()
