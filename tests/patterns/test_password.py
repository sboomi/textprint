from textprint.patterns import Password


def test_passwords():
    passwords = {
"lorem": False,
"ipsum": False,
"gr3at@3wdsG": True,
"a": False,
"ab": False,
"abc": False,
"abcd": False,
"abcde": False,
"john doe": False,
"johnny": False,
"abcdefghijklmnopqrst": False
    }

    password_validator = Password(8)

    for password, is_valid_password in passwords.items():
        match = password_validator.search(password)
        if is_valid_password:
            assert len(match) == 1
            assert match[0] == password
        else:
            assert len(match) == 0