from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import logging
from .entities.bar import Bar

class BarFacade:
    defaultConnection = None
    beerConnection = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection        = DefaultConnection()  
            self.beerConnection = self.defaultConnection.getBeerConnection()
        except Exception as e:
            logging.debug('Error in "UserFacade: "')
            raise Exception('Error no controlado: {}'.format(e.args[0]))            
        finally:            
            pass

    ############ Constructor ##############################################
    def __init__(self):
        self.getCursor()        

    ############ Login ####################################################
    def barId(self, _bar_id):
        try:
            results = self.beerConnection.session.query(Bar).filter(Bar.id == _bar_id)
            return results
        except MultipleResultsFound as me:                
            logging.debug('Multiple rows. Failed Integrity from database')
        except NoResultFound as ne:
            logging.debug('Bar not found "')
        except Exception as ex:
            logging.debug('Exception: "')
        finally:            
            pass
        return None
    ########### insert_bar #################################################
    def insertBar(self, _json):
        try:
            _json_entrada = json.loads(_json)
            bar = Bar(_json_entrada["title"], _json_entrada["open_date"], _json_entrada["openinng_hour"], 
                        _json_entrada["close_hour"], _json_entrada["open_days"], _json_entrada["payment_product"], 
                        _json_entrada["description"], _json_entrada["image"], _json_entrada["address"],
                        _json_entrada["points"], _json_entrada["facebook"], _json_entrada["twitter"]
                        _json_entrada["instagram"], _json_entrada["emergency_number"], _json_entrada["created_by"])
            self.beerConnection.session.add(bar)
            self.beerConnection.session.commit()
            self.beerConnection.session.close()            
        except Exception as ex:
            logging.debug('Exception when we try add Bar: {}"'.format(ex))
        finally:            
            pass

    ########### forgotPassword #################################################
    def bars(self):
        try:            
            results = self.beerConnection.session.query(Bar)
			self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try fetchy Bars: {}"'.format(ex))
        finally:            
            pass          

    ########### forgotPassword #################################################
    def updateBar(self, _json):
        SQL_UPDATE_BARES          = "UPDATE BAR SET "
        SQL_WHERE_UPDATE_BARES      = "WHERE ID = {}"            
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
            update = SQL_UPDATE_BARES.join(update).join(SQL_WHERE_UPDATE_BARES.format(json_entrada["id"]))
            self.beerConnection.session.query(Bar).from_statement(text(update))
            self.beerConnection.session.commit()
			self.beerConnection.session.close()
        except Exception as ex:
            logging.debug('Exception when we try add User: {}"'.format(ex))
        finally:            
            pass                  