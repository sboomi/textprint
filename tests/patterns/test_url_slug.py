from textprint.patterns import UrlSlug


def test_url_slugs():
    url_slugs = {
        "best-way": True,
        "best-d4y": True,
        "my-1ife": True,
        "@t-the-sky": False,
        "at-the--sky": False,
        "-": False,
        "a": True,
        "fly-": False,
    }

    url_slug_parser = UrlSlug()

    for url_slug, is_act_url_slug in url_slugs.items():
        match = url_slug_parser.search(url_slug)
        if is_act_url_slug:
            assert len(match) == 1
            assert match[0] == url_slug
        else:
            assert len(match) == 0
