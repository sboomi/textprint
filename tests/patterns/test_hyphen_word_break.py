from textprint.patterns import HyphenWordBreak


def test_hyphens_in_text():
    sample_text = """It illustrates not only the impor-
tance of the golden rule for asking questions—Ask what you want
to know, not something else—but also, more important, the ambi-
guities of language and the powerful force of context in interpret-
ing the meaning of questions and answers. Our colleague had
"""

    hyphen_parser = HyphenWordBreak()

    matches = hyphen_parser.search(sample_text)
    assert len(matches) == 3


def test_rebuild_string_on_a_line():
    sample_text = """It illustrates not only the impor-
tance of the golden rule for asking questions—Ask what you want
to know, not something else—but also, more important, the ambi-
guities of language and the powerful force of context in interpret-
ing the meaning of questions and answers. Our colleague had
"""

    result = (
        """It illustrates not only the importance of the golden rule for """
        """asking questions—Ask what you want
to know, not something else—but also, more important, the ambiguities of """
        """language and the powerful force of context in interpreting the meaning """
        """of questions and answers. Our colleague had
        """
    )

    hyphen_parser = HyphenWordBreak()

    act_result = hyphen_parser.reassemble_text(sample_text)
    assert result.strip() == act_result.strip()
