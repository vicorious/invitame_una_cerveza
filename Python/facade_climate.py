"""
Climate module
"""
import requests
from constant import Constant
from dto.climate_dto import ClimateDTO

class Climate:
    """
    Climate class
    """
    def __init__(self):
        """
        Constructor
        """

    def get_current_weather(self, city):
        """
        get current weather from oepnwheater site
        """
        response = requests.get(Constant.weather_end_point,
                                params={'q': city,
                                        'units': Constant.weather_units,
                                        'appid' : Constant.weather_key})
        json_response = response.json()
        climate_dto = ClimateDTO(weather=json_response["weather"][0],
                                 main=json_response["main"],
                                 wind=json_response["wind"],
                                 city=json_response["name"])
        return climate_dto

    def __str__(self):
        return self.__class__.__name__
