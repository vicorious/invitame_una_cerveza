"""
Beer Pairing module
"""
from typing import Any, List
from entities.beer import Beer
from entities.pairing import Pairing
from constant import Constant

class BeerPairing():

    beer = None
    pairing = None
    """
    BeerPairing
    """
    def __init__(self, beer, pairing):
        """
        Constructor
        """
        self.pairing = pairing
        self.beer = beer

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))
    
    def serialize(self):
        return dict(pairing=Pairing(self.pairing.name, self.pairing.image, self.pairing.beer_id, Constant.user, self.pairing.id).serialize(),
                    beer=Beer(self.beer.name, self.beer.pint_price, self.beer.cup330_price,
                     self.beer.giraffe_price, self.beer.pitcher_price,
                     self.beer.bar_id, self.beer.beer_type_id, self.beer.avb,
                     self.beer.ibu, self.beer.srm,
                     self.beer.description, self.beer.image,
                     self.beer.pint, self.beer.cup330,
                     self.beer.giraffe, self.beer.pitcher, Constant.user, self.beer.id).serialize())

    @staticmethod
    def serialize_list(items: List[Any] = None, is_me: bool = False):
        return [] if items is None else list(
            map(lambda item: BeerPairing(item[0], item[1]).serialize(), items))