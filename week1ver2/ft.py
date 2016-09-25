import sys


class Student(object):
	def __init__(self, _id, name, add, sex, math, physics, chemistry):
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

	def _show(self):
		for i in range(self._list.__len__()):
			print (self._list[i])

	def _read(self, file_name, _modes):
		self._list = []
		for line in open(file_name, _modes):
			line.strip()
			_id, name, add, sex, math, physics, chemistry = line.split()
			# Student = {"id": id, "name": name, "add": add, "sex": sex, "math": math, "physics": physics,"chemistry": chemistry}
			_str = Student(_id, name, add, sex, math, physics, chemistry)
			self._list.append(_str)
		return self._list

	def _write(self, file_name, _modes):
		fo = open(file_name, _modes)
		for i in range(self._tmp.__len__()):
			_str = str(self._tmp[i])
			fo.writelines(_str)
		del self._tmp[0:self._tmp.__len__()]
		fo.close()

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
			self._tmp.append('\n' + str(student))

	def _sorted(self):
		for j in range(0, self._list.__len__()-1):
			if int(self._list[j].get_id()) > int(self._list[j+1].get_id()):
				self._list[j], self._list[j+1] = self._list[j+1], self._list[j]
		return self._list

	def _search_option(self):
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
				_list._menu()
				break
			elif choice == 1:
				_total = raw_input('enter total score: ')
				_list._search_total_score(_total)
				_list._write('search.txt', 'a+')
				break
			elif choice == 2:
				_id = raw_input('enter ID: ')
				_list._search_id(_id)
				_list._write('search.txt', 'a+')

			elif choice == 3:
				_name = raw_input('enter Name: ')
				_list._search_name(_name)
				_list._write('search.txt', 'a+')

			elif choice == 4:
				_score = raw_input('enter score: ')
				_list._search_score(_score)
				_list._write('search.txt', 'a+')
			else:
				print("Not EXISTS")

	def _search_total_score(self, _score):
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if float(self._list[i].sum_score()) == float(_score):
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		return self._tmp.append('\n' + 'Result total scores ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))

	def _search_name(self, _name):
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if _name.lower() in str(self._list[i].get_name()).lower():
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		return self._tmp.append('\n' + 'Result Name ' + str(_name) + '\n' + str(_total) + '\n' + str(_str))

	def _search_id(self, _id):
		write_str = []
		_total = 0
		for i in range(self._list.__len__()):
			if self._list[i].get_id() == _id:
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		return self._tmp.append('\n' + 'Result ID ' + str(_id) + '\n' + str(_total) + '\n' + str(_str))

	def _search_score(self, _score):
		write_str = []
		_total = 0
		find = float(_score)
		for i in range(self._list.__len__()):
			if self._list[i].get_math() == find or self._list[i].get_phys() == find or self._list[i].get_chem() == find:
				_total += 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total * 2).strip()
		return self._tmp.append('\n' + 'Result Score ' + str(_score) + '\n' + str(_total) + '\n' + str(_str))

	def _statistic_option(self):
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
				_list._menu()
				break
			elif choice == 1:
				print ("1. total < 15 ")
				_list._statistic_con('0','15')
				_list._write('statistic.txt', 'a')
			elif choice == 2:
				print ("2. 15 <= total < 20: ")
				_list._statistic_con('15','20')
				_list._write('statistic.txt', 'a')
			elif choice == 3:
				print ("3. 20 <= total < 25")
				_list._statistic_con('20','25')
				_list._write('statistic.txt', 'a')
			elif choice == 4:
				print ("4. total > 25")
				_list._statistic_con('25','30')
				_list._write('statistic.txt', 'a')
			else:
				print("khong co lua chon nay ")

	def _statistic_con(self,_score_min, _score_max):
		_total = 0
		write_str = []
		_sco_min = int(_score_min)
		_sco_max = int(_score_max)
		for i in range(self._list.__len__()):
			if _sco_min <= float(self._list[i].sum_score()) < _sco_max:
				_total = _total + 1
				print (self._list[i])
				write_str.append(str(self._list[i]))
		_str = str(write_str).lstrip('[').rstrip(']').replace(",", "\n", _total).replace("'", "", _total*2).strip()
		return self._tmp.append('\n'+'total scores <'+str(_sco_max)+'\n'+str(_total)+'\n'+str(_str))

	def _delete_students(self):
		id_del = int(raw_input('Nhap id Student can xoa: '))
		for j in range(0, self._list.__len__() - 1):
			if int(self._list[j].get_id()) == id_del:
				print (self._list[j])
				del self._list[j]
			self._tmp.append(str(self._list[j])+'\n')
		print ('Deleted!')
		return self._tmp

# gop 3 def name, add, sex thanh 1 def?
# co the sua 1 sinhvien[i] ngay trong file k?
# neu ghi W+ thi khi bi loi file goc se mat sach

	def _edit_option(self):
		id_edit = int(raw_input('Enter ID Edit: '))
		for i in range(self._list.__len__()):
			if int(self._list[i].get_id()) == id_edit:
				print (self._list[i])
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
						_list._menu()
						break
					elif choice == 1:
						_list._edit_name(k)
						break
					elif choice == 2:
						_list._edit_add(k)
						break
					elif choice == 3:
						_list._edit_sex(k)
						break
					else:
						print("Not Exist!")
		else:
			print ('done!!')

	def _edit_name(self, i):
		name_new = raw_input('Enter Name New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_name(), name_new)
		self._list[i] = student_new
		print (student_new)
		self._tmp = self._list

	def _edit_add(self, i):
		add_new = raw_input('Enter Add New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_add(), add_new)
		self._list[i] = student_new
		print (student_new)
		self._tmp = self._list

	def _edit_sex(self, i):
		sex_new = raw_input('Enter Sex New: ')
		student_new = str(self._list[i]).replace(self._list[i].get_sex(), sex_new)
		self._list[i] = student_new
		print (student_new)
		self._tmp = self._list

	def edit_save(self, file_name, _modes):
		fo = open(file_name, _modes)
		for i in range(self._tmp.__len__()):
			_str = str(self._tmp[i])
			fo.write(_str+'\n')
		fo.close()

	def _menu(self):
		print ("Student manager")
		print ("1. Read & View list Student from file")
		print ("2. Enter infor student form keyboard")
		print ("3. Edit a Student")
		print ("4. Delete a Student")
		print ("5. Search")
		print ("6. Statistics")
		print ("0. Exit")

		while True:
			choice = input("\nMain - Choose 0 -> 5: ")
			if choice == 0:
				print ('Exiting...')
				sys.exit(1)
			elif choice == 1:
				print ('List Student:')
				_list._show()
				_list._menu()
			elif choice == 2:
				_list._add_student()
				_list._write('output.txt', 'a')
			elif choice == 3:
				_list._edit_option()
				_list.edit_save('output.txt','w')
			elif choice == 4:
				_list._delete_students()
				_list._write('output.txt', 'w')
			elif choice == 5:
				_list._sorted()
				_list._search_option()
			elif choice == 6:
				_list._statistic_option()
			else:
				print("Choose not exists")

if __name__ == '__main__':
	_list = students()
	_list._read('output.txt', 'r')
	_list._menu()
