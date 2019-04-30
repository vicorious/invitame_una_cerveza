from default_connection import DefaultConnection
import json
import sys
import psycopg2.extras
import logging

class BaresFacade:

    SQL_BARES                 = "SELECT * FROM BAR"

    SQL_BARES_ID              = "SELECT * FROM BAR WHERE ID = {}" 

    SQL_INSERT_BARES          = "INSERT INTO BARES (ID, NOMBRE, FECHA_APERTURA, HORA_APERTURA, HORA_CIERRE, DIAS_ABIERTO, PRODUCTO_PAGO) VALUES ({},'{}', TO_DATE('{}','YYYY/MM/DD'), '{}', '{}', '{}', '{}')"

	SQL_UPDATE_BARES          = "UPDATE BARES SET "
	
	SQL_WHERE_UPDATE_BARES	  = "WHERE ID = {}"
	
    conexion = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

     ################## Constructor ####################
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
            logging.debug('Error obteniendo el cursor facade bares')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            pass

    ############ valoracion ####################### 
    def bares(self):
        try:        
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            cursor.execute(self.SQL_BARES)            
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error obteniendo los bares')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None 
                  
    ############ valoracion por tipo ##############
    def bares_id(self, _id):
        try:
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####           
            cursor.execute(self.SQL_BARES_ID.format(_id))   
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            logging.debug('Error obteniendo el bar: {}'.format(_id))
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return None
    
    ########### Insertar Bar
    def insertar_bar(self, _json):
        try:         
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            json_entrada = json.loads(_json)            
            insert = self.SQL_INSERT_BARES.format(json_entrada["id"], json_entrada["nombre"], json_entrada["fecha_apertura"], json_entrada["hora_apertura"], json_entrada["hora_cierre"], json_entrada["dias_abierto"], json_entrada["producto_pago"])
            cursor.execute(insert)
            self.conexion.commit()
            return True
        except Exception as e:
            logging.debug('Error asociando la respuesta a la pregunta')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return False
		
    ########### Asociar respuesta a la pregunta
    def actualizar_bar(self, _json):
        try:         
            #Conexion a postgre            
            cursor    = self.getCursor()
            #####
            json_entrada = json.loads(_json)
			update = ''
			for objeto in json_object:				
				for attribute, value in objeto.items():
				    if attribute == 'id' or attribute == 'ID':
					    continue
				    if value is int:
					    update.join(attribute.upper()).join(" = ").join(value).join(" ")
					else:
					    update.join(attribute.upper()).join(" = ").join("'").join(value).join("'").join(" ")
            update = self.SQL_UPDATE_BARES.join(update).join(SQL_WHERE_UPDATE_BARES.format(json_entrada["id"]))
            cursor.execute(update)
            self.conexion.commit()
            return True
        except Exception as e:
            logging.debug('Error asociando la respuesta a la pregunta')
            raise Exception('Error no controlado: {}'.format(e.args[0]))			
        finally:            
            cursor.close()
            self.cerrarConexion()
        return False		

    ########## Cerrar conexion ###################
    def cerrarConexion(self):
         self.conexion.close()
                