from typing import List, NamedTuple

from .base import BasePattern
from .pattern_list import PatternTypes


class Version(NamedTuple):
    major: int
    minor: int
    patch: int
    prerelease: str = ""
    metadata: str = ""


class SemanticVersioning(BasePattern):
    """Matches a semantic versioning pattern
    according to https://semver.org/

    This is a strict versioning only working as a validator. The version must be
    on separate lines.
    """

    TYPE = PatternTypes.SEMANTIC_VERSIONING
    REGEX_FORMAT_STRING = (
        r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0"
        r"|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*"
        r"|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+"
        r"(?:\.[0-9a-zA-Z-]+)*))?$"
    )

    def as_object(self, target_string: str) -> List[Version]:
        """Returns each validated version as an object featuring each of the groups:

        1. Major version
        2. Minor version
        3. Patch
        4. Prerelease
        5. Metadata

        :param target_string: The version to look over. Should be strict (no spaces
            or words in between)
        :type target_string: str
        :return: List of NamedTuples with each parameter
        :rtype: List[Version]
        """
        if not hasattr(self, "regex_pattern"):
            self.compile()

        regex_matches = self.regex_pattern.finditer(target_string)

        version_matches = []
        for m in regex_matches:
            major, minor, patch, *args = [
                int(m.group(grp_n)) if grp_n < 4 else m.group(grp_n)
                for grp_n in range(1, len(m.groups()) + 1)
            ]
            if args:
                args = ["" if arg is None else arg for arg in args]
            version_matches.append(Version(major, minor, patch, *args))

        return version_matches
