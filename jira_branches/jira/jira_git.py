from commands import git
from jira.client import Client
from config.config import Config
from jira.serializers import deserialize_ticket, TicketInfo


class JiraGitService:

    def __init__(self, client: Client):
        self.client = client
        self.config = Config()

    def checkout_ticket_branch(self, ticket_id):
        prefix = self.config.get_option('idPrefix') or ''
        ticket_id = f"{prefix}{ticket_id.replace(prefix, '')}"
        try:
            response = self.client.get_ticket_summary(ticket_id)
            ticket_info = deserialize_ticket(response)

            branch_name = str(BranchNameFormatter(ticket_info))
            branch_exists = git.check_branch(branch_name)
            git.checkout(branch_name, not branch_exists)
        except Exception as error:
            print(f"ERROR: {ticket_id} - {error}")


class BranchNameFormatter:
    char_replacements = {
        ' ': '-',
        '--': '-',
        '---': '-',
        '&': 'and',
        '>': 'gt',
        '/': '-'
    }

    char_forbidden = [
        '..',
        '~',
        '^',
        ':',
        '[',
        ']',
        '?',
        '*',
        '.',
        '@{',
        '\\',
        '|',
        '(',
        ')'
    ]

    summary = ''

    def __init__(self, ticket_info: TicketInfo):
        self.ticket_info = ticket_info
        self.summary = self.ticket_info.summary.strip()
        self.config = Config()

    def __str__(self):
        return self.format_branch_name()

    def format_branch_name(self):
        branch_name = self.config.get('branchTemplate')
        valid_options = {
            'id': self.ticket_info.key,
            'type': self.map_type(),
            'summary': self.format_summary()
        }

        for option, value in valid_options.items():
            branch_name = branch_name.replace(f"[{option}]", value)

        return branch_name

    def map_type(self):
        ticket_type = self.ticket_info.type
        return self.map_configured_types(ticket_type)

    def format_summary(self):
        self.strip_forbidden_chars()
        self.replace_chars()

        return self.summary.lower()

    def replace_chars(self):
        for target, replacement in self.char_replacements.items():
            self.summary = self.summary.replace(target, replacement)

    def strip_forbidden_chars(self):
        for forbidden in self.char_forbidden:
            self.summary = self.summary.replace(forbidden, '')

    def map_configured_types(self, ticket_type):
        type_map = self.config.get_option('mapTypes')
        if type_map:
            if ticket_type in type_map:
                return type_map[ticket_type]

            if '*' in type_map:
                return type_map['*']

        return ticket_type
