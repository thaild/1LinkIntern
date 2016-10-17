# Python TCP Client B
import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 20
MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))
while MESSAGE != 'exit':
	tcpClientB.send(MESSAGE)
	data = tcpClientB.recv(1024)
	print " Client received data:", data
	MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close()
