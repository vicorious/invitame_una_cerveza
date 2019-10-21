from sqlalchemy.orm             import sessionmaker
from dto.beer_connection        import BeerConnection
from sqlalchemy.ext.declarative import declarative_base
import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)
class DefaultConnection:

    beerConnection = None
    session = None
    base = None
    engine = None
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=engine)
        # start session
        self.session = Session()
        self.base = declarative_base()
        self.beerConnection = BeerConnection(engine = self.engine, session = self.session, base = self.base)
    ########## Cerrar conexion ###################
    def commit(self):
         self.session.commit()
       
    ########## Cerrar conexion ###################
    def closeConnection(self):
         self.session.close()
         
    def getBeerConnection(self):
        return self.beerConnection