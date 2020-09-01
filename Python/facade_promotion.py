"""
Promotion module
"""
import json
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
from sqlalchemy import join
from sqlalchemy.sql import select
from entities.promotion import Promotion
from dto.promotion_beer_roe import PromotionBeerBar
from entities.bar import Bar
from entities.beer import Beer
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
            promotion = Promotion(_json_entrada["duration"], _json_entrada["beer_id"], _json_entrada["created_by"])
            self.cursor.default_connection.get_beer_connection().session.add(promotion)
            self.cursor.default_connection.get_beer_connection().session.commit()
            self.cursor.default_connection.get_beer_connection().session.close()
        except Exception as _excep:
            logging.debug('Exception when we try add Promotion: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

    ########### Beers #################################################
    def promotions(self):
        """
        get promotions method
        """
        try:
            results = self.cursor.default_connection.get_beer_connection().session.query(Promotion).all()
            return Promotion.serialize_many(results)
        except Exception as _excep:
            logging.debug('Exception when we try fetch Promotions: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

    ########### Beers #################################################
    def promotions_by_bar(self, _bar_id):
        """
        get promotions methodby bar
        """
        try:
            if str(_bar_id) == "0":
                results = self.cursor.default_connection.get_beer_connection().session.query(Promotion, Beer, Bar).join(Beer, Promotion.beer_id==Beer.id).join(Bar, Beer.bar_id==Bar.id).all()
            else:
                results = self.cursor.default_connection.get_beer_connection().session.query(Promotion, Beer, Bar).join(Beer, Promotion.beer_id==Beer.id).join(Bar, Beer.bar_id==Bar.id).filter(Bar.id == _bar_id).all()
            return PromotionBeerBar.serialize_list(results)
        except Exception as _excep:
            logging.debug('Exception when we try fetch promotions_by_bar: %s"', _excep)
        finally:
            self.cursor.default_connection.get_beer_connection().session.close()

    ########### Update beer #################################################
    def update_promotion(self, _json):
        """
        update promotion method
        """
        update_promo = "UPDATE PROMOTION SET "
        where_promotion = "WHERE ID = {}"
        self.cursor.update_query(_json, update_promo, where_promotion)
