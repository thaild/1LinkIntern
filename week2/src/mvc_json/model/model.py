
import json


class Model(object):
	def __init__(self, _id=None, name=None, add=None, sex=None, math=0, physics=0, chem=0):
		self._name = name
		self._id = _id
		self._add = add
		self._sex = sex
		self._math = float(math)
		self._physics = float(physics)
		self._chemistry = float(chem)
		self._list = []
		self._tmp = []

	#
	# def sum_score(self):
	# 	return self._math + self._physics + self._chemistry

	def __str__(self):
		return '{self._id} {self._name} {self._add} {self._sex} {self._math} {self._physics} {self._chemistry}'.format(
			self=self)

	def read(self, file_name):
		json_data = open(file_name).read()
		students = json.loads(json_data)
		return students

	def write_option(self, file_name, _modes, write_str):
		fo = open(file_name, _modes)
		fo.write('[\n')
		for i in range(write_str.__len__() - 1):
			fo.write(write_str[i] + ',\n')
		fo.write(write_str[write_str.__len__() - 1])
		fo.write(']')
		fo.close()

	def write(self, file_name, _modes, _tmp):
		students = _tmp
		fo = open(file_name, _modes)
		fo.write('[\n')
		for i in range(students.__len__() - 1):
			fo.write(str(json.dumps(students[i])) + ',\n')
		fo.write(str(json.dumps(students[students.__len__() - 1])))
		fo.write(']')
		fo.close()

	def write_add(self, file_name, _modes, _tmp):
		fi = open(file_name).read()
		students = json.loads(fi)
		fo = open(file_name, _modes)
		fo.write('[\n')
		for i in range(students.__len__()):
			fo.write(str(json.dumps(students[i])) + ',\n')

		student = {}
		scores = {}
		for i in range(_tmp.__len__()):
			_id, name, add, sex, math, physics, chemistry = _tmp[i].split()
			student["id"] = _id
			student["name"] = name
			student["add"] = add
			student["gender"] = sex
			student["scores"] = scores
			scores["math"] = math
			scores["physics"] = physics
			scores["chemistry"] = chemistry
			fo.write(str(json.dumps(student, ensure_ascii=False)))
			if i < _tmp.__len__() - 1:
				fo.write(',\n')
		fo.write(']')
		fo.close()

	# def write_add(self, file_name, _modes, _tmp):
	# 	student = {}
	# 	scores = {}
	# 	for i in range(_tmp.__len__()):
	# 		_id, name, add, sex, math, physics, chemistry = _tmp[i].split()
	# 		student["id"] = _id
	# 		student["name"] = name
	# 		student["add"] = add
	# 		student["gender"] = sex
	# 		student["scores"] = scores
	# 		scores["math"] = math
	# 		scores["physics"] = physics
	# 		scores["chemistry"] = chemistry
	#
	# 	fi = open(file_name).read()
	# 	students = json.loads(fi)
	#
	# 	fo = open(file_name, _modes)
	# 	fo.write('[\n')
	# 	for i in range(students.__len__()):
	# 		fo.write(str(json.dumps(students[i])) + ',\n')
	# 	fo.write(str(json.dumps(student, ensure_ascii=False)))
	# 	fo.write(']')
	# 	fo.close()

	def md_delete(self, _list, id_del):
		for j in range(0, _list.__len__() - 1):
			if id_del == int(_list[j]["id"]):
				del _list[j]
		Model().write('input.json', 'w', _list)

	def sorted(self, _list):
		for j in range(0, _list.__len__() - 1):
			if int(_list[j]['id']) > int(_list[j + 1]['id']):
				_list[j], _list[j + 1] = _list[j + 1], _list[j]
		return _list

	def _search(self, k, _list, _find):
		self._list = _list
		write_str = []
		_total = 0
		if int(k) == 1:
			for i in range(self._list.__len__()):
				if float(self._list[i]['scores']['math']) + \
					float(self._list[i]['scores']['physics']) + \
					float(self._list[i]['scores']['chemistry']) == float(_find):
					_total += 1
					write_str.append(json.dumps(self._list[i]))
		elif int(k) == 2:
			for i in range(self._list.__len__()):
				if str(_find) in str(self._list[i]['id']):
					_total += 1
					write_str.append(json.dumps(self._list[i]))
		elif int(k) == 3:
			for i in range(self._list.__len__()):
				if _find.lower() in str(self._list[i]['name']).lower():
					_total += 1
					write_str.append(json.dumps(self._list[i]))
		elif int(k) == 4:
			for i in range(self._list.__len__()):
				if float(_find) == float(self._list[i]['scores']['math']) or \
					float(_find) == float(self._list[i]['scores']['physics']) or \
					float(_find) == float(self._list[i]['scores']['chemistry']):
					_total += 1
					write_str.append(json.dumps(self._list[i]))

		if write_str.__len__() != 0:
			self.write_option("search.json", 'w', write_str)
		else:
			write_str = 'No result'
		return write_str

	def statistic(self, _list, _score_min, _score_max):
		self._list = _list
		_total = 0
		write_str = []
		_sco_min = int(_score_min)
		_sco_max = int(_score_max)
		for i in range(self._list.__len__()):
			if _sco_min <= float(self._list[i]['scores']['math']) + float(self._list[i]['scores']['physics']) + float(self._list[i]['scores']['chemistry']) < _sco_max:
				_total = _total + 1
				write_str.append(json.dumps(self._list[i]))
		if write_str.__len__() != 0:
			self.write_option("statistic.json", 'w', write_str)
		else:
			write_str = 'No result'
		return write_str


	def md_edit(self, k, _list, str_new, i):
		self._list = _list
		if int(k) == 1:
			self._list[i]["name"] = str_new
		elif int(k) == 2:
			self._list[i]["add"] = str_new
		elif int(k) == 3:
			self._list[i]["gender"] = str_new

		return self._list
