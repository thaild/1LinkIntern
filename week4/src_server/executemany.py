import sqlite3 as sql
import sys
import os

Students = (
	(1, 'thai le', 'nam', 'nghe an', 6, 8, 6),
	(2, 'thai dinh le', 'nam', 'nghe an', 6, 6, 9),
	(3, 'thai', 'nam', 'nghe an', 6, 8, 6),
	(4, 'thai dinh', 'nam', 'nghe an', 8, 8, 6),
	(5, 'thai le dinh', 'nam', 'nghe an', 6, 6, 6),
	(6, 'thai le', 'nam', 'nghe an', 6, 6, 9),
	(7, 'thai le', 'nam', 'nghe an', 5, 6, 10),
	(8, 'thai le', 'nam', 'nghe an', 3, 6, 8),
	(9, 'thai le', 'nam', 'nghe an', 8, 6, 9),
	(10, 'thai le', 'nam', 'nghe an', 1, 6, 6)
)
path = os.path.dirname(__file__) + "/Students.db"
conn = sql.connect(path)
with conn:
	conn.row_factory = sql.Row # return result as diction
	cur = conn.cursor()
	# cur.execute('SELECT SQLITE_VERSION()')
	cur.execute("DROP TABLE IF EXISTS Student")
	cur.execute("CREATE TABLE Student(id INT, name TEXT, gender TEXT, address TEXT, math FLOAT, physic FLOAT, chemistry FLOAT)")
	cur.executemany("INSERT INTO Student VALUES(?, ?, ?, ?,?,?,?)", Students)
	cur.execute("SELECT * FROM Student")

	while True:
		row = cur.fetchone()
		if row == None: break
		print (row)
