from __future__ import generators
import os
import Queue
import threading
import time
import json

import win32file
import win32con

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
				file_type = "Deleted"
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

data_import = []

class load_data(threading.Thread):
	def __init__(self, pathfile, **kwds):
		threading.Thread.__init__(self, **kwds)
		self.pathfile = pathfile
		self.start()

	def run(self):
		data_import = []
		file_input = open(self.pathfile).read()
		for k in range(json.loads(file_input).__len__()):
			data_import.append(json.loads(file_input)[k])
		# print data_import.__len__()
		# for data in data_import:
		# 	print (json.dumps(data))


if __name__ == '__main__':
	path_to_watch = [os.path.abspath("../data/DIEM_THI_2016/")] #return path real
	print "Watching %s at %s" % (", ".join(path_to_watch), time.asctime())
	files_changed = Queue.Queue()
	Watcher(path_to_watch[0], files_changed)

	while 1:
		try:
			file_type, filename, action = files_changed.get_nowait()
			print file_type, filename, action
			if action == 'Created':
				load_data(filename)
		except Queue.Empty:
			time.sleep(2)
			print data_import.__len__()

