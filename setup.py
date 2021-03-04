#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sc-mysqlhelper - Setup

Copyright (c) 2021 Scott Lau
"""

import os

from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


with open('README.rst') as fd:
    readme = fd.read()

setup(
    name='sc-mysqlhelper',
    version=get_version("mysqlhelper/__init__.py"),
    url='https://github.com/Scott-Lau/sc-mysqlhelper',
    packages=find_packages(),
    author='Scott Lau',
    author_email='exceedego@126.com',
    license='MIT',
    platforms='POSIX',
    description='A helper for MySQL using python language',
    long_description=readme,
    keywords='mysql helper connection pool python',
    install_requires=[
        'PyMySQL>=1.0.2',
        'DBUtils>=2.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        'mysqlhelper': [],
    },
    include_package_data=True,
)
