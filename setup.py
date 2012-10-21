#!/usr/bin/env python

import os
import sys

import requests
from requests.compat import is_py2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = ['kippt_wrapper']

requires = []

description = ""
with open('README.md','r') as readme:
    description = readme.read()
license = ""
with open('LICENSE','r') as licenseFile:
    license = licenseFile.read()


setup(
    name='Kippt Wrapper',
    version="0.1",
    description='Kippt.com API wrapper for Python',
    long_description=description,
    author='Thomas Biddle',
    author_email='me@ThomasBiddle.com',
    url='https://github.com/thomasbiddle/Kippt-Python-Wrapper',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'kippt_wrapper': 'src'},
    include_package_data=True,
    install_requires=requires,
    license=license,
)

del os.environ['PYTHONDONTWRITEBYTECODE']