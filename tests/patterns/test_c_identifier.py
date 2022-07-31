from textprint.patterns import CLanguageIdentifier


def test_c_identifiers():
    tokens = {
        "abc123": True,
        "PascalCase": True,
        "camelCase": True,
        "snake_case": True,
        "_test": True,
        "_": True,
        "123abc": False,
    }

    c_parser = CLanguageIdentifier()

    for token, is_c_like in tokens.items():
        match = c_parser.search(token)
        if is_c_like:
            assert len(match) == 1
            assert match[0] == token
