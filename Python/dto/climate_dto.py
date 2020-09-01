"""
ClimateDTO
"""
class ClimateDTO():
    """
    ClimateDTO
    """
    def __init__(self, **kwargs):
        """
        Constructor
        """
        self.__dict__ = kwargs

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self, is_me: bool = False):
        return self.__dict__

    def __iter__(self):
        yield 'id', self.weather
        yield 'main', self.main
        yield 'wind', self.wind
        yield 'city', self.city
