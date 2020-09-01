"""
Promotion roe module
"""
from typing import Any, List
from entities.promotion import Promotion
from entities.bar import Bar
from entities.beer import Beer
from constant import Constant

class PromotionBeerBar():

    promotion = None
    beer = None
    bar = None
    """
    PromotionBeerBar
    """
    def __init__(self, promotion, beer, bar):
        """
        Constructor
        """
        self.promotion = promotion
        self.beer = beer
        self.bar = bar

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))
    
    def serialize(self):
        return dict(promotion=Promotion(self.promotion.id,self.promotion.duration, self.promotion.beer_id, Constant.user).serialize(),
                    beer=Beer(self.beer.id, self.beer.name, self.beer.pint_price, self.beer.cup330_price,
                     self.beer.giraffe_price, self.beer.pitcher_price,
                     self.beer.bar_id, self.beer.beer_type_id, self.beer.avb,
                     self.beer.ibu, self.beer.srm,
                     self.beer.description, self.beer.image,
                     self.beer.pint, self.beer.cup330,
                     self.beer.giraffe, self.beer.pitcher, Constant.user).serialize(),
                    bar=Bar(self.bar.id, self.bar.name, self.bar.open_date, self.bar.opening_hour,
                     self.bar.close_hour, self.bar.open_days,
                     self.bar.payment_product, self.bar.description, self.bar.image,
                     self.bar.address, self.bar.points,
                     self.bar.facebook, self.bar.twitter,
                     self.bar.instagram, self.bar.emergency_number, Constant.user).serialize())

    @staticmethod
    def serialize_list(items: List[Any] = None, is_me: bool = False):
        return [] if items is None else list(
            map(lambda item: PromotionBeerBar(item[0], item[1], item[2]).serialize(), items))