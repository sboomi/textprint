from textprint.patterns import PanFromGstin


def test_valid_pans():
    pans = [
        "22ABCDE1234F1Z5",
        "11GHIJK1234L1Z5",
        "33PQRST5678L1Z5",
        "34UVWXY5678L1Z5",
        "35PQRST5678L1Z5",
        "22ABCDE1234F1Z5",
    ]

    pan_gstin_parser = PanFromGstin()

    for pan in pans:
        match = pan_gstin_parser.search(pan)
        assert len(match) == 1
        assert match[0] == pan
