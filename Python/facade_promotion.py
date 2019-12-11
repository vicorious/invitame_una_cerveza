"""
Promotion module
"""
import json
import logging
from entities.promotion import Promotion
from cursor import Cursor

class PromotionFacade:
    """
    Promotion class
    """
    cursor = None
    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.cursor = Cursor()

    ########### insert_beer #################################################
    def insert_promotion(self, _json):
        """
        insert promotion
        """
        try:
            _json_entrada = json.loads(_json)
            promotion = Promotion(_json_entrada["beer_id"], _json_entrada["created_by"])
            self.cursor.beer_connection.session.add(promotion)
            self.cursor.beer_connection.session.commit()
            self.cursor.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add Promotion: %s"', _excep)
        finally:
            self.cursor.beer_connection.session.close()

    ########### Beers #################################################
    def promotions(self):
        """
        get promotions method
        """
        try:
            results = self.cursor.beer_connection.session.query(Promotion).all()
            return results
        except Exception as _excep:
            logging.debug('Exception when we try fetch Promotions: %s"', _excep)
        finally:
            self.cursor.beer_connection.session.close()

    ########### Update beer #################################################
    def update_promotion(self, _json):
        """
        update promotion method
        """
        update_promo = "UPDATE PROMOTION SET "
        where_promotion = "WHERE ID = {}"
        self.cursor.update_query(_json, update_promo, where_promotion)
