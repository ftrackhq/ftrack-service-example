# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import argparse
import logging
import sys
import warnings
import time

import ftrack_api

import healthcheck as _healthcheck
from .actions.example_action import (
    ExampleAction as _ExampleAction
)


def main(arguments=None):
    '''ftrack service example.'''
    if arguments is None:
        arguments = []

    parser = argparse.ArgumentParser()

    # Allow setting of logging level from arguments.
    loggingLevels = {}
    for level in (
        logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING,
        logging.ERROR, logging.CRITICAL
    ):
        loggingLevels[logging.getLevelName(level).lower()] = level

    parser.add_argument(
        '-v', '--verbosity',
        help='Set the logging output verbosity.',
        choices=loggingLevels.keys(),
        default='info'
    )

    parser.add_argument(
        '--healthcheck',
        dest='healthcheck',
        help='Run healthcheck.',
        action='store_true',
        default=False
    )

    namespace = parser.parse_args(arguments)

    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
        level=loggingLevels[namespace.verbosity],
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    session = ftrack_api.Session(auto_connect_event_hub=True)
    _healthcheck.register(session)
    if namespace.healthcheck:
        _healthcheck.publish(session)
        return

    actions = (
        _ExampleAction(session),
    )

    for action in actions:
        action.register()



    # Wait for events
    logging.info(
        'Registered actions and listening for events. Use Ctrl-C to abort.'
    )
    session.event_hub.wait()


if __name__ == '__main__':
    raise SystemExit(
        main(sys.argv[1:])
    )
