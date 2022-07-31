import re
from .base import BasePattern
from .pattern_list import PatternTypes


class Username(BasePattern):
    """Pattern checking against an username with a defined length"""

    TYPE = PatternTypes.USERNAME
    REGEX_FORMAT_STRING = r"^[a-z0-9_-]{min_len,max_len}$"

    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__()

    def _compile(self) -> str:
        return self.REGEX_FORMAT_STRING.replace("min_len", str(self.min_len)).replace(
            "max_len", str(self.max_len)
        )


class DiscordUsername(BasePattern):
    """Variant of the Username pattern checking against any Discord username in
    text data"""

    TYPE = PatternTypes.USERNAME
    REGEX_FORMAT_STRING = r"^.{3,32}#[0-9]{4}$"

    def __init__(self):
        super().__init__(flags=[re.M, re.I])

    def _compile(self) -> str:
        return self.REGEX_FORMAT_STRING
