
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

	# def get_id(self):
	# 	return self._id
	#
	# def get_name(self):
	# 	return self._name
	#
	# def get_add(self):
	# 	return self._add
	#
	# def get_sex(self):
	# 	return self._sex
	#
	# def get_math(self):
	# 	return self._math
	#
	# def get_phys(self):
	# 	return self._physics
	#
	# def get_chem(self):
	# 	return self._chemistry

	def sum_score(self):
		return self._math + self._physics + self._chemistry

	def __str__(self):
		return '{self._id} {self._name} {self._add} {self._sex} {self._math} {self._physics} {self._chemistry}'.format(
			self=self)

	def read(self, file_name):
		json_data = open(file_name).read()
		students = json.loads(json_data)
		return students

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
		student = _tmp
		fi = open(file_name)
		students = fi.read()

		fo = open(file_name, _modes)
		fo.write('[\n')
		for i in range(students.__len__()):
			fo.write(str(json.dumps(students[i])) + ',\n')
		fo.write(str(json.dumps(student)))
		fo.write(']')
		fo.close()


	# def md_delete(self, _list, id_del):
	# 	self._list = _list
	# 	for j in range(0, self._list.__len__() - 1):
	# 		if id_del == int(self._list[j].get_id()):
	# 			del self._list[j]
	# 		self._tmp.append(str(self._list[j]))
	# 	Model().write('input.txt', 'w', self._tmp)
	#
	# def sorted(self, _list):
	# 	self._list = _list
	# 	for j in range(0, self._list.__len__() - 1):
	# 		if int(self._list[j].get_id()) > int(self._list[j + 1].get_id()):
	# 			self._list[j], self._list[j + 1] = self._list[j + 1], self._list[j]
	# 	return self._list
	#
	# def search_total_score(self, _list, _score):
	# 	self._list = _list
	# 	write_str = []
	# 	_total = 0
	# 	for i in range(self._list.__len__()):
	# 		if float(self._list[i].sum_score()) == float(_score):
	# 			_total += 1
	# 			# print (self._list[i])
	# 			write_str.append(str(self._list[i]))
	# 	_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
	# 	self._tmp.append('\n' + 'Result total scores ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))
	# 	return self._tmp
	#
	# def search_name(self, _list, _name):
	# 	self._list = _list
	# 	write_str = []
	# 	_total = 0
	# 	for i in range(self._list.__len__()):
	# 		if _name.lower() in str(self._list[i].get_name()).lower():
	# 			_total += 1
	# 			# print (self._list[i])
	# 			write_str.append(str(self._list[i]))
	# 	_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
	# 	self._tmp.append('\n' + 'Result Name ' + str(_name) + '\n' + str(_total) + '\n' + str(_str))
	# 	return self._tmp
	#
	# def search_id(self, _list, _id):
	# 	self._list = _list
	# 	write_str = []
	# 	_total = 0
	# 	for i in range(self._list.__len__()):
	# 		if str(_id) in self._list[i].get_id():
	# 			_total += 1
	# 			# print (self._list[i])
	# 			write_str.append(str(self._list[i]))
	# 	_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
	# 	self._tmp.append('\n' + 'Result ID ' + str(_id) + '\n' + str(_total) + '\n' + str(_str))
	# 	return self._tmp
	#
	# def search_score(self, _list, _score):
	# 	self._list = _list
	# 	write_str = []
	# 	_total = 0
	# 	find = float(_score)
	# 	for i in range(self._list.__len__()):
	# 		if float(self._list[i].get_math()) == find or float(self._list[i].get_phys()) == find or float(
	# 				self._list[i].get_chem()) == find:
	# 			_total += 1
	# 			# print (self._list[i])
	# 			write_str.append(str(self._list[i]))
	# 	_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
	# 	self._tmp.append('\n' + 'Result Score ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))
	# 	return self._tmp
	#
	# def statistic(self, _list, _score_min, _score_max):
	# 	self._list = _list
	# 	_total = 0
	# 	write_str = []
	# 	_sco_min = int(_score_min)
	# 	_sco_max = int(_score_max)
	# 	for i in range(self._list.__len__()):
	# 		if _sco_min <= float(self._list[i].sum_score()) < _sco_max:
	# 			_total = _total + 1
	# 			# print (self._list[i])
	# 			write_str.append(str(self._list[i]))
	# 	_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
	# 	self._tmp.append('\n' + 'total scores <' + str(_sco_max) + '\n' + str(_total) + '\n' + str(_str))
	# 	return self._tmp
	#
	# def md_edit(self, k, _list, str_new, i):
	# 	self._list = _list
	# 	if int(k) == 1:
	# 		student_new = str(self._list[i]).replace(self._list[i].get_name(), str_new)
	# 	elif int(k) == 2:
	# 		student_new = str(self._list[i]).replace(self._list[i].get_add(), str_new)
	# 	elif int(k) == 3:
	# 		student_new = str(self._list[i]).replace(self._list[i].get_sex(), str_new)
	#
	# 	self._list[i] = student_new
	# 	return self._list
