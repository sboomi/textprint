import re
from .pattern_list import PatternTypes
from .base import BasePattern


class Hashtag(BasePattern):
    TYPE = PatternTypes.HASHTAG
    REGEX_FORMAT_STRING = r"#\b[^\s!@#$%^&*(),.?\":{}|<>]*\b"

    def __init__(self):
        super().__init__([re.M, re.I])
