# -*- coding: utf-8 -*-
"""
A simple connection pool for mysql using dbutils.pooled_db
"""

import logging

import pymysql
from dbutils.pooled_db import PooledDB


class MySQLHelper:
    _pool = None

    def __init__(
            self,
            *,
            host,
            port,
            user,
            password,
            database,
            use_unicode=True,
            charset="utf8mb4",
            min_cached=10,
            max_cached=10,
            max_shared=20,
            max_connections=100,
            blocking=True,
            max_usage=0,
            set_session=""):
        if self._pool is None:
            self._pool = PooledDB(
                creator=pymysql,
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                use_unicode=use_unicode,
                charset=charset,
                mincached=min_cached,
                maxcached=max_cached,
                maxshared=max_shared,
                maxconnections=max_connections,
                blocking=blocking,
                maxusage=max_usage,
                setsession=set_session,
            )

    def get_conn(self):
        conn = self._pool.connection()
        cursor = conn.cursor()
        return cursor, conn

    def select_all_with_callback(self, *, sql='', param=(), callback=None):
        if callback is None:
            logging.warning("failed to select with callback, callback is None")
            return
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            res = cursor.fetchone()
            while res is not None:
                callback(res)
                res = cursor.fetchone()
            self.close(cursor, conn)
        except Exception as e:
            logging.exception("failed to select with call_back %s, params %s", sql, param, exc_info=e)
            self.close(cursor, conn)

    def select_all(self, *, sql='', param=()):
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            res = cursor.fetchall()
            self.close(cursor, conn)
            return res
        except Exception as e:
            logging.exception("failed to select many %s, params %s", sql, param, exc_info=e)
            self.close(cursor, conn)
            return None

    def select_one(self, *, sql='', param=()):
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            res = cursor.fetchone()
            self.close(cursor, conn)
            return res
        except Exception as e:
            logging.exception("failed to select one %s, params %s", sql, param, exc_info=e)
            self.close(cursor, conn)
            return None

    def insert(self, *, sql='', param=()):
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            _id = cursor.rowcount
            conn.commit()
            self.close(cursor, conn)
            return _id
        except Exception as e:
            logging.exception("failed to insert %s, params %s", sql, param, exc_info=e)
            conn.rollback()
            self.close(cursor, conn)
            return 0

    def insert_many(self, *, sql='', param=()):
        cursor, conn = self.get_conn()
        try:
            cursor.executemany(sql, param)
            conn.commit()
            self.close(cursor, conn)
            return True
        except Exception as e:
            logging.exception("failed to insert many %s, params %s", sql, param, exc_info=e)
            conn.rollback()
            self.close(cursor, conn)
            return False

    def delete(self, *, sql='', param=()):
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            self.close(cursor, conn)
            return True
        except Exception as e:
            logging.exception("failed to delete %s, params %s", sql, param, exc_info=e)
            conn.rollback()
            self.close(cursor, conn)
            return False

    def update(self, *, sql='', param=()):
        cursor, conn = None, None
        try:
            cursor, conn = self.execute(sql=sql, param=param)
            _id = cursor.rowcount
            self.close(cursor, conn)
            return _id
        except Exception as e:
            logging.exception("failed to update %s, params %s", sql, param, exc_info=e)
            conn.rollback()
            self.close(cursor, conn)
            return 0

    def execute(self, *, sql='', param=(), auto_close=False):
        cursor, conn = self.get_conn()
        try:
            if param:
                cursor.execute(sql, param)
            else:
                cursor.execute(sql)
            conn.commit()
            if auto_close:
                self.close(cursor, conn)
        except Exception as e:
            logging.exception("failed to execute %s, params %s", sql, param, exc_info=e)
            conn.rollback()
        return cursor, conn

    def execute_many(self, *, sql_list=None):
        if sql_list is None:
            sql_list = []
        cursor, conn = self.get_conn()
        try:
            for order in sql_list:
                sql = order['sql']
                param = order['param']
                if param:
                    cursor.execute(sql, param)
                else:
                    cursor.execute(sql)
            conn.commit()
            self.close(cursor, conn)
            return True
        except Exception as e:
            logging.exception("failed to execute %s", sql_list, exc_info=e)
            conn.rollback()
            self.close(cursor, conn)
            return False

    def close(self, cursor, conn):
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
