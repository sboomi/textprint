from textprint.patterns import PhoneNumber


def test_series_of_phone_numbers():
    """GIVEN series of phone numbers
    WHEN PhoneNumber is searching
    THEN the proper result must be displayed
    """
    phone_numbers = {
        "+919367788755": True,
        "8989829304": True,
        "+16308520397": True,
        "786-307-3615": True,
        "789": False,
        "123765": False,
        "1-1-1": False,
        "+982": False,
    }

    phone_number_parser = PhoneNumber()

    for phone_number, is_phone_number in phone_numbers.items():
        matched_strs = phone_number_parser.search(phone_number)
        if is_phone_number:
            assert len(matched_strs) == 1
            assert matched_strs[0] == phone_number


def test_series_of_phone_numbers_e164():
    """GIVEN series of phone numbers
    WHEN PhoneNumber is searching with E164 option enabled
    THEN the proper result must be displayed
    """
    phone_numbers = {
        "+919367788755": True,
        "8989829304": False,
        "+16308520397": True,
        "786-307-3615": False,
        "+14155552671": True,
        "+551155256325": True,
    }

    phone_number_parser = PhoneNumber(is_e164=True)

    for phone_number, is_phone_number in phone_numbers.items():
        matched_strs = phone_number_parser.search(phone_number)
        if is_phone_number:
            assert len(matched_strs) == 1
            assert matched_strs[0] == phone_number
