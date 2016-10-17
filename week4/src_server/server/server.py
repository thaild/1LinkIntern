import socket
import errno, ast
import socket
from time import sleep
from watcher_jsontosql import Watcher
import sqlite3 as sql
from condb import Connection
import sys

# update database
# w = Watcher()
# w.run()

s = socket.socket()
# host = socket.gethostname()
host = ''
port = 44444
s.bind((host, port))
s.listen(2)
print 'Waiting for connection...'

''' multi connect client??'''
while True:
	try:
		conn, addr = s.accept()
		print 'got connection from ', addr
	except socket.error:
		break

	while True:
		try:
			received = conn.recv(50)

		except socket.error:
			break

		# except socket.error as e:
		# 	err = e.args[0]
		# 	if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
		# 		sleep(1)
		# 		print 'No data available'
		# 		continue
		# 	if e.errno != errno.ECONNRESET:
		# 		raise
		# 		pass
		# 	else:
		# 		# a "real" error occurred
		# 		# print('Connection aborted.', socket.error(10054, ''))
		# 		print e
		# 		continue
		# except SyntaxError or ValueError:
		# 	continue

		else:
			if received != None:
				received_dict = ast.literal_eval(received)
				# print 0
			print 'Received = ', received
			con_db = sql.connect("E:\\1link\week4\src_server\Students.db")

			with con_db:
				'''with will auto execute query insert, update, edit, delete (if not use commit() )
				python will auto exe exception and disconnect database if not use
				'''
				send_client = []
				con_db.row_factory = sql.Row  # return result as diction
				cur = con_db.cursor()

				rows = Connection.query(con_db, received_dict)

				if rows is None:
					send_client.append("No Result!!")
				for row in rows:
					student_tmp = str(row['id']) + '  ' + str(row['name']) + '  ' + str(row['gender']) + '  ' + str(row['address']) + '  ' + str(row['math']) + '  ' + str(row['physic']) + '  ' + str(row['chemistry'])
					send_client.append(student_tmp)

			conn.sendall(str(send_client))
		# conn.close()

			# conn.send(b'thanks for connecting...')

s.close()
