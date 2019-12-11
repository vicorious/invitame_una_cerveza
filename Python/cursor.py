"""
Cursor module
"""
from flask import json
from proxy import ProxyConfiguration
from default_connection import DefaultConnection
import logging
class Cursor:
    """
    Cursor Class
    """
    default_connection = None
    proxy = None
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    def __init__(self):
        """
        Cursor class
        """
        self.proxy = ProxyConfiguration()
        self.default_connection = DefaultConnection(self.proxy.engine)

    def update_query(self, _json, _update_table, _where):
        """
        Update any table
        """
        try:
            _json_entrada = json.loads(_json)
            update = ''
            for json_i in _json_entrada:
                for attribute, value in json_i:
                    if attribute in ('id', 'ID'):
                        continue
                    if value is int:
                        update.join(attribute.upper()).join(" = ").join(value).join(" ")
                    else:
                        update.join(attribute.upper()).join(" = '").join(value).join("' ")
            update = _update_table.join(update).join(_where.format(_json_entrada["id"]))
            self.default_connection.beer_connection.session.query(Bar).from_statement(str(update))
            self.default_connection.beer_connection.session.commit()
            self.default_connection.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try update: %s"', _excep)
        finally:
            self.default_connection.beer_connection.session.close()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.proxy))
