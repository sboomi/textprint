from datetime import date

from textprint.patterns import Date


def test_dates():
    """GIVEN a set of dates
    WHEN Date is searching in the string
    THEN validate dates
    """

    test_dates = {
        "01/01/2000": True,
        "31/01/2000": True,
        "32/01/2000": False,
        "01-1-2000": True,
        "1.1.2019": True,
    }

    date_parser = Date()

    for dates, is_date in test_dates.items():
        match = date_parser.search(dates)
        if is_date:
            assert len(match) == 1
            assert match[0] == dates


def test_dates_with_date_objects():
    """GIVEN parsable cdates
    WHEN Date is running as_date
    THEN return a date object for each coordinate
    """

    test_dates = {
        "01/01/2000": date(2000, 1, 1),
        "31/01/2000": date(2000, 1, 31),
        "01-1-2000": date(2000, 1, 1),
        "1.1.2019": date(2019, 1, 1),
    }

    date_parser = Date()

    for txt_date, exp_date in test_dates.items():
        act_date = date_parser.to_date(txt_date)[0]
        assert act_date == exp_date
