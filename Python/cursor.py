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

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.proxy))
