import requests
from config.auth import Credentials
from jira.request import JiraRequest


class Client:
    auth: Credentials = None

    def __init__(self, base_url):
        self.base_url = base_url

    def authenticate(self, credentials):
        self.auth = credentials
        return self

    def get_ticket_summary(self, ticket_id):
        request = JiraRequest('issue', ticket_id)
        request.select('summary', 'issuetype')

        return self.get(request)

    def get(self, request: JiraRequest):
        url = f"{self.base_url}{str(request)}"
        return requests.get(url, auth=(self.auth.user, self.auth.password))
