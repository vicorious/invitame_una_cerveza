"""
Promotion module
"""
import json
import logging
from default_connection import DefaultConnection
from entities.promotion import Promotion
from proxy import ProxyConfiguration

class PromotionFacade:
    """
    Promotion class
    """
    default_connection = None
    beer_connection = None
    proxy = None

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ retorna el cursor para poder interactuar con la DB #######
    def get_cursor(self):
        """
        get cursor method
        """
        try:
            #Conexion a postgre
            self.default_connection = DefaultConnection(self.proxy.engine)
            self.beer_connection = self.default_connection.get_beer_connection()
        except Exception as _excep:
            logging.debug('Error in "Promotion facade: %s "', _excep)
            raise Exception('Error no controlado: {}'.format(_excep.args[0]))
        finally:
            pass

    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.proxy = ProxyConfiguration()
        self.get_cursor()

    ########### insert_beer #################################################
    def insert_promotion(self, _json):
        """
        insert promotion
        """
        try:
            _json_entrada = json.loads(_json)
            promotion = Promotion(_json_entrada["beer_id"], _json_entrada["created_by"])
            self.beer_connection.session.add(promotion)
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add Promotion: %s"', _excep)
        finally:
            self.beer_connection.session.close()

    ########### Beers #################################################
    def promotions(self):
        """
        get promotions method
        """
        try:
            results = self.beer_connection.session.query(Promotion).all()
            return results
        except Exception as _excep:
            logging.debug('Exception when we try fetch Promotions: %s"', _excep)
        finally:
            self.beer_connection.session.close()

    ########### Update beer #################################################
    def update_promotion(self, _json):
        """
        update promotion method
        """
        update_promo = "UPDATE PROMOTION SET "
        where_promotion = "WHERE ID = {}"
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
                        update.join(attribute.upper()).join(" = '").join(value).join("' ")
            update = update_promo.join(update).join(where_promotion.format(_json_entrada["id"]))
            self.beer_connection.session.query(Promotion).from_statement(str(update))
            self.beer_connection.session.commit()
            self.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try update promotion: %s"', _excep)
        finally:
            self.beer_connection.session.close()
