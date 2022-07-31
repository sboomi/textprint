from textprint.patterns import Ascii


def test_ascii_series():
    """GIVEN a series of words with ASCI and non-ASCII characters
    with their non-ASCII filtered form
    WHEN Ascii parser is ran on each one of them
    THEN the word m
    """
    mixed_words = {
        "lor難em": "lorem",
        "ipsum": "ipsum",
        "說上難車中防水回大石在該是並": "",
        "a - = ? / ~": "a - = ? / ~",
        "ab": "ab",
        "難": "",
        "ഇത് മലയാളം": " ",
        "Christmas": "Christmas",
    }

    ascii_parser = Ascii()

    for word, ascii_only in mixed_words.items():
        matched_strs = ascii_parser.search(word)
        assert ascii_only == "".join(matched_strs)
