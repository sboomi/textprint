from .pattern_list import PatternTypes
from .base import BasePattern


class MacAddress(BasePattern):
    TYPE = PatternTypes.MAC_ADDRESS
