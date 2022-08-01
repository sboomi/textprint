from .base import BasePattern
from .pattern_list import PatternTypes


class MacAddress(BasePattern):
    """Matches against mac addresses in the text data

    :param BasePattern: _description_
    :type BasePattern: _type_
    """

    TYPE = PatternTypes.MAC_ADDRESS
    REGEX_FORMAT_STRING = r"[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5}"
