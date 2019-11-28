from constant import Constant
import requests
class Climate:

    def __init__(self):
        pass
        
    def getCurrentWeather(self, city):
        response = requests.get(Constant.weather_end_point,params={'q': city})
        json_response = response.json()