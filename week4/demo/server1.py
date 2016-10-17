import socket
s = socket.socket()
# host = socket.gethostname()
host =''
port = 12321
s.bind((host, port))

s.listen(5)
while True:
	conn, addr = s.accept()
	print ('got connection from ', addr)
	print ('Received message == ', conn.recv(50))
	conn.send(b'thanks for connecting...')
	conn.close()

s.close()