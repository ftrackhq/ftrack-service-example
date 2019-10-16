# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import logging
import time

import ftrack_api


# Name to use for the healthcheck topic.
HEALTH_TOPIC = 'com.ftrack.service.example.health'

# Global variable to track when healthcheck reply has been received.
_received_health_reply = False


def _handle_health_event(event):
    '''Handle health event.'''
    logging.info('Received health event, responding.')
    return True


def _handle_health_reply(event):
    '''Handle health reply.'''
    global _received_health_reply
    _received_health_reply = True
    logging.info('Received health response.')


def register(session):
    '''Register listener for healhcheck.'''
    session.event_hub.subscribe(
        'topic={}'.format(HEALTH_TOPIC),
        _handle_health_event
    )


def publish(session):
    '''Publish a healthckeck event and wait for response.'''
    while not session.event_hub.connected:
        time.sleep(0.1)

    event = ftrack_api.event.base.Event(topic=HEALTH_TOPIC)
    session.event_hub.publish(
        event,
        on_reply=_handle_health_reply
    )

    while _received_health_reply is False:
        session.event_hub.wait(0.01)
