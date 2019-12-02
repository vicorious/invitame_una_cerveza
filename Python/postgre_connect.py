"""
PostgreModule
"""
import logging
import psycopg2
class PostgreConnect:
    """
    PostgreConnect class
    """
    password = ''
    user = ''
    _ip = ''
    port = ''
    _db = ''
    cadena = ''

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    def __init__(self, db, port, ip, user, password):
        """
        Constructor
        """
        self.password = password
        self.user = user
        self._ip = ip
        self.port = port
        self._db = db

    def connect(self):
        """
        Connect method
        """
        db_str = "host='{}' dbname='{}'".format(self._ip, self._db)
        user_str = "user='{}' password='{}'".format(self.user, self.password)
        cadena = db_str.join(user_str)
        logging.debug('La cadena de conexion es: %s', cadena)
        conexion = psycopg2.connect(cadena)
        logging.debug('Conexion correcta')
        return conexion

    def __str__(self):
        return self.__class__.__name__
