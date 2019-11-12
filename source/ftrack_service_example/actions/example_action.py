# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import time
import json

import ftrack_api

from ftrack_action_handler.action import BaseAction as _BaseAction
from .. import util


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

        self.logger.info(
            u'Launching action with selection {0}'.format(entities)
        )

        self._run_async(entities, event)

        return {
            'success': True,
            'message': 'Successfully launched action.'
        }

    @util.async
    def _run_async(self, entities, event):
        '''Long running or blocking job.'''

        # Create a new session as sessions are not thread safe. We also want to
        # avoid poluting the main session with operations in case of a failure.
        session = ftrack_api.Session(auto_connect_event_hub=False)

        # Create a job so that the user can track progress.
        user_id = event['source']['user']['id']
        job = session.create(
            'Job',
            {
                'user': session.get('User', user_id),
                'status': 'running',
                'data': json.dumps(
                    {
                        'description': 'Long running example job.'
                    }
                )
            }
        )
        session.commit()

        self.logger.info('Starting async operation.')
        time.sleep(10)
        self.logger.info('Finished async operation.')

        job['status'] = 'done'
        session.commit()
