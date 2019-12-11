"""
User module
"""
import json
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm.sync import update
from entities.user import User
from cursor import Cursor

class UserFacade:
    """
    UserFacade class
    """
    cursor = None
    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.cursor = Cursor()

    ############ Login ####################################################
    def login(self, _json):
        """
        Login method
        """
        try:
            _json_entrada = json.loads(_json)
            self.cursor.beer_connection.session.query(User).filter(
                User.name == _json_entrada["name"],
                User.password_token == _json_entrada["password_token"]).one()
            self.cursor.default_connection.beer_connection.session.close()
        except MultipleResultsFound as multiples_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiples_results)
        except NoResultFound as no_results:
            logging.debug('User not found %s"', no_results)
        finally:
            pass

    ########### Register #################################################
    def register(self, _json):
        """
        register method
        """
        try:
            _json_entrada = json.loads(_json)
            user = User(_json_entrada["mail"], _json_entrada["borning_date"],
                        _json_entrada["password_token"], _json_entrada["positive_balance"],
                        _json_entrada["photo"], _json_entrada["credits"],
                        _json_entrada["user_login"])
            self.cursor.default_connection.beer_connection.session.add(user)
            self.cursor.default_connection.beer_connection.session.commit()
            self.cursor.default_connection.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add User: %s"', _excep)
        finally:
            pass

    ########### forgotPassword #################################################
    def forgot_password(self, _json):
        """
        forgot password method
        """
        try:
            _json_entrada = json.loads(_json)
            self.cursor.default_connection.beer_connection.session.execute(
                update(User, values={
                    User.password_token: _json_entrada["new_password_token"]})).filter(
                        User.name == _json_entrada["name"],
                        User.password_token == _json_entrada["password_token"])
            self.cursor.default_connection.beer_connection.session.commit()
            self.cursor.default_connection.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add User: %s"', _excep)
        finally:
            pass
