from .pattern_list import PatternTypes
from .base import BasePattern


class IpAddress(BasePattern):
    TYPE = PatternTypes.IP_ADDRESS
