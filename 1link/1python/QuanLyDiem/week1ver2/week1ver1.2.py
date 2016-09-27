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

	# return 'Student: id {self._id}, name {self._name}, Add: {self._add}, Gender:{self._sex}, Math {self._math}, Physics {self._physics}, Chemistry {self._chemistry}'.format(self=self)


class students(object):
	"""docstring for students"""

	def __init__(self):
		super(students, self).__init__()
		self._list = []
		self._tmp = []

	def _show(self):
		for i in range(self._list.__len__()):
			print self._list[i]

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
			# _str = _str.lstrip('[').rstrip(']').replace(",", "\n", n-1).replace("'", "", n*2)
			# _str = _str.strip()
			# print _str
			fo.writelines(_str)
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
		pass

	def _search(self, _list_std):
		write_str = []

		def _score():
			write_str = []
			write_str.append('\n\tResult search score:\n')
			score = float(raw_input('Enter scores: '))
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) == score:
					print _list_std[i]
					write_str.append(_list_std[i])
			return write_str

		def _name():
			write_str = []
			write_str.append('\n\tResult search name:\n')
			f_name = float(raw_input('enter name: '))
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) == f_name:
					print _list_std[i]
					write_str.append(_list_std[i])
			return write_str

		def _id():
			write_str.append('\n\tResult search id:\n')
			f_id = float(raw_input('enter id: '))
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) == f_id:
					print _list_std[i]
					write_str.append(_list_std[i])
			return write_str

		def _total_scores():
			write_str = []
			write_str.append('\n\tResult search total scores:\n')
			t_score = float(raw_input('enter total scores: '))
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) == t_score:
					print _list_std[i]
					write_str.append(_list_std[i])
			return write_str

		def search_save(file_name, _modes):
			fo = open(file_name, _modes)
			for i in range(write_str.__len__()):
				_str = str(self._tmp[i])
				# _str = _str.lstrip('[').rstrip(']').replace(",", "\n", n-1).replace("'", "", n*2)
				# _str = _str.strip()
				print _str
				fo.writelines(_str)
			fo.close()

		print ("Search Student:")
		print ("1. theo tong so diem: ")
		print ("2. theo SBD: ")
		print ("3. theo Name")
		print ("4. theo diem")
		print ("0. Return")
		while True:
			choice = (raw_input("Choose 0 -> 4 (press 0 to return): "))
			choice = int(choice)
			if choice == 0:
				print ('Return...')
				_list._menu()
				break
			elif choice == 1:
				_total_scores()
				search_save('search.txt', 'a+')
				break
			elif choice == 2:
				_total_scores()
				search_save('search.txt', 'a+')

			elif choice == 3:
				_total_scores()
				search_save('search.txt', 'a+')

			elif choice == 4:
				_total_scores()
				search_save('search.txt', 'a+')

			else:
				print("Not EXISTS")

	def _statistic(self, _list_std):
		def _total15():
			_total = 0
			write_str = []
			write_str.append('\nStudent co total < 15:\n')
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) < 15:
					_total = _total + 1
					print _list_std[i]
				write_str.append(_list_std[i])
			return self._tmp.append(write_str)

		def _total1520():
			_total = 0
			write_str = []
			write_str.append('\nStudent co total < 20:\n')
			for i in range(_list_std.__len__()):
				if 15 <= float(_list_std[i].sum_score()) < 20:
					_total = _total + 1
					print _list_std[i]
				write_str.append(_list_std[i])
			return self._tmp.append(write_str)

		def _total2025():
			_total = 0
			write_str = []
			write_str.append('\nStudent co total < 25:\n')
			for i in range(_list_std.__len__()):
				if 20 <= float(_list_std[i].sum_score()) < 25:
					_total = _total + 1
					print _list_std[i]
				write_str.append(_list_std[i])
			return self._tmp.append(write_str)

		def _total25():
			_total = 0
			write_str = []
			write_str.append('\nStudent co total >= 25:\n')
			for i in range(_list_std.__len__()):
				if float(_list_std[i].sum_score()) >= 25:
					_total = _total + 1
					print _list_std[i]
				write_str.append(_list_std[i])
			return self._tmp.append(write_str)

		print ("Statistics Student:")
		print ("1. total < 15: ")
		print ("2. 15 <= total < 20: ")
		print ("3. 20 <= total < 25")
		print ("4. total > 25")
		print ("0. Return")

		while True:
			choice = (raw_input("Nhap lua chon 0 -> 4: "))
			choice = int(choice)
			if choice == 0:
				print ('Return...')
				_list._menu()
				break
			elif choice == 1:
				print ("1. total < 15 ")
				_total15()
			elif choice == 2:
				print ("2. 15 <= total < 20: ")
				_total1520()
			elif choice == 3:
				print ("3. 20 <= total < 25")
				_total2025()
			elif choice == 4:
				print ("4. total > 25")
				_total25()
			else:
				print("khong co lua chon nay ")

	def _delete_student(self, _list_std):
		id_del = int(raw_input('Nhap id Student can xoa: '))
		for j in range(0, _list_std.__len__() - 1):
			if int(_list_std[j].get_id()) == id_del:
				print (_list_std[j])
				del _list_std[j]
			self._tmp = _list_std
		print 'Deleted!'
		return self._tmp

	def _delete_students(self):
		_temp = self._list
		id_del = int(raw_input('Nhap id Student can xoa: '))
		for j in range(0, self._list.__len__() - 1):
			if int(self._list[j].get_id()) == id_del:
				print (self._list[j])
				del self._list[j]
			self._tmp.append(str(self._list[j]) + '\n')
		print self._tmp
		print ('Deleted!')
		return self._tmp

	def _edit_student(self, _list_stu):
		tmp = []

		def edit_menu():
			print ("Select: Edit Student")
			print ("1. name: ")
			print ("2. Add:")
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
					_name()
					break
				elif choice == 2:
					_add()
					break
				elif choice == 3:
					_sex()
					break
				else:
					print("Not Exist!")

		def _name():
			name_new = raw_input('Enter Name New: ')
			student_new = str(_list_stu[i]).replace(_list_stu[i].get_name(), name_new)
			print student_new
			tmp.append(student_new)
			edit_save()

		def _add():
			add_new = raw_input('Enter Add New: ')
			student_new = _list_stu[i].replace(_list_stu[i].get_add(), add_new)
			print student_new
			tmp.append(student_new)
			edit_save()

		def _sex():
			sex_new = raw_input('Enter Sex New: ')
			student_new = _list_stu[i].replace(_list_stu[i].get_sex(), sex_new)
			print student_new
			tmp.append(student_new)
			edit_save()

		def edit_save():
			fo = open('input.txt', 'a')
			_str = str(tmp)
			_str = _str.lstrip('[').rstrip(']').replace("'", "", 2).strip()
			fo.write('\n' + _str)
			del tmp[0:1]
			fo.close()

		id_edit = int(raw_input('Enter ID Edit: '))
		for i in range(_list_stu.__len__()):
			if int(_list_stu[i].get_id()) == id_edit:
				print (self._list[i])
				edit_menu()
		else:
			print ('Edited!!')

	def _menu(self):
		print ("Student manager")
		print ("1. Read & View list Student from file")
		print ("2. input information Student form keyboard")
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
				_list._write('input.txt', 'a')
			elif choice == 3:
				_list._edit_student(_list._read('input.txt', 'r'))
			elif choice == 4:
				_list._delete_students()
				_list._write('input.txt', 'w')
			elif choice == 5:
				_list._search(_list._read('input.txt', 'r'))
			# _list._write('search.txt', 'w')
			elif choice == 6:
				_list._statistic(_list._read('input.txt', 'r'))
				_list._write('statistic.txt', 'w')
			else:
				print("Choose not exists")


if __name__ == '__main__':
	_list = students()
	_list._read('input.txt', 'r')
	_list._menu()
