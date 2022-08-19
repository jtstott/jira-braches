# Jira branches

This project enables the creation and checkout of git branches based on Jira ticket data. Git branch name patterns can
be defined with tokens representing attributes of Jira tickets.

For example: `feature/PROJECT-1078-some-jira-ticket-title`

## Installation

1. Pull the repository
2. Define your configuration in the file: `~/.config/jira-branches/config.json`. The configuration should be in the
   following format:

```json lines
{
  "auth": {
    // Jira username
    "user": "",
    // Jira user password
    "password": ""
  },
  // Jira instance base URL
  "baseUrl": "",
  "options": {
    // Jira ticket ID prefix
    "id_prefix": ""
  }
}
```

## Configuration

### ID Prefix

The `id_prefix` can be used if all Jira ticket IDs start with the same prefix, meaning the prefix can be omitted when
the tool is executed.

For example if a all ticket IDs start with the prefix `MY-PROJECT-`, and the id_prefix is configured to this, then
branches can be created for a ticket with ID `MY-PROJECT-1078` by just passing `1078` as the argument.
