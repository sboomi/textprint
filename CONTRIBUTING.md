# Issues

# Development

The only requirements needed to start the packages in development mode are

- [Poetry](https://python-poetry.org/)
- Python 3.9 and above

You can then fork the repository on your account and clone it on your local computer.

To install all dependencies, launch

```shell
poetry install
```

which automatically creates an environment in your Poetry venv directoy if you left the installation by default.

Install pre-commit hooks with

```shell
poetry run pre-commit install
```

Make sure every test passes with

```shell
poetry run python -m pytest tests
```

Once everything is settled, you can start coding. 😉

## Creating your own pattern module

By definition, every module inherits from `textprint.patterns.base.BasePattern`. If you want to design a new module, you can override the following:

- `REGEX_FORMAT_STRING` which is the regex pattern meant to be compiled.
- The constructor `__init__` if you need extra parameters like a username.
  - In the same vein, you can override `flags` in `super().__init__(flags)`, if you need an extra flag like `re.I`.
- Abstract method `_compile` can be overriden especially in the case where instance arguments are provided.
- `TYPE` which needs an enum value from `textprint.patterns.pattern_list.PatternTypes`. Feel free to add your own if you think your pattern isn't related to any of the above components.

Finally do not forget to document and import your module in the `__init__.py` file.

Example with `textprint.patterns.username.Username`:

```python
import re

from .base import BasePattern
from .pattern_list import PatternTypes


class Username(BasePattern):
    """Pattern checking against any type of username with a defined length

    :param min_len: The minimal length of the username
    :type min_len: int
    :param max_len: The maximal length of the username
    :type max_len: int
    """

    TYPE = PatternTypes.USERNAME
    REGEX_FORMAT_STRING = r"\b[a-z0-9_-]{min_len,max_len}\b"

    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__()

    def _compile(self) -> str:
        return self.REGEX_FORMAT_STRING.replace("min_len", str(self.min_len)).replace(
            "max_len", str(self.max_len)
        )

```

After editing code, don't forget to run some checks using the following commands:

```shell
poetry run black .
poetry run isort . --profile black
poetry run flake8 .
poetry run bandit .
poetry run safety check
```

## Generate docs

The docs can be generated with the following command:

```shell
poetry run sphinx-apidoc -o docs textprint/
```
