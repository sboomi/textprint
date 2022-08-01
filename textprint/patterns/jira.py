from .base import BasePattern
from .pattern_list import PatternTypes


class JiraTicket(BasePattern):
    """Matches against Jira issue ticket slugs"""

    TYPE = PatternTypes.JIRA_ISSUE_TICKET
    REGEX_FORMAT_STRING = r"[A-Z]{2,}-\d+"
