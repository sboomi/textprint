from .pattern_list import PatternTypes
from .base import BasePattern


class CLanguageIdentifier(BasePattern):
    TYPE = PatternTypes.C_IDENTIFIER
