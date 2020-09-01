"""
Parameters module
"""
import logging
from entities.pay_type import PayType
class FacadeParameters:
    """
    FacadeParameters class
    """
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    cur = None
    ############ Constructor ##############################################
    def __init__(self):
        """
        Constructor
        """
        self.cur = Cursor()

    ############ pay_type ####################################################
    def pay_type(self):
        """
        Pay type´s method
        """
        try:
            results = self.cur.default_connection.get_beer_connection().session.query(PayType).all()
            return PayType.serialize_many(results)
        except Exception as _except:
            logging.debug('pay_type not found %s"', _except)       
        finally:
            self.cur.default_connection.get_beer_connection().session.close()