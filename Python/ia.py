"""
IA Module
"""
class IA:
    """
    IA class
    """
    ####### Constructor ############
    def __init__(self):
        """
        Constructor
        """
    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))
