from config.config import Config


class TemplateInterpreter:
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

    config = Config()

    def __init__(self, ticket_info):
        self.ticket_info = ticket_info

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
        summary = self.ticket_info.summary.strip()
        summary = self.strip_forbidden_chars(summary)
        summary = self.replace_chars(summary)

        return summary.lower()

    def map_configured_types(self, ticket_type):
        type_map = self.config.get_option('mapTypes')
        if type_map:
            if ticket_type in type_map:
                return type_map[ticket_type]

            if '*' in type_map:
                return type_map['*']

        return ticket_type

    def replace_chars(self, string: str) -> str:
        for target, replacement in self.char_replacements.items():
            string = string.replace(target, replacement)

        return string

    def strip_forbidden_chars(self, string: str) -> str:
        for forbidden in self.char_forbidden:
            string = string.replace(forbidden, '')

        return string
