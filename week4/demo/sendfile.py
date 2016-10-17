import socket


class Server:
	gate = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 0
	file = ''

	def __init__(self, port):
		self.port = port
		self.gate.bind((self.host, self.port))
		self.listen()

	def listen(self):
		self.gate.listen(10)
		while True:
			conn, addr = self.gate.accept()
			self.reciveFileName(conn)
			self.reciveFile()

	def reciveFileName(self, sock):
		buf = sock.recv(1024)
		print ('First bytes I got: ', +buf)
		while True:
			data = self.gate.recv(1024)
			self.file = data

	def reciveFile(self):
		createFile = open("new_" + self.file, "wb")
		while True:
			data = self.gate.recv(1024)
			createFile.write(data)
		createFile.close()


class Client:
	gateway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# host = socket.gethostname()
	host = ''
	port = 0
	file = ''

	def __init__(self, host, port, file):
		self.port = port
		self.host = host
		self.file = file
		self.connect()

	def connect(self):
		self.gateway.connect((self.host, self.port))
		self.sendFileName()
		self.sendFile()

	def sendFileName(self):
		self.gateway.send("name:" + self.file)

	def sendFile(self):
		readByte = open(self.file, "rb")
		data = readByte.read()
		readByte.close()

		self.gateway.send(data)
		self.gateway.close()

if __name__ == '__main__':
	a = Server(1111)
	b = Client('169.254.218.239', 1111, 'data.txt')
