# Base enumeration overriding the _generate_next_value method

from enum import Enum

class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_value):
        return name