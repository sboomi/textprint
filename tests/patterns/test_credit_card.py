from textprint.patterns import CreditCardNumber


def test_credit_card_numbers():
    numbers = {
        "4569403961014710": True,
        "5191914942157165": True,
        "370341378581367": True,
        "38520000023237": True,
        "6011000000000000": True,
        "3566002020360505": True,
        "1234566660000222": False,
    }

    credit_card_parser = CreditCardNumber()

    for number, is_cc_number in numbers.items():
        match = credit_card_parser.search(number)
        if is_cc_number:
            assert len(match) == 1
            assert match[0] == number
        else:
            assert len(match) == 0
