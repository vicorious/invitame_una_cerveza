"""
Bar module
"""
import json
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from entities.bar import Bar
from proxy import ProxyConfiguration

class BarFacade:
    """
    BarFacade class
    """
    default_connection = None
    beer_connection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        """
        DataModelingLanguage module
        """
        try:
            #Conexion a postgre
            self.default_connection = DefaultConnection(self.proxy.engine)
            self.beer_connection = self.default_connection.get_beer_connection()
        except Exception as _excep:
            logging.debug('Error in "BarFacade: %s"', _excep)
            raise Exception('Error no controlado: {}'.format(_excep.args[0]))
        finally:
            pass

    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ############ barId ####################################################
    def bar_id(self, _bar_id):
        """
        Bar for id Method
        """
        try:
            results = self.beer_connection.session.query(Bar).filter(Bar.id == _bar_id).one()
            return results
        except MultipleResultsFound as multiple_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiple_results)
        except NoResultFound as no_result:
            logging.debug('Bar not found %s', no_result)
        except Exception as _excep:
            logging.debug('Error in "bar_id: %s"', _excep)
        finally:
            self.beer_connection.session.close()
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
            self.beer_connection.session.add(bar)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
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
            results = self.beer_connection.session.query(Bar).all()
            return results
        except Exception as _excep:
            logging.debug('Exception when we try fetch Bars: %s"', _excep)
        finally:
            self.beer_connection.session.close()

    ########### Update bar #################################################
    def update_bar(self, _json):
        """
        Update Bar Method
        """
        sql_update_bares = "UPDATE BAR SET "
        sql_where_update_bares = "WHERE ID = {}"
        try:
            _json_entrada = json.loads(_json)
            update = ''
            for json_i in _json_entrada:
                for attribute, value in json_i:
                    if attribute in ('id','ID'):
                        continue
                    if value is int:
                        update.join(attribute.upper()).join(" = ").join(value).join(" ")
                    else:
                        update.join(attribute.upper()).join(" = ").join("'").join(value).join("'").join(" ")
            update = sql_update_bares.join(update).join(sql_where_update_bares.format(_json_entrada["id"]))
            self.beer_connection.session.query(Bar).from_statement(str(update))
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try update bar: %s"', _excep)
        finally:
            self.beer_connection.session.close()
