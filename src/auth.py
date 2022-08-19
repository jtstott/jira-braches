import json
import os
from config import Config


class Credentials:
    def __init__(self, user, password):
        self.user = user
        self.password = password


def parse_file():
    try:
        with open(os.path.expanduser('~/.config/jira-branches/config.json')) as f:
            return json.load(f)
    except FileNotFoundError:
        print('')


def get_credentials(args=None):
    if args.user and args.password:
        return Credentials(args.user, args.password)

    config_credentials = Config.get('auth')
    if config_credentials:
        return Credentials(config_credentials['user'], config_credentials['password'])
