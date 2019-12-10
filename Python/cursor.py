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
