from .pattern_list import PatternTypes
from .base import BasePattern


class BitcoinAddress(BasePattern):
    REGEX_FORMAT_STRING = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
    TYPE = PatternTypes.BITCOIN_ADDRESS
