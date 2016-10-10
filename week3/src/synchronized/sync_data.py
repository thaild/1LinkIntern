from __future__ import generators
import os
import Queue
import threading
import time
import json
import win32con
import win32file

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
		) # return a list result(action, filename)
		for action, file in results:
			full_filename = os.path.join(path_to_watch, file) # realpath of filename
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


class FileLoader(threading.Thread):
	@staticmethod
	def load(pathfile):
		fi = open(pathfile)
		new_array = []
		try:
			new_array = json.loads(fi.read())
		except Exception:
			print (Exception.message)
		DataFile.save(new_array)
		fi.close()


class DataFile():
	@staticmethod
	def save(new_array):
		old_array = []
		fi = open("../input3.json")
		try:
			old_array = json.loads(fi.read())
		except Exception:
			print (Exception.message)
		fi.close()

		for i in range(new_array.__len__()):
			old_array.append(new_array[i])  # append data in file input to arr

		# old_array = list(set(old_array))  # del phan tu trung lap
		fo = open("../input3.json", "w")
		print old_array.__len__()
		fo.write(json.dumps(old_array))
		fo.close()


if __name__ == '__main__':
	path_to_watch = [os.path.abspath("../data/DIEM_THI_2016/")]  # return path real
	print "Watching %s at %s" % (", ".join(path_to_watch), time.asctime())
	files_changed = Queue.Queue()
	Watcher(path_to_watch[0], files_changed)

	list_file_dir = []
	while 1:
		try:
			file_type, filename, action = files_changed.get_nowait()
			print file_type, filename, action
			# if filename not in list_file_dir:
			# 	list_file_dir.append(filename)
			if action == 'Created':
				FileLoader.load(filename)
		except Queue.Empty:
			time.sleep(1)



