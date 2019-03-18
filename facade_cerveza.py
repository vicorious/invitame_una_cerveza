from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import datetime
import logging
import time

class CervezaFacade:

    SQL_INSERT_CERVEZA            = "INSERT INTO CERVEZA (ID, NOMBRE, PRECIO, BAR_ID, TIPO_CERVEZA_ID, GRADOS_ALCOHOL, IBU, SRM) VALUES({},'{}',{},{}, {}, '{}', '{}', '{}')"

    SQL_CERVEZAS                  = "SELECT * FROM CERVEZA"

    SQL_CERVEZA_ID                = "SELECT * FROM CERVEZA WHERE ID = {}"

    conexion = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)


    ####### Constructor ############
    def __init__(self):
        pass

    ############ retorna el cursor para poder interactuar con la DB #######
    def getCursor(self):
        try:
            #Conexion a postgre
            default        = DefaultConnection()
            self.conexion  = default.postgre_connect()
            cursor         = self.conexion.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return cursor
        except Exception as e:
            logging.debug('Error obteniendo el cursor de facade cerveza')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            pass

    ############ crear cerveza ###############################
    def insert_cerveza(self, _json):
        try:        
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            json_entrada  = json.loads(_json)            
            insert        = self.SQL_INSERT_CERVEZA.format(json_entrada["id"], json_entrada["nombre"], json_entrada["precio"], json_entrada["bar_id"], json_entrada["tipo_cerveza_id"], json_entrada["grados_alcohol"], json_entrada["ibu"], json_entrada["srm"])
            cursor.execute(insert)
            self.conexion.commit()
            return True
        except Exception as e:
            logging.debug('Error creando el examen')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:
            cursor.close()
            self.cerrarConexion()
        return False
    
    ########### obtener cervezas ##############################################
    def cervezas(self):
        try:
            #Conexion a postgre            
            cursor        = self.getCursor()
            #####            
            cursor.execute(self.SQL_CERVEZAS)            
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error consultando cervezas')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None

    ######### obtener cervezas por id #############################################    
    def cerveza_id(self, _id):
        try:         
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            cerveza = self.SQL_CERVEZA_ID.format(_id)
            cursor.execute(cerveza)
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error obteniendo cerveza con el id {} '.format(_id))
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return False

    ########## Cerrar conexion ###################
    def cerrarConexion(self):
         self.conexion.close()