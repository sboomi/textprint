from .base import BasePattern
from .pattern_list import PatternTypes


class PortNumber(BasePattern):
    """Matches a port number from a socket.

    A port number is a uint16 value ranging from 0 to 65535.
    """

    TYPE = PatternTypes.PORT_NUMBER
    REGEX_FORMAT_STRING = (
        r"\b((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|"
        r"(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))\b"
    )
