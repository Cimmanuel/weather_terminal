from .base_enum import BaseEnum
from enum import auto, unique

@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()