from textprint.patterns import Email


def test_match_and_extract_email():
    emails = {
        "geon@ihateregex.io": ["geon@ihateregex.io"],
        "test@gmail.com mail@test.org": ["test@gmail.com", "mail@test.org"],
        "mail@testing.com": ["mail@testing.com"],
        "hello@": [],
        "@test": [],
        "email@gmail": [],
        "theproblem@test@gmail.com": ["test@gmail.com"],
    }

    email_parser = Email()

    for email, exp_result in emails.items():
        matches = email_parser.search(email)
        assert matches == exp_result
