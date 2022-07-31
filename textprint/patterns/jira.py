from .pattern_list import PatternTypes
from .base import BasePattern


class JiraTicket(BasePattern):
    TYPE = PatternTypes.JIRA_ISSUE_TICKET
