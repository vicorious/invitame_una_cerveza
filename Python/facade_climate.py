from constant import Constant
from dto.climate_dto import ClimateDTO
import requests
class Climate:

    def __init__(self):
        pass
        
    def getCurrentWeather(self, city):
        response = requests.get(Constant.weather_end_point,params={'q': city, 'units': Constant.weather_units, 'appid' : Constant.weather_key})
        json_response = response.json()
        climate_dto = ClimateDTO(weather = json_response["weather"][0], main = json_response["main"], wind = json_response["wind"], city = json_response["name"])
        return climate_dto
    