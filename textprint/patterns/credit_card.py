from .pattern_list import PatternTypes
from .base import BasePattern


class CreditCardNumber(BasePattern):
    TYPE = PatternTypes.CREDIT_CARD_NUMBER
