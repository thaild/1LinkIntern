import socket
from time import sleep
s = socket.socket()
# host = socket.gethostname()
host = "localhost"
port = 9999
s.connect((host, port))
sleep(20)
s.sendall(b"hello!! how are you??")
print s.recv(1024)