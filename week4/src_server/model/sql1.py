import sqlite3 as sql
import sys
import os

conn = None

path = os.path.dirname(__file__) + "/test.db"
conn = sql.connect("E:\\1link\week4\src_server\Students.db")
with conn:
	cur = conn.cursor()
	# cur.execute('SELECT SQLITE_VERSION()')
	# cur.execute("DROP TABLE IF EXISTS Student")
	cur.execute("CREATE TABLE IF NOT EXISTS Std_tmp(id INT, name TEXT, gender TEXT, address TEXT, math FLOAT, physic FLOAT, chemistry FLOAT)")


	# data = cur.fetchone()
	# print "sqlite version %s" % data
