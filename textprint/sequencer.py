from typing import Dict, List

from .patterns.base import BasePattern


class PatternSequencer:
    def __init__(self, patterns: List[BasePattern]) -> None:
        self.patterns = patterns

    def __call__(self, target_string: str) -> Dict[str, List[str]]:
        results = {}

        for pattern in self.patterns:
            results[pattern.__class__.__name__] = pattern.search(target_string)

        return results

    def __len__(self) -> int:
        return len(self.patterns)
