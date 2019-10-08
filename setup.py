# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import os
import re

from setuptools import setup, find_packages


ROOT_PATH = os.path.dirname(
    os.path.realpath(__file__)
)

SOURCE_PATH = os.path.join(
    ROOT_PATH, 'source'
)

README_PATH = os.path.join(ROOT_PATH, 'README.rst')


with open(os.path.join(
    SOURCE_PATH, 'ftrack_service_example', '_version.py')
) as _version_file:
    VERSION = re.match(
        r'.*__version__ = \'(.*?)\'', _version_file.read(), re.DOTALL
    ).group(1)


# Configuration.
setup(
    name='ftrack-service-example',
    version=VERSION,
    description='ftrack service example',
    long_description=open(README_PATH).read(),
    keywords='',
    url='https://bitbucket.org/ftrack/ftrack-service-example',
    author='ftrack',
    author_email='support@ftrack.com',
    license='Apache License (2.0)',
    packages=find_packages(SOURCE_PATH),
    package_dir={
        '': 'source'
    },
    install_requires=[
        'ftrack-python-api',
        'ftrack-action-handler'
    ]
)
