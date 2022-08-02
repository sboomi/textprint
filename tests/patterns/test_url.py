from textprint.patterns import Url


def test_urls():
    urls = {
        "abcdef": False,
        "www.whatever.com": False,
        "https://github.com/geongeorge/i-hate-regex": True,
        "https://www.facebook.com/": True,
        "https://www.google.com/": True,
        "https://xkcd.com/2293/": True,
        "https://this-shouldn't.match@example.com": False,
        "http://www.example.com/": True,
    }

    url_parser = Url()

    for url, is_act_url in urls.items():
        match = url_parser.search(url)
        if is_act_url:
            assert len(match) == 1
            assert match[0] == url
        else:
            assert len(match) == 0
