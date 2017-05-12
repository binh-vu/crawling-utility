#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='crawling_utility',
    version='0.0.1',
    description='Utilities for crawling websites',
    author='Binh Vu',
    author_email='binhlvu@gmail.com',
    url='https://github.com/binh-vu/crawling-utility',
    packages=find_packages(exclude=['tests.*', 'tests'])
)
