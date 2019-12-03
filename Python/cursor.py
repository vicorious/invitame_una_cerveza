"""
Cursor module
"""
from default_connection import DefaultConnection
from proxy import ProxyConfiguration

class Cursor:
    """
    Cursor Class
    """
    default_connection = None
    beer_connection = None
    proxy = None
    def __init__(self):
        """
        Cursor class
        """
        self.proxy = ProxyConfiguration()
