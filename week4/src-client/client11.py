import socket, errno, sys
from time import sleep

host = socket.gethostname()
port = 44444


class Client:
	@staticmethod
	def view_menu():
		menu = "..::VIEW STUDENT::..\n1. Search\n2. Sort \n0. Exit"
		while True:
			choose_view = input(menu + "\nMain - Choose 0 -> 2: ")
			if choose_view == 0:
				print ('Exiting...')
				sys.exit(1)
			elif choose_view == 1:
				option = Client.search_option()
				view_send = {"choose": choose_view, "type": option['type'], "find": option['find']}
				s.sendall(str(view_send))
				sleep(1)
				Client.received()
				# break
			elif choose_view == 2:
				option = Client.sort_option()
				view_send = {"choose": choose_view, "type": option['type']}
				s.sendall(str(view_send))
				sleep(1)
				Client.received()
				# break
			else:
				print("Choose not exists")

	@staticmethod
	def search_option():
		find = {}
		menu = "Search Option:\n1. total scores \n2. ID: \n3. Name\n4. Score\n0. Return"
		while True:
			type = int(raw_input(menu + "\nChoose 0 -> 4: "))
			if type == 0:
				print ('Return...')
				find = {"type": type, "find": "ss"}
				break
			elif type == 1 or type == 2 or type == 3 or type == 4:
				find_str = raw_input('Enter search: ')
				find = {"type": type, "find": find_str}
				break
			else:
				find = {"type": "", "find": ""}
				print("Not EXISTS")
		return find

	@staticmethod
	def sort_option():
		sort = {}
		menu = "Sort Option:\n1.Total Scores \n2. ID: \n3. Name\n0. Return"
		while True:
			type = int(raw_input(menu + "\nChoose 0 -> 4: "))
			if type == 0:
				print ('Return...')
				sort = {"type": type}
				break
			elif type == 1 or type == 2 or type == 3:
				sort = {"type": type}
				break
			else:
				sort = {"type": ""}
				print("Not EXISTS")
		return sort

	@staticmethod
	def received():
		while True:
			try:
				recv_server = s.recv(4096)
			except socket.error as e:
				err = e.args[0]
				if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
					sleep(1)
					print 'No data available'
					continue
				else:
					print e
					break
			else:
				print str(recv_server)
			break


if __name__ == '__main__':
	s = socket.socket()
	s.connect((host, port))
	client = Client()
	client.view_menu()

