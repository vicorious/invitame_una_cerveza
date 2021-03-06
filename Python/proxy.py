"""
Configuration module
"""
import os
import logging
from sqlalchemy                 import create_engine
from sqlalchemy_utils           import database_exists, create_database
from constant                   import Constant
from ddl                        import DDL
from dml                        import DML
logging.basicConfig(filename="test.log", level=logging.DEBUG)
class ProxyConfiguration:
    """
    ProxyConfiguration class
    """
    engine = None
    def __init__(self, engine=None):
        """
        Constructor
        """
        if engine is None:
            self.create_engine()
        else:
            self.engine = engine
            logging.debug("Engine set!")

    def create_database(self):
        """
        create database method
        """
        create_database(self.engine.url)
        logging.debug("Database created!")

    def create_engine(self):
        """
        create engine method
        """
        db_url = Constant.ip_default + ":" + Constant.port_default
        db_name = Constant.db_default
        db_user = Constant.user_default
        db_password = Constant.password_default
        self.engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
        logging.debug("Engine created!")

    def exist_data_base(self):
        """
        exist data base method
        """
        return database_exists(self.engine.url)

    def create_ddl(self):
        """
        create ddl method
        """
        ddl = DDL()
        ddl.data_definition_language(self.engine)
        logging.debug("DataDefinitionLanguage created!")

    def create_dml(self):
        """
        create dml method
        """
        dml = DML(self.engine)
        dml.create_dml()
        logging.debug("DataModelingLanguage created!")

    def install_postgre(self):
        """
        install postgre method
        """
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_name = file_dir + Constant.postgre_exe_file
        os.system(file_name)
        