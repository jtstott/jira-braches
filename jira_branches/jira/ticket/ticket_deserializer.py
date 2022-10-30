from requests import Response

from jira.ticket.ticket_info import TicketInfo


def deserialize_ticket(response: Response) -> TicketInfo:
    if response.ok:
        response_data = response.json()
        ticket_key = str(response_data['key'])
        ticket_summary = str(response_data['fields']['summary'])
        ticket_type = str(response_data['fields']['issuetype']['name'])
        return TicketInfo(ticket_key, ticket_summary, ticket_type)

    if response.status_code == 401 or response.status_code == 403:
        raise Exception('Unable to authenticate api to Jira. Check credentials')

    raise Exception(
        f"Unable to retrieve ticket details from Jira. HTTP status {response.status_code} - {response.json()['errorMessages']}")
