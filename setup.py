#!/usr/bin/env python

from setuptools import setup, find_packages

import os

requires = [
    'boto3==1.1.2'
]


setup(
    name='petard',
    version=open(os.path.join('petard', '_version')).read().strip(),
    description='Blasting down the door to the Amazon API Gateway',
    long_description=open('README.md').read(),
    author='Mitch Garnaat',
    author_email='mitch@garnaat.com',
    url='https://github.com/garnaat/petard',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
