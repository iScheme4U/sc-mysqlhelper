"""The main module

Copyright (c) 2021 Scott Lau
"""

from mysqlhelper.mysql_connection_pool import MySQLHelper

VERSION = (0, 1, 2)

__all__ = [
    "MySQLHelper",
    "VERSION",
]
