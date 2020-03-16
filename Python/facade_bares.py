"""
Bar module
"""
import json
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from entities.bar import Bar
from cursor import Cursor

class BarFacade:
    """
    BarFacade class
    """
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    cursor = None
    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.cursor = Cursor()

    ############ barId ####################################################
    def bar_id(self, _bar_id):
        """
        Bar for id Method
        """
        try:
            results = self.cursor.default_connection.get_beer_connection().session.query(Bar).filter(
                Bar.id == _bar_id).one()
            return results
        except MultipleResultsFound as multiple_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiple_results)
        except NoResultFound as no_result:
            logging.debug('Bar not found %s', no_result)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()
        return None
    ########### insert_bar #################################################
    def insert_bar(self, _json):
        """
        Insert Bar Method
        """
        try:
            _json_entrada = json.loads(_json)
            bar = Bar(_json_entrada["title"], _json_entrada["open_date"],
                      _json_entrada["openinng_hour"], _json_entrada["close_hour"],
                      _json_entrada["open_days"],
                      _json_entrada["payment_product"], _json_entrada["description"],
                      _json_entrada["image"],
                      _json_entrada["address"], _json_entrada["points"], _json_entrada["facebook"],
                      _json_entrada["twitter"], _json_entrada["instagram"],
                      _json_entrada["emergency_number"], _json_entrada["created_by"])
            self.cursor.default_connection.get_beer_connection().session.add(bar)
            self.cursor.default_connection.get_beer_connection().session.commit()
            self.cursor.default_connection.get_beer_connection().session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add Bar: %s"', _excep)
        finally:
            pass

    ########### Bars #################################################
    def bars(self):
        """
        getBars Method
        """
        try:
            results = self.cursor.default_connection._session.query(Bar).all()
            return results
        except Exception as _excep:
            logging.debug('Exception when we try fetch Bars: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

    ########### Update bar #################################################
    def update_bar(self, _json):
        """
        Update Bar Method
        """
        update_bares = "UPDATE BAR SET "
        where_update_bares = "WHERE ID = {}"
        self.cursor.update_query(_json, update_bares, where_update_bares)
