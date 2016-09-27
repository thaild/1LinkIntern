
import sys


class Student(object):
	def __init__(self, _id=None, name=None, add=None, sex=None, math=0, physics=0, chemistry=0):
		self._name = name
		self._id = _id
		self._add = add
		self._sex = sex
		self._math = float(math)
		self._physics = float(physics)
		self._chemistry = float(chemistry)

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def get_add(self):
		return self._add

	def get_sex(self):
		return self._sex

	def get_math(self):
		return self._math

	def get_phys(self):
		return self._physics

	def get_chem(self):
		return self._chemistry

	def sum_score(self):
		return self._math + self._physics + self._chemistry

	def __str__(self):
		return '{self._id} {self._name} {self._add} {self._sex} {self._math} {self._physics} {self._chemistry}'.format(
			self=self)


class students(object):
	"""docstring for students"""

	def __init__(self):
		super(students, self).__init__()
		self._list = []
		self._tmp = []

	def _read(self, file_name, _modes):
		self._list = []
		for line in open(file_name, _modes):
			line.strip()
			_id, name, add, sex, math, physics, chemistry = line.split()
			_str = Student(_id, name, add, sex, math, physics, chemistry)
			self._list.append(_str)
		return self._list

	def _write(self, file_name, _modes, _tmp):
		fo = open(file_name, _modes)
		for i in range(_tmp.__len__()):
			_str = str(_tmp[i])+'\n'
			fo.writelines(_str)
		del _tmp[0:_tmp.__len__()]
		fo.close()


class view(students):
	"""docstring for view"""
	def __init__(self):
		super(view, self).__init__()
		self._tmp = []
		self._list = []

	def _show(self, _list):
		for i in range(_list.__len__()):
			print (_list[i])

	def _add_student(self):
		n = int(input('Nhap n: '))
		for i in range(n):
			print ("Nhap thong tin cho Student {}".format(i + 1))
			_id = raw_input('Nhap ID: ')
			name = raw_input('Nhap Name: ')
			add = raw_input('Nhap add: ')
			sex = raw_input('Nhap Sex: ')
			math = float(raw_input('Nhap diem Toan: '))
			physics = float(raw_input('Nhap diem ly: '))
			chemistry = float(raw_input('Nhap diem hoa: '))
			student = Student(_id, name, add, sex, math, physics, chemistry)
			print (student)
		self._tmp.append(str(student))
		return self._tmp

	def _edit_option(self, _list):
		id_edit = int(raw_input('Enter ID Edit: '))
		for i in range(_list.__len__()):
			if int(_list[i].get_id()) == id_edit:
				print (_list[i])
				k = i
				print ("Select: Edit Student")
				print ("1. name: ")
				print ("2. Address:")
				print ("3. Sex:")
				print ("0. Return")
				while True:
					choice = (raw_input("Choose 0 -> 3: (press 0 to Return)"))
					choice = int(choice)
					if choice == 0:
						print ('Return...')
						view._menu()

					elif choice == 1:
						self._tmp = controller()._edit_name(_list, k)
						students()._write('input.txt', 'w', self._tmp)
					elif choice == 2:
						self._tmp = controller()._edit_add(_list, k)
						students()._write('input.txt', 'w', self._tmp)

					elif choice == 3:
						self._tmp = controller()._edit_sex(_list, k)
						students()._write('input.txt', 'w', self._tmp)

					else:
						print("Not Exist!")
		else:
			print ('done!!')

	def _search_option(self, _list):
		list_std = _list
		print ("Search Student:")
		print ("1. total scores: ")
		print ("2. ID: ")
		print ("3. Name")
		print ("4. Score")
		print ("0. Return")
		while True:
			choice = int(raw_input("Choose 0 -> 4 (press 0 to return): "))
			if choice == 0:
				print ('Return...')
				view._menu()

			elif choice == 1:
				_total = raw_input('enter total score: ')
				self._tmp = controller()._search_total_score(list_std, _total)
				students()._write('search.txt', 'a+', self._tmp)
			elif choice == 2:
				_id = raw_input('enter ID: ')
				self._tmp = controller()._search_id(list_std, _id)
				students()._write('search.txt', 'a+', self._tmp)
			elif choice == 3:
				_name = raw_input('enter Name: ')
				self._tmp = students()._search_name(list_std, _name)
				controller()._write('search.txt', 'a+', self._tmp)
			elif choice == 4:
				_score = raw_input('enter score: ')
				self._tmp = controller()._search_score(list_std, _score)
				students()._write('search.txt', 'a+', self._tmp)
			else:
				print("Not EXISTS")

	def _statistic_option(self, _list):
		print ("Statistics Student:")
		print ("1. total < 15: ")
		print ("2. 15 <= total < 20: ")
		print ("3. 20 <= total < 25")
		print ("4. total > 25")
		print ("0. Return")

		while True:
			choice = int(raw_input("Nhap lua chon 0 -> 4: "))
			if choice == 0:
				print ('Return...')
				view._menu()

			elif choice == 1:
				print ("1. total < 15 ")
				self._tmp = controller()._statistic_con(_list, '0', '15')
				students()._write('statistic.txt', 'a', self._tmp)
			elif choice == 2:
				print ("2. 15 <= total < 20: ")
				self._tmp = controller()._statistic_con(_list, '15', '20')
				students()._write('statistic.txt', 'a', self._tmp)
			elif choice == 3:
				print ("3. 20 <= total < 25")
				self._tmp = controller()._statistic_con(_list, '20', '25')
				students()._write('statistic.txt', 'a', self._tmp)
			elif choice == 4:
				print ("4. total > 25")
				self._tmp = controller()._statistic_con(_list, '25', '30')
				students()._write('statistic.txt', 'a', self._tmp)
			else:
				print("khong co lua chon nay ")

	def _menu(self):
		print ("Student manager")
		print ("1. Enter infor student form keyboard")
		print ("2. View list Student")
		print ("3. Edit a Student")
		print ("4. Delete a Student")
		print ("5. Search")
		print ("6. Statistics")
		print ("0. Exit")
		list_std = students()._read('input.txt', 'r')

		while True:
			choice = input("\nMain - Choose 0 -> 6: ")
			if choice == 0:
				print ('Exiting...')
				sys.exit(1)
			elif choice == 2:
				print ('List Student:')
				view._show(list_std)
				view._menu()
			elif choice == 1:
				view._add_student()
				students()._write('input.txt', 'a', self._tmp)
			elif choice == 3:
				view._edit_option(list_std)
			elif choice == 4:
				id_del = int(raw_input('Nhap id Student can xoa: '))
				self._tmp = controller()._delete_students(list_std, id_del)
				students()._write('input.txt', 'w', self._tmp)
			elif choice == 5:
				view._search_option(controller()._sorted(list_std))
			elif choice == 6:
				view._statistic_option(list_std)

			else:
				print("Choose not exists")


