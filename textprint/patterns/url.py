from typing import Dict, List
from urllib.parse import ParseResult, urlparse

import requests

from .base import BasePattern
from .pattern_list import PatternTypes


class Url(BasePattern):
    """
    Matches any URL with the HTTP/HTTPS protocol in the text data.
    """

    TYPE = PatternTypes.URL
    REGEX_FORMAT_STRING = (
        r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
        r"[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
    )

    def as_url_objects(self, target_string: str) -> List[ParseResult]:
        """If URLs are detected, returns them as a ParseResult object

        See Python's `urllib.parse` module for more details.

        :param target_string: The string to perform a research on
        :type target_string: str
        :return: A list of ParseResult objects
        :rtype: List[ParseResult]
        """
        matches = self.search(target_string)

        return [urlparse(m) for m in matches]

    def get_status_codes(self, target_string: str) -> Dict[str, int]:
        """Quickly makes a survey of every URL found in the text and
        performs a GET request on every single one of them. Returns the URLs
        and their respective status codes.

        For more information on status codes,
        check https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

        :param target_string: The string to perform a research on
        :type target_string: str
        :return: A dict with URLs and their status codes
        :rtype: Dict[str, int]
        """
        matches = self.search(target_string)

        status_codes = {url: 0 for url in list(set(matches))}

        for url in status_codes:
            res = requests.get(url)
            status_codes[url] = res.status_code

        return status_codes
