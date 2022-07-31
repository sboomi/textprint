from textprint.patterns import HanUnification


def test_han_characters():
    chrs = ["今", "具", "雇"]

    han_parser = HanUnification()

    for char in chrs:
        match = han_parser.search(char)[0]
        assert char == match
