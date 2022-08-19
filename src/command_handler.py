import sys

from auth import get_credentials
from client import Client
from config import Config
from jira_git import JiraGitService


def checkout_branch(opts, args):
    try:
        ticket_id = args[0]
    except IndexError:
        print("Argument 0 missing. Please specify a ticket ID to create the branch from.")
        sys.exit()

    client = Client(Config.get('baseUrl')).authenticate(get_credentials(opts))
    JiraGitService(client).checkout_ticket_branch(ticket_id)


commands = {
    'branch': checkout_branch
}
