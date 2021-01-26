#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sc-mysqlhelper - Setup

Copyright (c) 2021 Scott Lau
"""

from setuptools import setup, find_packages

from mysqlhelper import VERSION

with open('README.rst') as fd:
    readme = fd.read()

setup(
    name='sc-mysqlhelper',
    version='.'.join(str(v) for v in VERSION),
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
        'PyMySQL==1.0.2',
        'DBUtils==2.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
