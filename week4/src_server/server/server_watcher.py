from threading import Thread
import threading
import socket
import errno, ast
import socket
from time import sleep
from watcher_jsontosql import Watcher
import sqlite3 as sql
from condb import Connection

TCP_IP = '0.0.0.0'
TCP_PORT = 2016


def main():
	server = Server()
	server.go()
	try:
		join_threads(server.threads)
	except KeyboardInterrupt:
		print ("\nKeyboardInterrupt catched.")


class ClientThread(Thread):
	def __init__(self, con, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.conn = con
		print "[+] New server started for " + ip + ":" + str(port)

	def run(self):
		while True:
			received = self.conn.recv(1024)
			received_dict = ast.literal_eval(received)

			print "Server received:", received
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

			self.conn.sendall(str(send_client))


class Server(object):
	def __init__(self):
		self.running = True
		self.threads = []
		self.watch = Watcher()

	def watcher(self):
		while self.running:
			self.watch.run()

	def socket_server(self):
		tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcpServer.bind((TCP_IP, TCP_PORT))
		threads = []
		while True:
			tcpServer.listen(3)
			print ("Waiting for connections...")
			(conn, (ip, port)) = tcpServer.accept()
			newthread = ClientThread(conn,ip, port)
			newthread.start()
			threads.append(newthread)

		for t in threads:
			t.join()

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


