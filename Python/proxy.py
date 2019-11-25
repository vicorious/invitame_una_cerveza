from sqlalchemy                 import create_engine
from sqlalchemy_utils           import database_exists, create_database
from constant                   import Constant
from ddl                        import DDL
from dml                        import DML
import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)
class ProxyConfiguration:

    engine = None
    def __init__(self, engine=None):
       if engine is None:
           self.createEngine()
       else: 
           self.engine = engine
           logging.debug("Engine set!")

    def createDatabase(self):
        #Create database
        create_database(self.engine.url)
        logging.debug("Database created!")

    def createEngine(self):
        # generate database schema
        db_url = Constant.ip_default + ":" + Constant.port_default
        db_name = Constant.db_default
        db_user = Constant.user_default
        db_password = Constant.password_default
        self.engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
        logging.debug("Engine created!")

    def existDataBase(self):
        return database_exists(self.engine.url)

    def createDDL(self):
        ddl = DDL()
        ddl.dataDefinitionLanguage(self.engine)
        logging.debug("DataDefinitionLanguage created!")
    
    def installPostgre(self):
        import os
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = fileDir + Constant.postgre_exe_file
        os.system(filename)