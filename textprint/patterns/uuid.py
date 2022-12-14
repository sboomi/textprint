from typing import List
from uuid import UUID

from .base import BasePattern
from .pattern_list import PatternTypes


class Uuid(BasePattern):
    """Matches a hyphen-separated UUID.

    A UUID is an unique identifier for computer systems.
    Each of them is 128-bits, composed of 5 groups of 16 octets
    in base 16 (32 digits), separated by hyphens.
    """

    TYPE = PatternTypes.UUID
    REGEX_FORMAT_STRING = (
        r"[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-"
        r"[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}"
    )

    def to_uuid(self, target_string: str) -> List[UUID]:
        matches = self.search(target_string)

        return [UUID(m) for m in matches]
