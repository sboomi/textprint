import os
from pathlib import Path
from typing import Dict, List, Union

from tqdm import tqdm

from .patterns.base import BasePattern
from .sequencer import PatternSequencer


class TextDataset:
    def __init__(
        self,
        text_folder: Union[str, os.PathLike[str]],
        regex_patterns: List[BasePattern],
    ):
        if not Path(text_folder).exists():
            raise FileNotFoundError(f"{text_folder} is not a valid directory")
        self.text_folder = Path(text_folder)
        self.regex_patterns = PatternSequencer(regex_patterns)

    def __len__(self) -> int:
        return len(list(self.text_folder.glob("*.txt")))

    def __getitem__(self, idx: int) -> Path:
        return list(self.text_folder.glob("*.txt"))[idx]

    def search_on_text_file(self, txt_file: Path) -> Dict[str, List[str]]:
        if not txt_file.exists():
            raise FileNotFoundError(f"{txt_file.resolve()} is not a valid filename")

        with open(txt_file, "r") as f:
            text_input = f.read()
            return self.regex_patterns(text_input)

    def search_on_data_folder(self):
        results = {}

        for txt_file in tqdm(self.text_folder.glob("*.txt")):
            results.update(self.search_on_text_file(txt_file))

        return results
