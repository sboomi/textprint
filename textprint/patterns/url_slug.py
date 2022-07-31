from .pattern_list import PatternTypes
from .base import BasePattern


class UrlSlug(BasePattern):
    TYPE = PatternTypes.URL_SLUG
    REGEX_FORMAT_STRING = r"[a-z0-9]+(?:-[a-z0-9]+)*"
