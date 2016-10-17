import socket
# host = socket.gethostname()
host = "localhost"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall('client send: data')
data = s.recv(1024)
s.close()
print 'Received ',repr(data)