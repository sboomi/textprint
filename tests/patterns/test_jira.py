from textprint.patterns import JiraTicket


def test_ticket_entries():
    tickets = {
        "DAT-123": True,
        "A-333": False,
        "AB-333": True,
        "aka-48": False,
        "PROJECT-6": True,
        "TST 000": False,
    }

    jira_parser = JiraTicket()

    for ticket, is_jira_ticket in tickets.items():
        match = jira_parser.search(ticket)
        if is_jira_ticket:
            assert len(match) == 1
            assert match[0] == ticket
