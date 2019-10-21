from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import datetime
import logging
import time
from entities.beer import Beer
from proxy                  import ProxyConfiguration

class BeerFacade:
    defaultConnection = None
    beerConnection = None
    proxy = ProxyConfiguration()

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection        = DefaultConnection(self.proxy.engine)
            self.beerConnection = self.defaultConnection.getBeerConnection()   
        except Exception as e:
            logging.debug('Error in "Beer facade: "')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.getCursor()        

    ############ beerId ####################################################
    def beerId(self, _beer_id):
        try:
            results = self.beerConnection.session.query(Beer).filter(Beer.id == _beer_id)
            return results
        except MultipleResultsFound as me:                
            logging.debug('Multiple rows. Failed Integrity from database')
        except NoResultFound as ne:
            logging.debug('Beer not found "')
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            self.beerConnection.session.close()
        return None
    ########### insert_beer #################################################
    def insertBeer(self, _json):
        try:
            _json_entrada = json.loads(_json)
            beer = Beer(_json_entrada["title"], _json_entrada["price"], _json_entrada["happy_hour_price"], 
                        _json_entrada["bar_id"], _json_entrada["beer_type_id"], _json_entrada["avb"], 
                        _json_entrada["ibu"], _json_entrada["srm"], _json_entrada["description"],
                        _json_entrada["image"], _json_entrada["pint"], _json_entrada["cup330"],
                        _json_entrada["giraffe"], _json_entrada["pitcher"], _json_entrada["created_by"])
            self.beerConnection.session.add(beer)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()            
        except Exception as ex:
            logging.debug('Exception when we try add Beer: {}"'.format(ex))
        finally:            
            self.beerConnection.session.close()

    ########### Beers #################################################
    def beers(self):
        try:            
            results = self.beerConnection.session.query(Beer)
            return results
        except Exception as ex:
            logging.debug('Exception when we try fetch Beers: {}"'.format(ex))
        finally:
            self.beerConnection.session.close()          

    ########### Update beer #################################################
    def updateBeer(self, _json):
        SQL_UPDATE_BEERS         = "UPDATE BEER SET "
        SQL_WHERE_UPDATE_BEERS      = "WHERE ID = {}"            
        try:
            _json_entrada = json.loads(_json)
            update = ''
            for json in _json_entrada:
                for attribute, value in json:
                    if attribute == 'id' or attribute == 'ID':
                        continue
                    if value is int:
                        update.join(attribute.upper()).join(" = ").join(value).join(" ")
                    else:
                        update.join(attribute.upper()).join(" = ").join("'").join(value).join("'").join(" ")
            update = SQL_UPDATE_BEERS.join(update).join(SQL_WHERE_UPDATE_BEERS.format(json_entrada["id"]))
            self.beerConnection.session.query(Beer).from_statement(text(update))
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try update beer: {}"'.format(ex))
        finally:            
            self.beerConnection.session.close() 