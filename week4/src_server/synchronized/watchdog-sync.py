import time, json, threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
	DIRECTORY_TO_WATCH = "../data/DIEM_THI_2016/"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
		self.observer.start()
		try:
			while True:
				time.sleep(1)
		except:
			self.observer.stop()
			print "Error"
		self.observer.join()


class Handler(FileSystemEventHandler):
	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
			# Take any action here when a file is first created.
			print "Received created event - %s." % event.src_path
			FileLoader.load(event.src_path)
		elif event.event_type == 'modified':
			# Taken any action here when a file is modified.
			print "Received modified event - %s." % event.src_path
			FileLoader.load(event.src_path)


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


class Singleton(object):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(
				cls, *args, **kwargs)
		return cls._instance


def update(new_array, old_array):
	for i in range(old_array.__len__()):
		for j in range(new_array.__len__()):
			if old_array[i]['id'] == new_array[j]['id']:
				old_array[i] = new_array[j] # update student[i] in old_array
	return old_array


class DataFile(Singleton):
	@staticmethod
	def save(new_array):
		old_array = []
		fi = open("../input2.json")
		try:
			old_array = json.loads(fi.read())
		except Exception:
			print (Exception.message)
		fi.close()
		old_array = update(new_array, old_array)
		for i in range(new_array.__len__()):
			old_array.append(new_array[i])  # append data in file input to arr

		fo = open("../input2.json", "w")
		# old_array = list(set(old_array))  # del phan tu trung lap
		tmp_array = []
		[tmp_array.append(json.dumps(k)) for k in old_array]
		tmp_array = list(set(tmp_array))  # del phan tu trung lap
		fo.write('[\n')
		for i in range(tmp_array.__len__()):
			fo.write(tmp_array[i])
			if i < tmp_array.__len__() - 1:
				fo.write(',\n')
		fo.write(']')
		print tmp_array.__len__()
		# fo.write(json.dumps(old_array))
		fo.close()


if __name__ == '__main__':
	w = Watcher()
	w.run()
