import json
import sys
import psycopg2.extras
import datetime
import logging
import time
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from default_connection import DefaultConnection
from entities.promotion import Promotion
from proxy import ProxyConfiguration

class PromotionFacade:
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
            logging.debug('Error in "Promotion facade: "')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.proxy = ProxyConfiguration()
        self.get_cursor()        

    ########### insert_beer #################################################
    def insert_promotion(self, _json):
        try:
            _json_entrada = json.loads(_json)
            promotion = Promotion(_json_entrada["beer_id"], _json_entrada["created_by"])
            self.beerConnection.session.add(promotion)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()            
        except Exception as ex:
            logging.debug('Exception when we try add Promotion: {}"'.format(ex))
        finally:            
            self.beerConnection.session.close()

    ########### Beers #################################################
    def promotions(self):
        try:            
            results = self.beerConnection.session.query(Promotion).all()
            return results
        except Exception as ex:
            logging.debug('Exception when we try fetch Promotions: {}"'.format(ex))
        finally:
            self.beerConnection.session.close()          

    ########### Update beer #################################################
    def update_promotion(self, _json):
        SQL_UPDATE_BEERS = "UPDATE PROMOTION SET "
        SQL_WHERE_UPDATE_BEERS = "WHERE ID = {}"            
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
            update = SQL_UPDATE_BEERS.join(update).join(SQL_WHERE_UPDATE_BEERS.format(_json_entrada["id"]))
            self.beerConnection.session.query(Promotion).from_statement(str(update))
            self.beerConnection.session.commit()
            self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try update promotion: {}"'.format(ex))
        finally:            
            self.beerConnection.session.close() 