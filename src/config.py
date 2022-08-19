import json
import os
import string


class Config:
    _instance = None
    config = {}

    def __init__(self):
        self.load_config()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def load_config(self):
        try:
            with open(os.path.expanduser('~/.config/jira-branches/config.json')) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print('Error: Unable to parse config file.')

    @staticmethod
    def get(key: string):
        return Config().config.get(key)
