# coding: utf-8
from __future__ import absolute_import
import sys

if __package__ == '' or __package__ is None:
    import os

    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from pundler.config import Config
from pundler.commands import Install, List
from pundler.exceptions import NotCommandError
from pundler.parser import Parser


def usage():
    print("""
NAME
    pundle - Python Package Management

SYNOPSIS
    pundle COMMAND OPTIONS
""")


def main():
    parser = Parser()
    options, args = parser.parse()
    if not len(args):
        usage()
        return 0

    command_name = args[0]
    if command_name == 'install':
        if options.environment:
            config = Config(pyfile=options.filename,
                            environment=options.environment)
        else:
            config = Config(pyfile=options.filename)
        command = Install(config)

    elif command_name == "list":
        command = List()

    else:
        raise NotCommandError('command({}) not found.'.format(command_name))

    command.run()


if __name__ == "__main__":
    sys.exit(main() or 0)
