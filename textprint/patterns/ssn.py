from .base import BasePattern
from .pattern_list import PatternTypes


class SocialSecurityNumber(BasePattern):
    """Pattern matching any US SSN in your text data

    The American SSN is 9 digits (###-##-####). It can't
    * Contain any zeroes in any specific group
    * Begin with 666
    * Begin with any value from 900-999
    """

    TYPE = PatternTypes.SSN
    REGEX_FORMAT_STRING = r"(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}"
