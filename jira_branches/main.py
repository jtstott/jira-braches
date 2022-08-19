#!/usr/bin/python
import argparse
import sys
from commands import command_handler


def main(command, argv):
    opts, all_args = parseargs()
    command_handler.commands[command](opts, argv)


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='user')
    parser.add_argument('-p', dest='password')
    return parser.parse_known_args()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
