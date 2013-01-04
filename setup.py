#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='Actor-Registry',
    version='0.2.0',
    url='https://github.com/dmr/actor-registry',
    license='MIT',
    author='Daniel Rech',
    author_email='danielmrech@gmail.com',
    description=('This small web app starts a server that allows to register urls and returns registered urls'),
    long_description=open('README.rst').read(),

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'actor_registry = actor_registry:main'
        ],
    },

    zip_safe=False,
    platforms='any',

    install_requires=[
        'argparse',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ]
)
