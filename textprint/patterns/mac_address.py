from .pattern_list import PatternTypes
from .base import BasePattern


class MacAddress(BasePattern):
    TYPE = PatternTypes.MAC_ADDRESS
    REGEX_FORMAT_STRING = r"[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5}"
