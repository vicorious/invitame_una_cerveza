from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker
from sqlalchemy_utils           import database_exists, create_database
from constant                   import Constant
from sqlalchemy                 import MetaData
from ddl                        import DDL
from default_connection         import DefaultConnection

class ProxyConfiguration:

    defaultConnection = None
    metadata = None
    
    def __init__(self):
        self.defaultConnection = DefaultConnection()

    def createDatabase(self):
        # generate database schema
        db_url = Constant.ip_default + ":" + Constant.port_default
        db_name = Constant.db_default
        db_user = Constant.user_default
        db_password = Constant.password_default        
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
        #Create database
        create_database(engine.url) if not database_exists(engine.url) else print('Database created!')
        return engine
    def getMetaData(self):
        return self.metadata

    def createDDL(self):
        ddl = DDL()
        ddl.dataDefinitionLanguage()