class controller(students):
	"""docstring for controller"""

	def __init__(self):
		super(controller, self).__init__()
		self._tmp = []
		self._list = []

	def _edit_name(self, _list, i):
		self._list = _list
		name_new = raw_input('Enter Name New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_name(), name_new)
		self._list[i] = student_new
		print (student_new)
		return self._list

	def _edit_add(self, _list, i):
		self._list = _list
		add_new = raw_input('Enter Add New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_add(), add_new)
		self._list[i] = student_new
		print (student_new)
		return self._list

	def _edit_sex(self, _list, i):
		self._list = _list
		sex_new = raw_input('Enter Sex New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_sex(), sex_new)
		self._list[i] = student_new
		print (student_new)
		return self._list

	def _delete_students(self, _list, id_del):
		self._list = _list
		n = self._list.__len__()
		for j in range(0, n-1):
			if id_del == int(self._list[j].get_id()):
				print (self._list[j])
				del self._list[j]
			self._tmp.append(str(self._list[j]))
		print ('Deleted!')
		return self._tmp

	def _sorted(self, _list):
		self._list = _list
		for j in range(0, self._list.__len__() - 1):
			if int(self._list[j].get_id()) > int(self._list[j + 1].get_id()):
				self._list[j], self._list[j + 1] = self._list[j + 1], self._list[j]
		return self._list

	def _search_total_score(self, _list, _score):
		self._list = _list
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if float(self._list[i].sum_score()) == float(_score):
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		self._tmp.append('\n' + 'Result total scores ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))
		return self._tmp

	def _search_name(self, _list, _name):
		self._list = _list
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if _name.lower() in str(self._list[i].get_name()).lower():
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		self._tmp.append('\n' + 'Result Name ' + str(_name) + '\n' + str(_total) + '\n' + str(_str))
		return self._tmp

	def _search_id(self, _list, _id):
		self._list = _list
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if str(_id) in self._list[i].get_id():
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		self._tmp.append('\n' + 'Result ID ' + str(_id) + '\n' + str(_total) + '\n' + str(_str))
		return self._tmp

	def _search_score(self, _list, _score):
		self._list = _list
		write_str = []
		_total = 0
		find = float(_score)
		for i in range(self._list.__len__()):
			if float(self._list[i].get_math()) == find or float(self._list[i].get_phys()) == find or float(
					self._list[i].get_chem()) == find:
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		self._tmp.append('\n' + 'Result Score ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))
		return self._tmp

	def _statistic_con(self, _list, _score_min, _score_max):
		self._list = _list
		_total = 0
		write_str = []
		_sco_min = int(_score_min)
		_sco_max = int(_score_max)
		for i in range(self._list.__len__()):
			if _sco_min <= float(self._list[i].sum_score()) < _sco_max:
				_total = _total + 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		self._tmp.append('\n' + 'total scores <' + str(_sco_max) + '\n' + str(_total) + '\n' + str(_str))
		return self._tmp


if __name__ == '__main__':
	view = view()
	view._menu()