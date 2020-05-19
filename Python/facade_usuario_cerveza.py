"""
User Beer module
"""
import json
import logging
from entities.user_beer import UserBeer
from cursor import Cursor

class UserBeerFacade:
    """
    User beer facade
    """
    cursor = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ####### Constructor ############
    def __init__(self):
        """
        Constructor
        """
        self.cursor = Cursor()

 ############ User for visit ####################################################
    def user_for_visit(self, _json):
        """
        user for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.cursor.default_connection.get_beer_connection().session.query(UserBeer).filter(
                UserBeer.id == _json_entrada["id"])
            return UserBeer.serialize_many(results)
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

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
            self.cursor.default_connection.get_beer_connection().session.add(user_beer)
            self.cursor.default_connection.get_beer_connection().session.commit()
            self.cursor.default_connection.get_beer_connection().session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add UserByVisit: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

 ############ Update beer for visit ####################################################
    def user_beer_for_visit(self, _json):
        """
        get cursor
        """
        try:
            _json_entrada = json.loads(_json)
            result = self.cursor.default_connection.get_beer_connection().session.query(UserBeer).filter(
                UserBeer.user_id == _json_entrada["user_id"],
                UserBeer.beer_id == _json_entrada["beer_id"])
            return UserBeer.serialize_many(result)
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

 ############ getUserBeerForPayment ####################################################
    def user_beer_pay_type_for_visit(self, _json):
        """
        User beer pay type for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.cursor.default_connection.get_beer_connection().session.query(UserBeer).filter(
                UserBeer.user_id == _json_entrada["user_id"],
                UserBeer.beer_id == _json_entrada["beer_id"],
                UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return UserBeer.serialize_many(results)
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

 ############ getUserPayType ####################################################
    def user_pay_type_for_visit(self, _json):
        """
        User pay type for visit method
        """
        try:
            _json_entrada = json.loads(_json)
            results = self.cursor.default_connection.get_beer_connection().session.query(UserBeer).filter(
                UserBeer.user_id == _json_entrada["user_id"],
                UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return UserBeer.serialize_many(results)
        except Exception as _excep:
            logging.debug('Exception: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()
