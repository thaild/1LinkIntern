import ast
import socket
import sqlite3 as sql
from condb import Connection
from threading import Thread
from SocketServer import ThreadingMixIn


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print "[+] New server started for " + ip + ":" + str(port)

	def run(self):
		while True:
			received = conn.recv(1024)
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

			conn.sendall(str(send_client))


TCP_IP = '0.0.0.0'
TCP_PORT = 2016

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []
while True:
	tcpServer.listen(3)
	print "Waiting for connections from TCP clients..."
	(conn, (ip, port)) = tcpServer.accept()
	newthread = ClientThread(ip, port)
	newthread.start()
	threads.append(newthread)

for t in threads:
	t.join()
