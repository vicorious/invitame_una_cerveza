from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker
from constant                     import Constant

class DefaultConnection:

    session = None       
    Base = None
    
    def __init__(self):
        pass

    def postgre_connect(self):
        # generate database schema
        db_url = Constant.ip_default + ":" + Constant.port_default
        db_name = Constant.db_default
        db_user = Constant.user_default
        db_password = Constant.password_default
        engine = create_engine('postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
        self.session = sessionmaker(bind=engine)
        self.Base = declarative_base()

        # start session
        self.session = Session()
        
    ########## Cerrar conexion ###################
    def commit(self):
         self.session.commit()

        
    ########## Cerrar conexion ###################
    def closeConnection(self):
         self.session.close()
         
    def getSession(self):
         return self.session