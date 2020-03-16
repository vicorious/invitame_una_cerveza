"""
Constant module
"""
class Constant:
    """
    Constant class
    """
    user_default = 'postgres'
    ip_default = 'localhost'
    port_default = '5432'
    db_default = 'invitame_una_cerveza'
    password_default = '*postgre123*'
    postgre_exe_file = '/exe/postgresql-12.1-1-windows-x64.exe'
    user = 'Alejo'
    weather_key = '8cde928e3f9fdc6ce35a4f5d0375ac62'
    weather_end_point = 'http://api.openweathermap.org/data/2.5/weather'
    weather_units = 'metric'

    def __init__(self):
        """
        Constructor
        """
    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.user_default, self.ip_default, self.port_default,
                     self.db_default, self.password_default,
                     self.postgre_exe_file, self.user, self.weather_key,
                     self.weather_end_point, self.weather_units))
