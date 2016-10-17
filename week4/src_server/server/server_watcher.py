import threading
import socket
import errno, ast
import socket
from time import sleep
from watcher_jsontosql import Watcher
import sqlite3 as sql
from condb import Connection


def main():
	server = Server()
	server.go()
	try:
		join_threads(server.threads)
	except KeyboardInterrupt:
		print ("\nKeyboardInterrupt catched.")


class SockServer:
	@staticmethod
	def sock(s):
		# s = socket.socket()
		# # host = socket.gethostname()
		# host = ''
		# port = 44444
		# s.bind((host, port))
		# s.listen(2)
		# print 'Waiting for connection...'

		''' multi connect client??'''
		while True:
			try:
				conn, addr = s.accept()
				print 'got connection from ', addr
			except socket.error:
				break

			while True:
				try:
					received = conn.recv(1024)

				except socket.error or ast.ExceptHandler:
					break
				else:
					try:
						received_dict = ast.literal_eval(received)
					except:
						pass
					print 'Received: ', received
					con_db = sql.connect("E:\\1link\week4\src_server\Students.db")
					with con_db:
						send_client = []
						con_db.row_factory = sql.Row  # return result as diction
						rows = Connection.query(con_db, received_dict)
						if rows is None:
							send_client.append("No Result!!")
						for row in rows:
							student_tmp = str(row['id']) + '  ' + str(row['name']) + '  ' + str(
								row['gender']) + '  ' + str(
								row['address']) + '  ' + str(row['math']) + '  ' + str(row['physic']) + '  ' + str(
								row['chemistry'])
							send_client.append(student_tmp)

					conn.sendall(str(send_client))
				# conn.close()


class Server(object):
	def __init__(self):
		self.running = True
		self.threads = []
		self.watch = Watcher()
		self.sock = SockServer()

	def watcher(self):
		while self.running:
			self.watch.run()

	def socket_server(self):
		s = socket.socket()
		host = ''
		port = 44444
		s.bind((host, port))
		s.listen(2)
		print 'Waiting for connection...'

		while True:
			self.sock.sock(s)
		s.close()

	def go(self):
		t1 = threading.Thread(target=self.watcher)
		t2 = threading.Thread(target=self.socket_server)

		t1.daemon = True
		t2.daemon = True
		t1.start()
		t2.start()
		self.threads.append(t1)
		self.threads.append(t2)


def join_threads(threads):
	for t in threads:
		while t.isAlive():
			t.join(5)


if __name__ == "__main__":
	main()
