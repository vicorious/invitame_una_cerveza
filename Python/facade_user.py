import json
import sys
import logging
from entities.user import User
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from proxy import ProxyConfiguration
from sqlalchemy.orm.sync import update

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
        except Exception as exception:
            logging.debug('Error in "UserFacade: %s"', exception)
            raise Exception('Error no controlado: {}'.format(exception.args[0]))
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
        except MultipleResultsFound as multiples_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiples_results)
        except NoResultFound as no_results:
            logging.debug('User not found %s"', no_results)
        except Exception as exception:
            logging.debug('Exception: %s"' , exception)
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
        except Exception as exception:
            logging.debug('Exception when we try add User: %s"' , exception)
        finally:
            pass

    ########### forgotPassword #################################################
    def forgot_password(self, _json):
        try:
            _json_entrada = json.loads(_json)
            self.beerConnection.session.execute(update(User, values={User.password_token: _json_entrada["new_password_token"]})).filter(User.name == _json_entrada["name"], User.password_token == _json_entrada["password_token"])
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try add User: %s"' , exception)
        finally:
            pass