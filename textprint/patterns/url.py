from .pattern_list import PatternTypes
from .base import BasePattern


class Url(BasePattern):
    TYPE = PatternTypes.URL
    REGEX_FORMAT_STRING = (
        r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
        r"[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
    )
