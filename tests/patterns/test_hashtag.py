from textprint.patterns import Hashtag


def test_hashtags():
    hashtags = {
        "#Hello": "#Hello",
        "#Photography_Daily": "#Photography_Daily",
        "#Photography Daily": "#Photography",
        "#hashtag123": "#hashtag123",
        "#DontLookUp": "#DontLookUp",
        "#dontlookup": "#dontlookup",
        "#dont_look_up": "#dont_look_up",
        "#justice4me": "#justice4me",
        "#_": "#_",
        "NotAHashtag": "",
        "#dont look up": "#dont",
    }

    hashtag_parser = Hashtag()

    for hashtag, parsed_hashtag in hashtags.items():
        match = hashtag_parser.search(hashtag)
        if parsed_hashtag:
            assert match[0] == parsed_hashtag
