from textprint.patterns import SemanticVersioning


def test_semver_syntax():
    semver_candidates = {
"1": False,
"0.0.4": True,
"1.2.3": True,
"1.2": False,
"10.20.30": True,
"01.1.1": False,
"1.1.2-prerelease+meta": True,
"1.1.2+meta": True,
"9.8.7-whatever+meta+meta": False,
"1.0.0-alpha": True,
"1.0.0-alpha.beta": True,
"1.0.0-alpha.1": True,
"1.0.0-alpha.0valid": True,
"1.0.0-rc.1+build.1": True,
"1.2.3-beta": True,
"10.2.3-DEV-SNAPSHOT": True,
"1.2.3.DEV":  False,
"1.2.3-0123": False,
"1.2.3-SNAPSHOT-123": True,
"1.0.0": True,
"2.0.0+build.1848": True,
"2.0.1-alpha.1227": True,
"1.0.0-alpha+beta": True,
"1.0.0-alpha_beta": False,
"1.2.3----RC-SNAPSHOT.12.9.1--.12+788": True,
"1.2.3----R-S.12.9.1--.12+meta": True,
"1.2-SNAPSHOT": False,
"1.2.31.2.3----RC-SNAPSHOT.12.09.1--..12+788": False
    }

    semver_parser = SemanticVersioning()

    for candidate, is_semver in semver_candidates.items():
        match = semver_parser.search(candidate)
        if is_semver:
            assert len(match) == 1
            assert match[0] == candidate
        else:
            assert len(match) == 0