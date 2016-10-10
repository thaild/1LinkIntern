import threading
import time
import json
import os

class tests_condition(threading.Thread):
	"""
	Producers random integers to a list
	"""

	def __init__(self, file_list, condition):
		threading.Thread.__init__(self)
		self.file_list = file_list
		self.condition = condition

	def run(self):
		"""
        Append random integers to integers list at random time.
        """
		data_import = []
		fo = open("../data_condition.json", "a")
		while True:
			self.file_list = os.listdir("../data/DIEM_THI_2016/")
			for i in range(self.file_list.__len__()):
				file_input = open("../data/DIEM_THI_2016/" + self.file_list[i]).read()
				self.condition.acquire()
				data_import.append(json.loads(file_input))

				fo.write(json.dumps(data_import))
				self.condition.notify()
				self.condition.release()
			time.sleep(1)


class del_file_input(threading.Thread):
	"""
	consumes random integers for a list
	"""

	def __init__(self, file_list, condition):
		threading.Thread.__init__(self)
		self.file_list = file_list
		self.condition = condition


	def run(self):
		"""
		Consumes integers from shared list
		"""
		while True:
			self.condition.acquire()
			print('condition acquired by {}'.format(self.name))
			while True:
				if self.file_list:
					self.file_list.pop()
				break
			self.condition.wait()
		self.condition.release()


def main():
	file_list = []
	condition = threading.Condition()
	test_con = tests_condition(file_list, condition)
	del_file = del_file_input(file_list, condition)
	test_con.start()
	del_file.start()

	test_con.join()
	del_file.join()


if __name__ == '__main__':
	main()
