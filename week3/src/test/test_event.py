import threading
import time
import json
import os
import sys

from datetime import datetime

class Demo(threading.Thread):
	def __init__(self, file_list, event):
		threading.Thread.__init__(self)
		self.file_list = file_list
		self.event = event

	def run(self):
		"""
		Append data in file school.input to INPUT.json
		"""
		path = "../data/DIEM_THI_2016/"
		self.file_list = os.listdir(path)
		self.event.set() # flag = True
		print path
		self.event.clear() # flag False
		time.sleep(1)


class pop_file_input(threading.Thread):
	"""
	remove file readed
	"""

	def __init__(self, file_list, event):
		threading.Thread.__init__(self)
		self.file_list = file_list
		self.event = event

	def run(self):
		while True:
			self.event.wait() # flag= True -> continous
			try:
				self.file_list = self.file_list.pop()
				print self.file_list
				print ('addasd')
			except IndexError:
				time.sleep(1)


def main():
	file_list = []
	event = threading.Event()
	demo = Demo(file_list, event)
	pop_file = pop_file_input(file_list, event)

	demo.start()
	pop_file.start()
	demo.join()
	pop_file.join()


if __name__ == '__main__':
	main()
