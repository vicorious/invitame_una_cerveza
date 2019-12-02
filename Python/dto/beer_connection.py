"""
BeerConnection module
"""
class BeerConnection():
    """
    BeerConnection class
    """
    def __init__(self, **kwargs):
        """
        Constructor
        """
        self.__dict__ = kwargs

    def __str__(self):
        return self.__class__.__name__
