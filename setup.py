#!/usr/bin/env python

from setuptools import *

setup(
    name='nose-subheadings-plugin',
    version='0.1',
    description='Subheadings for nose --verbosity=2 output',
    long_description=('This is a nose plugin for adding package/module/class '
                      'subheadings to --verbosity=2 console test results.'),
    author='Antti Kaihola',
    author_email='akaihol+nose@ambitone.com',
    url='https://github.com/akaihola/nose-subheadings-plugin',
    license='BSD',
    packages = find_packages(exclude=['test', 'test.*']),
    install_requires=['setuptools'],
    entry_points='''
        [nose.plugins.0.10]
        subheadings = subheadings:SubheadingsPlugin
        ''',
    py_modules=['subheadings'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
    ],
    keywords='test nosetests nose nosetest output console subheading',
)
