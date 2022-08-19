import json
import os
import string

from helpers.singleton_meta import SingletonMeta


class Config(metaclass=SingletonMeta):
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

    def get(self, key: string):
        return self.config.get(key)

    def get_option(self, key: string):
        return self.get('options').get(key)
