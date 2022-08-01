from .base import BasePattern
from .pattern_list import PatternTypes


class Password(BasePattern):
    """Matches against a modern password with customizable minimal length

    A modern password must be hard to guess and thus have at least

    * One upper case letter
    * One lower case letter
    * One number
    * One special character

    :param min_len: minimal length for the password
    :type min_len: int
    """

    TYPE = PatternTypes.PASSWORD
    REGEX_FORMAT_STRING = (
        r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{min_len,}"
    )

    def __init__(self, min_len: int):
        super().__init__()
        self.min_len = min_len

    def _compile(self) -> str:
        return self.REGEX_FORMAT_STRING.replace("min_len", str(self.min_len))
