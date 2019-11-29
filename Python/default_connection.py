import logging
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from dto.beer_connection        import BeerConnection
logging.basicConfig(filename="test.log", level=logging.DEBUG)
class DefaultConnection:

    beer_connection = None
    session = None
    base = None
    engine = None
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=engine)
        # start session
        self.session = Session()
        self.base = declarative_base()
        self.beer_connection = BeerConnection(engine =self.engine, session =self.session, base =self.base)
    ########## Cerrar conexion ###################
    def commit(self):
        self.session.commit()

    ########## Cerrar conexion ###################
    def close_connection(self):
        self.session.close()

    def get_beer_connection(self):
        return self.beer_connection
