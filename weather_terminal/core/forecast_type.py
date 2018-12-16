# This is the application model that's representing
# all the information this application will scrape
# from the weather website.

from enum import Enum, unique

@unique
class ForecastType(Enum):
    TODAY = 'today'
    FIVEDAYS = '5day'
    TENDAYS = '10day'
    WEEKEND = 'weekend'