from .pattern_list import PatternTypes
from .base import BasePattern


class Email(BasePattern):
    REGEX_FORMAT_STRING = (
        r"""(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+")"""
        r""")@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]"""
        r"""+\.)+[a-zA-Z]{2,}))"""
    )
    TYPE = PatternTypes.EMAIL
