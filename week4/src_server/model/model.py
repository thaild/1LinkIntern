import json


class Student(object):
	def __init__(self, _id=None, name=None, add=None, sex=None, math=0, physics=0, chem=0):
		self._name = name
		self._id = _id
		self._add = add
		self._sex = sex
		self._math = float(math)
		self._physics = float(physics)
		self._chemistry = float(chem)

	def __str__(self):
		return '{self._id} {self._name} {self._add} {self._sex} {self._math} {self._physics} self._chemistry}'.format(self=self)


class Model(Student):
	def __init__(self):
		super(Model, self).__init__()
		self._list = []
		self._tmp = []

	def read(self, file_name):
		json_data = open(file_name).read()
		list = json.loads(json_data)
		return list

	def write_statistic(self, file_name, modes, write_str, sc_min, sc_max):
		fo = open(file_name, modes)
		fo.write("\nResult Search {} <= scores < {}\n". format(sc_min,sc_max))
		for i in range(write_str.__len__()):
			fo.write(write_str[i] + '\n')
		fo.close()

	def write_search(self, file_name, modes, write_str):
		fo = open(file_name, modes)
		for i in range(write_str.__len__()):
			fo.write(write_str[i]+'\n')
		fo.close()

	def write(self, file_name, modes, tmp):
		students = tmp
		fo = open(file_name, modes)
		fo.write('[\n')
		for i in range(students.__len__() - 1):
			fo.write(str(json.dumps(students[i])) + ',\n')
		fo.write(str(json.dumps(students[students.__len__() - 1])))
		fo.write(']')
		fo.close()

	def write_add(self, file_name, modes, tmp_students):
		fi = open(file_name).read()
		students = json.loads(fi)
		fo = open(file_name, modes)
		fo.write('[\n')
		for i in range(students.__len__()):
			fo.write(str(json.dumps(students[i])) + ',\n')
			pass
		for i in range(tmp_students.__len__()):
			fo.write(str(tmp_students[i]))
			if i < tmp_students.__len__() - 1:
				fo.write(',\n')
		fo.write(']')
		fo.close()

	def md_delete(self, list, id_del):
		for j in range(0, list.__len__() - 1):
			if id_del == int(list[j]["id"]):
				del list[j]
		Model().write('input2.json', 'w', list)

	def sorted(self, list):
		self._list = sorted(list, key=lambda i: i['id'])
		return self._list

	def student_print(self, std):
		return str(std['id']) + ' ' + str(std['name']) + ' ' + str(std['add']) + ' ' + str(std['gender']) + ' ' + str(std['math']) + ' ' + str(std['chemistry']) + ' ' + str(std['physics'])

	def search(self, k, std_list, find):
		self._list = std_list
		write_str = []
		if int(k) == 1:
			write_str.append('\nResult Search Total Scores: {}'.format(find))
			for i in range(self._list.__len__()):
				if float(self._list[i]['math']) + \
					float(self._list[i]['physics']) + \
					float(self._list[i]['chemistry']) == float(find):
					stt_finded = self.student_print(self._list[i])
					write_str.append(stt_finded)
		elif int(k) == 2:
			write_str.append('\nResult Search ID: {}'.format(find))
			for i in range(self._list.__len__()):
				if str(find) in str(self._list[i]['id']):
					stt_finded = self.student_print(self._list[i])
					write_str.append(stt_finded)
		elif int(k) == 3:
			write_str.append('\nResult Search Name: {}'.format(find))
			for i in range(self._list.__len__()):
				if find.lower() in str(self._list[i]['name']).lower():
					stt_finded = self.student_print(self._list[i])
					write_str.append(stt_finded)
		elif int(k) == 4:
			write_str.append('\nResult Search Scores: {}'.format(find))
			for i in range(self._list.__len__()):
				if float(find) == float(self._list[i]['math']) or \
					float(find) == float(self._list[i]['physics']) or \
					float(find) == float(self._list[i]['chemistry']):
					stt_finded = self.student_print(self._list[i])
					write_str.append(stt_finded)
		if write_str.__len__() != 0:
			self.write_search("search.txt", 'a', write_str)
		else:
			write_str = 'No result'
		return write_str

	def statistic(self, std_list, score_min, score_max):
		self._list = std_list
		total = 0
		write_str = []
		for i in range(self._list.__len__()):
			if int(score_min) <= float(self._list[i]['math']) + float(self._list[i]['physics']) + float(self._list[i]['chemistry']) < int(score_max):
				total = total + 1
				std_finded = self.student_print(self._list[i])
				write_str.append(std_finded)
		if write_str.__len__() != 0:
			self.write_statistic("statistic.txt", 'a', write_str, score_min, score_max)
		else:
			write_str.append('No result')
		return write_str

	def md_edit(self, k, std_list, str_new, i):
		self._list = std_list
		if int(k) == 1:
			self._list[i]["name"] = str_new
		elif int(k) == 2:
			self._list[i]["add"] = str_new
		elif int(k) == 3:
			self._list[i]["gender"] = str_new
		return self._list
