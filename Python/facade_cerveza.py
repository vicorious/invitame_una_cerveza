import json
import logging
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from entities.beer import Beer
from proxy import ProxyConfiguration

class BeerFacade:
    default_connection = None
    beer_connection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        try:
            #Conexion a postgre
            self.default_connection = DefaultConnection(self.proxy.engine)
            self.beer_connection = self.defaultConnection.get_beer_connection()
        except Exception as exception:
            logging.debug('Error in "Beer facade: %s"', exception)
            raise Exception('Error no controlado: {}'.format(exception.args[0]))
        finally:
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ############ beerId ####################################################
    def beer_id(self, _beer_id):
        try:
            results = self.beerConnection.session.query(Beer).filter(Beer.id == _beer_id).one()
            return results
        except MultipleResultsFound as multiple_results:
            logging.debug('Multiple rows. Failed Integrity from database %s', multiple_results)
        except NoResultFound as no_result:
            logging.debug('Beer not found %s"', no_result)
        except Exception as exception:
            logging.debug('Exception: %s"', exception)
        finally:
            self.beer_connection.session.close()
        return None
    ########### insert_beer #################################################
    def insert_beer(self, _json):
        try:
            _json_entrada = json.loads(_json)
            beer = Beer(_json_entrada["title"], _json_entrada["price"], _json_entrada["happy_hour_price"],_json_entrada["bar_id"], _json_entrada["beer_type_id"], _json_entrada["avb"],_json_entrada["ibu"], _json_entrada["srm"], _json_entrada["description"], _json_entrada["image"], _json_entrada["pint"], _json_entrada["cup330"], _json_entrada["giraffe"], _json_entrada["pitcher"], _json_entrada["created_by"])
            self.beer_connection.session.add(beer)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try add Beer: %s"', exception)
        finally:
            self.beer_connection.session.close()

    ########### Beers #################################################
    def beers(self):
        try:
            results = self.beer_connection.session.query(Beer).all()
            return results
        except Exception as exception:
            logging.debug('Exception when we try fetch Beers: %s"', exception)
        finally:
            self.beer_connection.session.close()

    ########### Update beer #################################################
    def update_beer(self, _json):
        sql_update_beers = "UPDATE BEER SET "
        sql_where_update_beers = "WHERE ID = {}"
        try:
            _json_entrada = json.loads(_json)
            update = ''
            for json_i in _json_entrada:
                for attribute, value in json_i:
                    if attribute in('id', 'ID'):
                        continue
                    if value is int:
                        update.join(attribute.upper()).join(" = ").join(value).join(" ")
                    else:
                        update.join(attribute.upper()).join(" = ").join("'").join(value).join("'").join(" ")
            update = sql_update_beers.join(update).join(sql_where_update_beers.format(_json_entrada["id"]))
            self.beer_connection.session.query(Beer).from_statement(str(update))
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try update beer: %s"', exception)
        finally:
            self.beer_connection.session.close()
