# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import ftrack_api

from ftrack_action_handler.action import BaseAction as _BaseAction


class ExampleAction(_BaseAction):
    '''Report action class.'''

    variant = 'ftrack action example'
    identifier = 'com.ftrack.example.action'
    label = 'Example action'

    def discover(self, session, entities, event):
        '''Discover any available actions.'''
        return True

    def launch(self, session, entities, event):
        '''Launch the action.'''
        return True
