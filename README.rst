.. image:: https://badge.fury.io/py/sc-mysqlhelper.svg
    :target: https://badge.fury.io/py/sc-mysqlhelper
.. image:: https://img.shields.io/pypi/pyversions/sc-mysqlhelper
    :alt: PyPI - Python Version

MySQL helper for Python
========================================

A helper for working with mysql written in python, with
connection-pooling feature


Installation
------------

It is possible to install the tool with `pip`::

    pip install sc-mysqlhelper

Features
--------

* Connection pooling


Configuration
-------------

The script itself is currently configuration free.


Dependencies
------------

* PyMySQL 1.0.2
* DBUtils 2.0


Usage
-------
Sample usage::

    from mysqlhelper import MySQLHelper

    helper = MySQLHelper(host="localhost", port=3306, user="test", password="test", database="test")
    rs = helper.select_one(sql="select count(*) from users")
    print(rs[0])

License
-------

The script is released under the MIT License.  The MIT License is registered
with and approved by the Open Source Initiative [1]_.

.. [1] https://opensource.org/licenses/MIT
