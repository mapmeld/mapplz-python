# setup.py
# for installing MapPLZ-Python
# FreeBSD license - by Nick Doiron (@mapmeld)

import os
from distutils.core import setup
from setuptools import find_packages

VERSION = '0.1.1'
CLASSIFIERS = [
]

install_requires = [
    'psycopg2 >= 2.5.2',
    'pymongo >= 2.6.3',
    'geojson >= 1.0.9'
]

packages = []
data_files = []

setup(
    name='mapplz',
    description='easy data mapping',
    version=VERSION,
    author='Nick Doiron',
    author_email='nick@mapmeld.com',
    url='http://www.mapplz.com',
    download_url='https://github.com/mapmeld/mapplz-python/archive/master.zip',
    classifiers=CLASSIFIERS
)
