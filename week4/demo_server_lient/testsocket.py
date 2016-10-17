
import multiprocessing as mp
import socket
import time

def basic():
    sproc = mp.Process(target=server)
    sproc.daemon = True
    sproc.start()
    time.sleep(.5)
    client()
    sproc.join()


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 1234
    s.bind((host, port))
    s.listen(5)
    c, addr = s.accept()
    print('Got connection from {}'.format(addr))
    print('Received message == {}'.format(c.recv(50).decode('ascii')))
    c.send(b'Thank you for connecting')
    c.close()

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    time.sleep(1)
    s.sendall(b"Hello!! How are you")
    print(s.recv(1024).decode('ascii'))
    s.close()
if __name__ == '__main__':
	bs = basic()
