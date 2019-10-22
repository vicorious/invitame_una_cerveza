from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import datetime
import logging
import time
from entities.user_beer import UserBeer
from proxy                  import ProxyConfiguration

class UserBeerFacade:
    
    defaultConnection = None
    beerConnection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ####### Constructor ############
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.getCursor()        

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection        = DefaultConnection(self.proxy.engine)
            self.beerConnection = self.defaultConnection.getBeerConnection()   
        except Exception as e:
            logging.debug('Error getting "UserBeerFacade" cursor')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

 ############ User for visit ####################################################
    def userForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.id == _json_entrada["id"])            
            return results
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            self.beerConnection.session.close()

    ########### Insert User for visit #################################################
    def insertUserForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            user_beer = UserBeer(_json_entrada["beer_id"], _json_entrada["user_id"], _json_entrada["pay_type_id"], 
                        _json_entrada["climate_id"], _json_entrada["visit_date"], _json_entrada["_token"], 
                        _json_entrada["qr"], _json_entrada["created_by"])
            self.beerConnection.session.add(user_beer)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try add UserByVisit: {}"'.format(ex))
        finally:            
            self.beerConnection.session.close()
            
 ############ Update beer for visit ####################################################
    def userBeerForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"])
            return results
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            self.beerConnection.session.close()
            
 ############ getUserBeerForPayment ####################################################
    def userBeerPayTypeForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            self.beerConnection.session.close()
            
 ############ getUserPayType ####################################################
    def userPayTypeForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.pay_type_id == _json_entrada["pay_type_id"])
            return results
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            self.beerConnection.session.close()        