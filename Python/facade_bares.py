import json
import sys
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from entities.bar import Bar
from proxy import ProxyConfiguration

class BarFacade:
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
            logging.debug('Error in "BarFacade: %s"', exception)
            raise Exception('Error no controlado: {}'.format(exception.args[0]))
        finally:            
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ############ barId ####################################################
    def bar_id(self, _bar_id):
        try:
            results = self.beerConnection.session.query(Bar).filter(Bar.id == _bar_id).one()
            return results
        except MultipleResultsFound as multiple_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiple_results)
        except NoResultFound as no_result:
            logging.debug('Bar not found %s', no_result)
        except Exception as exception:
            logging.debug('Error in "bar_id: %s"', exception)
        finally:
            self.beerConnection.session.close()
        return None
    ########### insert_bar #################################################
    def insert_bar(self, _json):
        try:
            _json_entrada = json.loads(_json)
            bar = Bar(_json_entrada["title"], _json_entrada["open_date"], _json_entrada["openinng_hour"], _json_entrada["close_hour"], _json_entrada["open_days"], _json_entrada["payment_product"], _json_entrada["description"], _json_entrada["image"], _json_entrada["address"], _json_entrada["points"], _json_entrada["facebook"], _json_entrada["twitter"], _json_entrada["instagram"], _json_entrada["emergency_number"], _json_entrada["created_by"])
            self.beerConnection.session.add(bar)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try add Bar: %s"', exception)
        finally:
            pass

    ########### Bars #################################################
    def bars(self):
        try:
            results = self.beerConnection.session.query(Bar).all()
            return results
        except Exception as exception:
            logging.debug('Exception when we try fetch Bars: %s"' , exception)
        finally:
            self.beerConnection.session.close()

    ########### Update bar #################################################
    def update_bar(self, _json):
        SQL_UPDATE_BARES = "UPDATE BAR SET "
        SQL_WHERE_UPDATE_BARES = "WHERE ID = {}"
        try:
            _json_entrada = json.loads(_json)
            update = ''
            for json_i in _json_entrada:
                for attribute, value in json_i:
                    if attribute == 'id' or attribute == 'ID':
                        continue
                    if value is int:
                        update.join(attribute.upper()).join(" = ").join(value).join(" ")
                    else:
                        update.join(attribute.upper()).join(" = ").join("'").join(value).join("'").join(" ")
            update = SQL_UPDATE_BARES.join(update).join(SQL_WHERE_UPDATE_BARES.format(_json_entrada["id"]))
            self.beerConnection.session.query(Bar).from_statement(str(update))
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try update bar: %s"' , exception)
        finally:
            self.beerConnection.session.close()