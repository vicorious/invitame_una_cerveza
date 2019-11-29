import json
import sys
import psycopg2.extras
import logging
from entities.user import User
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from proxy import ProxyConfiguration

class UserFacade:

    defaultConnection = None
    beerConnection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection = DefaultConnection(self.proxy.engine)
            self.beerConnection = self.defaultConnection.get_beer_connection()   
        except Exception as e:
            logging.debug('Error in "UserFacade: "')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.get_cursor()        

    ############ Login ####################################################
    def login(self, _json):
        try:
            _json_entrada = json.loads(_json)
            results = self.beerConnection.session.query(User).filter(User.name == _json_entrada["name"], User.password_token == _json_entrada["password_token"]).one()
            self.beerConnection.session.close()
        except MultipleResultsFound as me:                
            logging.debug('Multiple rows. Failed Integrity from database')
        except NoResultFound as ne:
            logging.debug('User not found "')
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass

    ########### Register #################################################
    def register(self, _json):
        try:
            _json_entrada = json.loads(_json)
            user = User(_json_entrada["mail"], _json_entrada["borning_date"], _json_entrada["password_token"],_json_entrada["positive_balance"], _json_entrada["photo"], _json_entrada["credits"], _json_entrada["user_login"])
            self.beerConnection.session.add(user)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try add User: {}"'.format(ex))
        finally:            
            pass

    ########### forgotPassword #################################################
    def forgot_password(self, _json):
        try:
            _json_entrada = json.loads(_json)
            self.beerConnection.session.execute(update(User, values={User.password_token: _json_entrada["new_password_token"]})).filter(User.name == _json_entrada["name"], User.password_token == _json_entrada["password_token"])
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try add User: {}"'.format(ex))
        finally:            
            pass              