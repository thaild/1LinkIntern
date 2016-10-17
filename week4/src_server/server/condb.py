import sqlite3 as sql
import sys, os


class Connection:
	@staticmethod
	def query(conn, received_dict):
		with conn:
			conn.row_factory = sql.Row  # return result as diction
			cur = conn.cursor()
			sql_search = "SELECT * FROM Student "

			# "WHERE name like '% " + {} + " %' ".format(received_dict['find']))

			if received_dict['choose'] == 1 and received_dict['type'] == 2:
				cur.execute(sql_search + "WHERE id = {}".format(received_dict['find']))
			elif received_dict['choose'] == 1 and received_dict['type'] == 3:
				cur.execute(sql_search + "WHERE name like  '%{}%' ".format(received_dict['find']))
				# print (sql_search + "WHERE name like  '%{}%' ".format(received_dict['find']))
			elif received_dict['choose'] == 1 and received_dict['type'] == 4:
				cur.execute(
					sql_search + "WHERE math = {} or physic = {} or chemistry = {} ".format(received_dict['find'],received_dict['find'],received_dict['find']))
			elif received_dict['choose'] == 1 and received_dict['type'] == 1:
				cur.execute(sql_search + "WHERE math + physic + chemistry = {}".format(received_dict['find']))

			elif received_dict['choose'] == 2 and received_dict['type'] == 1:
				cur.execute(sql_search + " order by math + physic +chemistry asc ")
			elif received_dict['choose'] == 2 and received_dict['type'] == 2:
				cur.execute(sql_search + " order by id asc ")
			elif received_dict['choose'] == 2 and received_dict['type'] == 3:
				cur.execute(sql_search + " order by name asc ")

			return cur.fetchall()
