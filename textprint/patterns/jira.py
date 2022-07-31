from .pattern_list import PatternTypes
from .base import BasePattern


class JiraTicket(BasePattern):
    TYPE = PatternTypes.JIRA_ISSUE_TICKET
    REGEX_FORMAT_STRING = r"[A-Z]{2,}-\d+"
