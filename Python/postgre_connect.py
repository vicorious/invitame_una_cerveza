import logging
import psycopg2

class PostgreConnect:
    password = ''
    user = ''
    _ip = ''
    port = ''
    _db = ''
    cadena = ''

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    def __init__(self, db, port, ip, user, password):
        self.password = password
        self.user = user
        self._ip = ip
        self.port = port
        self._db = db

    def connect(self):
        cadena = "host='{}' dbname='{}' user='{}' password='{}'".format(self._ip, self._db, self.user, self.password)
        logging.debug('La cadena de conexion es: {}'.format(cadena))
        conexion = psycopg2.connect(cadena)
        logging.debug('Conexion correcta')
        return conexion
        