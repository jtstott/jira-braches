from config.config import Config
from config.template_interpreter import TemplateInterpreter
from jira.ticket.ticket_info import TicketInfo


class BranchName:
    def __init__(self, ticket_info: TicketInfo):
        self.ticket_info = ticket_info
        self.config = Config()

    def __str__(self):
        interpreter = TemplateInterpreter(self.ticket_info)
        return interpreter.format_branch_name()