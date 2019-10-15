from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import datetime
import logging
import time
from .entities.user_beer import UserBeer

class UserBeerFacade:
    
    defaultConnection = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ####### Constructor ############
    def __init__(self):
        pass

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection        = DefaultConnection()           
        except Exception as e:
            logging.debug('Error obteniendo el cursor facade bares')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

 ############ Login ####################################################
    def userForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.id == _json_entrada["id"])
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass

    ########### Register #################################################
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
            pass
			
 ############ Login ####################################################
    def userBeerForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"])
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass
			
 ############ Login ####################################################
    def userBeerPayTypeForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["beer_id"], UserBeer.beer_id == _json_entrada["pay_type_id"])
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass
			
 ############ Login ####################################################
    def userPayTypeForVisit(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(UserBeer).filter(UserBeer.user_id == _json_entrada["user_id"], UserBeer.beer_id == _json_entrada["pay_type_id"])
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass

    ########### forgotPassword #################################################
    def forgotPassword(self, _json):
        try:
            _json_entrada = json.loads(_json)
            self.beerConnection.session.execute(update(User, values={User.password_token: _json_entrada["new_password_token"]})).
                    filter(User.name == _json_entrada["name"], User.password_token == _json_entrada["password_token"])
			self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try add User: {}"'.format(ex))
        finally:            
            pass  			