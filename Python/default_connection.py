"""
Connection module
"""
import logging
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from dto.beer_connection import BeerConnection
logging.basicConfig(filename="test.log", level=logging.DEBUG)
class DefaultConnection:
    """
    DefaultConnection
    """
    beer_connection = None
    _session = None
    base = None
    engine = None
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    def __init__(self, engine):
        """
        Constructor
        """
        self.engine = engine
        session_maker = sessionmaker(bind=engine)
        # start session
        self._session = session_maker()
        self.base = declarative_base()
        self.beer_connection = BeerConnection(
            engine=self.engine,
            session=self._session,
            base=self.base)
        logging.debug('DefaultConnection full')
    ########## Cerrar conexion ###################
    def commit(self):
        """
        Commit Method
        """
        self._session.commit()

    ########## Cerrar conexion ###################
    def close_connection(self):
        """
        Close current connection
        """
        self._session.close()

    def get_beer_connection(self):
        """
        getBeerConnection
        """
        return self.beer_connection
