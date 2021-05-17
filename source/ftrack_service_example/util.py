# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import threading


def run_async(fn):
    '''Run *fn* asynchronously.'''
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
    return wrapper
