# db_connect.py
import pymysql
import pymysql.cursors
from flask import g

def get_db():
    if 'db' not in g or not is_connection_open(g.db):
        print("Re-establishing closed database connection.")
        g.db = pymysql.connect(
            host='wiad5ra41q8129zn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user='ouuuoyzcwlxujl8d',
            password='hl70ws1p7u7gz2fx',
            database='xhq42dq72lx1kw98',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def is_connection_open(conn):
    try:
        conn.ping(reconnect=True)
        return True
    except:
        return False

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None and not db._closed:
        print("Closing database connection.")
        db.close()