from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import logging

class ClienteFacade:

	defaultConnection = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ Constructor ##############################################
    def __init__(self):
        pass

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            self.defaultConnection        = DefaultConnection()         
        except Exception as e:
            logging.debug('Error obteniendo el cursor facade bares')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            pass  