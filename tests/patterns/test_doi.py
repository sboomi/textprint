from textprint.patterns import DigitalObjectIdentifier


def test_dois():
    dois = [
        "10.1000/123456",
        "10.1038/issn.1476-4687",
        "10.1111/dome.12082",
        "10.1111/josi.12122",
    ]

    doi_parser = DigitalObjectIdentifier()

    for doi in dois:
        match = doi_parser.search(doi)
        assert len(match) == 1
        assert match[0] == doi
