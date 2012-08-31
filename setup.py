#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='errorcats',
    version='1.0',
    description='An amusing replacement error handler',
    author='Nathaniel Case',
    author_email='Qalthos@gmail.com',
    url='https://github.com/Qalthos/errorcats',
    packages=find_packages(),
    package_data={'': ['*.mak']},
)
