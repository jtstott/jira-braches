import git
from client import Client
from config import Config
from serializers import deserialize_ticket, TicketInfo


class JiraGitService:

    def __init__(self, client: Client):
        self.client = client

    def checkout_ticket_branch(self, ticket_id):
        prefix = Config.get('prefix') or ''
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

    def __str__(self):
        return f"{self.map_type()}/{self.ticket_info.key}-{self.format_summary()}"

    def map_type(self):
        ticket_type = self.ticket_info.type

        match ticket_type:
            case 'Story':
                return 'feature'
            case 'Bug':
                return 'bugfix'
            case _:
                return 'task'

    def format_summary(self):
        self.replace_chars()
        self.strip_forbidden_chars()

        return self.summary.lower()

    def replace_chars(self):
        for target, replacement in self.char_replacements.items():
            self.summary = self.summary.replace(target, replacement)

    def strip_forbidden_chars(self):
        for forbidden in self.char_forbidden:
            self.summary = self.summary.replace(forbidden, '')
