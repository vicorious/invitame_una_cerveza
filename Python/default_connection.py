# coding=utf-8

from .entities.entity import Session, engine, Base

class DefaultConnection:

    session = None
    def __init__(self):
        pass

    def postgre_connect(self):
        # generate database schema
        Base.metadata.create_all(engine)

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