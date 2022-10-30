from commands import git
from jira.branch_name import BranchName
from jira.client import Client
from config.config import Config
from jira.ticket.ticket_deserializer import deserialize_ticket


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

            branch_name = str(BranchName(ticket_info))
            branch_exists = git.check_branch(branch_name)
            git.checkout(branch_name, not branch_exists)
        except Exception as error:
            print(f"ERROR: {ticket_id} - {error}")