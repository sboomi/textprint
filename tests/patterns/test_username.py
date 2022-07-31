from textprint.patterns import Username, DiscordUsername


def test_series_of_usernames():
    """GIVEN series of usernames
    WHEN Username is searching
    THEN the proper result must be displayed
    """
    usernames = {
        "lorem": True,
        "ipsum": True,
        "gr3at": True,
        "a": False,
        "ab": False,
        "abcd": True,
        "abcde": True,
        "john doe": False,
        "johnny": True,
        "abcdefghijklmnopqrst": False,
    }

    username_parser = Username(3, 15)

    for username, is_username in usernames.items():
        matched_strs = username_parser.search(username)
        if is_username:
            assert len(matched_strs) == 1
            assert matched_strs[0] == username


def test_discord_usernames():
    usernames = ["Disコルド#0001", "KiBender#1234", "SkankHunt42#2134"]

    username_parser = DiscordUsername()

    for username in usernames:
        matched_strs = username_parser.search(username)
        assert len(matched_strs) == 1
        assert matched_strs[0] == username
