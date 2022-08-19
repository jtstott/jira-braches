from requests import Response


class TicketInfo:
    def __init__(self, ticket_key, ticket_summary, ticket_type):
        self.key = ticket_key
        self.summary = ticket_summary
        self.type = ticket_type


def deserialize_ticket(response: Response) -> TicketInfo:
    if response.ok:
        response_data = response.json()
        ticket_key = str(response_data['key'])
        ticket_summary = str(response_data['fields']['summary'])
        ticket_type = str(response_data['fields']['issuetype']['name'])
        return TicketInfo(ticket_key, ticket_summary, ticket_type)

    if response.status_code == 401 or response.status_code == 403:
        raise Exception('Unable to authenticate request to Jira. Check credentials')

    raise Exception(
        f"Unable to retrieve ticket details from Jira. HTTP status {response.status_code} - {response.json()['errorMessages']}")
