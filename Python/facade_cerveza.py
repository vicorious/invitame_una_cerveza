"""
Beer module
"""
import json
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from entities.beer import Beer
from cursor import Cursor

class BeerFacade:
    """
    Beer class
    """
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    cur = None
    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.cur = Cursor()

    ############ beerId ####################################################
    def beer_id(self, _beer_id):
        """
        Beer for id method
        """
        try:
            results = self.cur.default_connection.beer_connection.session.query(Beer).filter(
                Beer.id == _beer_id).one()
            return results
        except MultipleResultsFound as multiple_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiple_results)
        except NoResultFound as no_result:
            logging.debug('Beer not found %s"', no_result)       
        finally:
            self.cur.default_connection.beer_connection.session.close()
        return None
    ########### insert_beer #################################################
    def insert_beer(self, _json):
        """
        insert beer method
        """
        try:
            _json_entrada = json.loads(_json)
            beer = Beer(_json_entrada["title"], _json_entrada["price"],
                        _json_entrada["happy_hour_price"],
                        _json_entrada["bar_id"], _json_entrada["beer_type_id"],
                        _json_entrada["avb"], _json_entrada["ibu"], _json_entrada["srm"],
                        _json_entrada["description"], _json_entrada["image"], _json_entrada["pint"],
                        _json_entrada["cup330"], _json_entrada["giraffe"],
                        _json_entrada["pitcher"], _json_entrada["created_by"])
            self.cur.default_connection.beer_connection.session.add(beer)
            self.cur.default_connection.beer_connection.session.commit()
            self.cur.default_connection.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add Beer: %s"', _excep)
        finally:
            self.cur.beer_connection.session.close()

    ########### Beers #################################################
    def beers(self):
        """
        get beers method
        """
        try:
            results = self.cur.default_connection.beer_connection.session.query(Beer).all()
            return results
        except Exception as _excep:
            logging.debug('Exception when we try fetch Beers: %s"', _excep)
        finally:
            self.cur.default_connection.beer_connection.session.close()

    ########### Update beer #################################################
    def update_beer(self, _json):
        """
        update beer method
        """
        update_beers = "UPDATE BEER SET "
        where_update_beers = "WHERE ID = {}"
        self.cursor.update_query(_json, update_beers, where_update_beers)
