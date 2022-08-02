from textprint.patterns import SocialSecurityNumber


def test_ssns():
    ssn_candidates = {
        "123-45-6789": True,
        "123 45 6789": False,
        "333-22-4444": True,
        "aaa-bbb-cccc": False,
        "900-58-4564": False,
        "999-58-4564": False,
        "000-45-5454": False,
    }

    ssn_parser = SocialSecurityNumber()

    for candidate_ssn, is_ssn in ssn_candidates.items():
        match = ssn_parser.search(candidate_ssn)
        if is_ssn:
            assert len(match) == 1
            assert match[0] == candidate_ssn
        else:
            assert len(match) == 0
