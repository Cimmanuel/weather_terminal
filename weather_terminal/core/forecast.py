# This is a class representing the weather 
# forecast data that the parser returns.

from datetime import date
from .forecast_type import ForecastType

class Forecast:
    def __init__(
        self, current_temp, wind, humidity, dew_point=None, pressure=None, visibility=None, 
        high_temp=None, low_temp=None, description='', forecast_date=None, forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._wind = wind
        self._humidity = humidity
        self._dew_point = dew_point
        self._pressure = pressure
        self._visibility = visibility
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._description = description
        self._forecast_type = forecast_type

        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date
    
    @property
    def current_temp(self):
        return self._current_temp

    @property
    def wind(self):
        return self._wind

    @property
    def humidity(self):
        return self._humidity

    @property
    def dew_point(self):
        return self._dew_point

    @property
    def pressure(self):
        return self._pressure

    @property
    def visibility(self):
        return self._visibility

    @property
    def description(self):
        return self._description

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")

    def __str__(self):
        temperature = None
        dew_pressure_visibility = None
        offset = ' ' * 4
        
        if self._forecast_type == ForecastType.TODAY:
            temperature = (
                f'{offset}Current temperature: {self._current_temp}\xb0\n'
                f'{offset}High {self._high_temp}\xb0 / '
                f'Low {self._low_temp}\xb0 '
            )
            dew_pressure_visibility = (
                f'{offset}Dew Point: {self._dew_point} / Pressure: {self._pressure} / Visibility: {self._visibility}\n\n'
                f'{offset}NB: Dew Point, Pressure, and Visibility will be displayed as though temperature values were in Fahrenheit\n'
            )
        else:
            temperature = (
                f'{offset}High {self._high_temp}\xb0 / '
                f'Low {self._low_temp}\xb0 '
            )
            dew_pressure_visibility = (
                f'{offset}Dew Point: Not available / Pressure: Not available / Visibility: Not available\n'
            )

        return (
            f'\n>> {self.forecast_date}\n'
            f'{temperature}'
            f'({self._description})\n'
            f'{offset}Wind: {self._wind} / Humidity: {self._humidity}\n'
            f'{dew_pressure_visibility}'
        )
