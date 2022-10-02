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
  // Branch name template with jira variable tokens
  "branchTemplate": "",
  "options": {
    // Jira ticket ID prefix
    "idPrefix": "",
    "mapTypes": {}
  }
}
```

## Configuration

### ID Prefix

The `idPrefix` can be used if all Jira ticket IDs start with the same prefix, meaning the prefix can be omitted when the
tool is executed.

For example if a all ticket IDs start with the prefix `MY-PROJECT-`, and the id_prefix is configured to this, then
branches can be created for a ticket with ID `MY-PROJECT-1078` by just passing `1078` as the argument.

### Branch template

The `branchTemplate` must be configured to the format the branch name will be created to. Any string is valid (excluding
forbidden branch name characters), and tokens can be used to represent Jira ticket variables.

Jira ticket variables can be used in the name template using the following syntax: `[var]`

For example, given a ticket has an ID '_ID-123_' and a summary '_Great feature_', the following branch
template: `"feat/[id]-[summary]"` would generate the branch name `feat/ID-123-great-feature`.

It is important to note that spaces will always be replaced by dashes (`-`), and summaries will loose their case
sensitivity but ID's will maintain it.

### Options

#### Map types

The `mapTypes` config option allows jira ticket types to be mapped to other values for branch name generation. For
example a ticket type of `Story` may want to be mapped in the branch name to `feature`, e.g;

```json
{
  "mapTypes": {
    "Story": "feature"
  }
}
```

This mapping will be invoked anytime the ticket type variable is used in the branch template.

The wildcard `*` can be used as a default case. If a key of `*` is set for `mapTypes`, the value set for this default
case will be applied to the type variable when no other type mappings are matched. Without a default case, if no `mapType`
mappings are found then the original value for the ticket type is used.

## Jira variables

The Jira variables (and therefore branch name tokens) currently supported are:

- `id`: Ticket ID
- `summary`: Ticket summary/title
- `type`: Ticket type (e.g. story, task, bug etc...)