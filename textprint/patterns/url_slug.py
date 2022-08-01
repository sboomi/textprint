from .base import BasePattern
from .pattern_list import PatternTypes


class UrlSlug(BasePattern):
    """Matches an URL slug

    A slug is the endpoint of an URL, usually indicating a unique object
    like the user's ID, or the user's post's ID.
    """

    TYPE = PatternTypes.URL_SLUG
    REGEX_FORMAT_STRING = r"[a-z0-9]+(?:-[a-z0-9]+)*"
