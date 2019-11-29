import json
import logging
from default_connection import DefaultConnection
from entities.promotion import Promotion
from proxy import ProxyConfiguration

class PromotionFacade:
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
            logging.debug('Error in "Promotion facade: %s "', exception)
            raise Exception('Error no controlado: {}'.format(exception.args[0]))
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
            self.beer_connection.session.add(promotion)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try add Promotion: %s"', exception)
        finally:
            self.beer_connection.session.close()

    ########### Beers #################################################
    def promotions(self):
        try:
            results = self.beer_connection.session.query(Promotion).all()
            return results
        except Exception as exception:
            logging.debug('Exception when we try fetch Promotions: %s"', exception)
        finally:
            self.beer_connection.session.close()

    ########### Update beer #################################################
    def update_promotion(self, _json):
        sql_update_promotion = "UPDATE PROMOTION SET "
        sql_where_update_promotion = "WHERE ID = {}"
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
            update = sql_update_promotion.join(update).join(sql_where_update_promotion.format(_json_entrada["id"]))
            self.beer_connection.session.query(Promotion).from_statement(str(update))
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as exception:
            logging.debug('Exception when we try update promotion: %s"', exception)
        finally:
            self.beer_connection.session.close()
