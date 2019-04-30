from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import datetime
import logging
import time

class UsuarioCervezaFacade:

    SQL_INSERT_USUARIO_CERVEZA      = "INSERT INTO USUARIO_CERVEZA (CERVEZA_ID, USUARIO_ID, TIPO_PAGO_ID, FECHA_VISITA, _TOKEN, PRODUCTO_PAGO) VALUES({},{},{},TO_DATE('{}','YYYY/MM/DD'), '{}', '{}')"

    SQL_USUARIO_VISITAS             = "SELECT * FROM USUARIO_CERVEZA WHERE USUARIO_ID = {}"

    SQL_USUARIO_CERVEZAS_VISITAS    = "SELECT * FROM USUARIO_CERVEZA WHERE USUARIO_ID = {} AND CERVEZA_ID = {}"

    SQL_USUARIO_TIPO_PAGO           = "SELECT * FROM USUARIO_CERVEZA WHERE USUARIO_ID = {} AND TIPO_PAGO_ID = {}"

    SQL_USUARIO_CERVEZA_TIPO_PAGO   = "SELECT * FROM USUARIO_CERVEZA WHERE USUARIO_ID = {} AND CERVEZA_ID = {} AND TIPO_PAGO_ID = {}"    

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
    def insert_usuario_cerveza(self, _json):
        try:        
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            json_entrada  = json.loads(_json)            
            insert        = self.SQL_INSERT_USUARIO_CERVEZA.format(json_entrada["cerveza_id"], json_entrada["usuario_id"], json_entrada["tipo_pago_id"], json_entrada["fecha_visita"], json_entrada["producto_pago"])
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
    def usuario_visitas(self, _usuario_id):
        try:
            #Conexion a postgre            
            cursor        = self.getCursor()
            #####            
            cursor.execute(self.SQL_USUARIO_VISITAS.format(_usuario_id))
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error consultando cervezas')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None

    ########### obtener cervezas ##############################################
    def usuario_cerveza_visita(self, _usuario_id, _cerveza_id):
        try:
            #Conexion a postgre            
            cursor        = self.getCursor()
            #####            
            cursor.execute(self.SQL_USUARIO_CERVEZAS_VISITAS.format(_usuario_id, _cerveza_id))
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error consultando cervezas')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None     

    ########### usuario por cerveza y tipo de pago ##############################################
    def usuario_cerveza_tipo_pago_visita(self, _usuario_id, _cerveza_id, _tipo_pago_id):
        try:
            #Conexion a postgre            
            cursor        = self.getCursor()
            #####            
            cursor.execute(self.SQL_USUARIO_CERVEZA_TIPO_PAGO.format(_usuario_id, _cerveza_id, _tipo_pago_id))
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error consultando cervezas')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None   

    ########### obtener usuario por tipo de pago ##############################################
    def usuario_tipo_pago(self, _usuario_id, _tipo_pago_id):
        try:
            #Conexion a postgre            
            cursor        = self.getCursor()
            #####            
            cursor.execute(self.SQL_USUARIO_TIPO_PAGO.format(_usuario_id, _tipo_pago_id))
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error consultando cervezas')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None                

    ########## Cerrar conexion ###################
    def cerrarConexion(self):
         self.conexion.close()