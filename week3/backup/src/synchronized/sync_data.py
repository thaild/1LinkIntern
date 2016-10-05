from __future__ import generators
import os
import sys
import Queue
import threading
import time
import json
from lib import win32con
from lib import win32file

ACTIONS = {
	1: "Created",
	2: "Deleted",
	3: "Updated",
	4: "Renamed to something",
	5: "Renamed from something"
}


def watch_path(path_to_watch, include_subdirectories=False):
	FILE_LIST_DIRECTORY = 0x0001
	hDir = win32file.CreateFile(
		path_to_watch,
		FILE_LIST_DIRECTORY,
		win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
		None,
		win32con.OPEN_EXISTING,
		win32con.FILE_FLAG_BACKUP_SEMANTICS,
		None
	)
	while 1:
		results = win32file.ReadDirectoryChangesW(
			hDir,
			1024,
			include_subdirectories,
			win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
			win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
			win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
			win32con.FILE_NOTIFY_CHANGE_SIZE |
			win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
			win32con.FILE_NOTIFY_CHANGE_SECURITY,
			None,
			None
		)
		for action, file in results:
			full_filename = os.path.join(path_to_watch, file)
			if not os.path.exists(full_filename):
				file_type = "deleted"
			elif os.path.isdir(full_filename):
				file_type = 'folder'
			else:
				file_type = 'file'
			yield (file_type, full_filename, ACTIONS.get(action, "Unknown"))


class Watcher(threading.Thread):
	def __init__(self, path_to_watch, results_queue, **kwds):
		threading.Thread.__init__(self, **kwds)
		self.setDaemon(1)
		self.path_to_watch = path_to_watch
		self.results_queue = results_queue
		self.start()

	def run(self):
		for result in watch_path(self.path_to_watch):
			self.results_queue.put(result)


def load_data_from_file(path_file):
	data_import = []
	data_tmp = []
	file_input = open(path_file).read()
	for k in range(json.loads(file_input).__len__()):
		data_import.append(json.loads(file_input)[k])
	for i in range(data_import.__len__()):
		data_tmp.append(json.dumps(data_import[i]))
	save_data_file(data_tmp)


def save_data_file(data_tmp):
	data_file = []
	fi = open("../input2.json").read()
	try:
		fi_data = json.loads(fi)
		for i in range(fi_data.__len__()):
			data_file.append(json.dumps(fi_data[i]))
	except Exception:
		print (Exception.message)
	for i in range(data_tmp.__len__()):
		data_file.append(data_tmp[i]) # append data in file input to arr

	data_file = list(set(data_file)) # del phan tu trung lap
	fo = open("../input2.json", "w")
	fo.write('[\n')
	for i in range(data_file.__len__()):
		fo.write(data_file[i])
		if i < data_file.__len__() - 1:
			fo.write(',\n')
	fo.write(']')
	fo.close()


if __name__ == '__main__':
	PATH_TO_WATCH = ["../data/DIEM_THI_2016/"]
	try:
		path_to_watch = sys.argv[1].split(",") or PATH_TO_WATCH
	except:
		path_to_watch = PATH_TO_WATCH
	path_to_watch = [os.path.abspath(p) for p in path_to_watch]  # return path real

	print ("Watching %s at %s" % (", ".join(path_to_watch), time.asctime()))
	files_changed = Queue.Queue()

	for p in path_to_watch:
		Watcher(p, files_changed)
	list_file_dir = []
	while 1:
		try:
			file_type, filename, action = files_changed.get_nowait()
			print file_type, filename, action
			if filename not in list_file_dir:
				list_file_dir.append(filename)
				# set(list_file_dir)
				if action == 'Created':
					load_data_from_file(filename)
		except Queue.Empty:
			pass
		time.sleep(1)
