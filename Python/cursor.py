"""
Cursor module
"""
from proxy import ProxyConfiguration

class Cursor:
    """
    Cursor Class
    """
    beer_connection = None
    proxy = None
    def __init__(self):
        """
        Cursor class
        """
        self.proxy = ProxyConfiguration()
    
    def update_query(self, _json, _update_table, _where):
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
            self.cursor.beer_connection.session.query(Bar).from_statement(str(update))
            self.cursor.beer_connection.session.commit()
            self.cursor.beer_connection.session.close()
        except Exception as _excep:
            logging.debug('Exception when we try update: %s"', _excep)
        finally:
            self.cursor.beer_connection.session.close()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.proxy))
