
import sys

from controller.controller import Controller
from model.model import Model


class View(object):
	"""docstring for view"""
	def __init__(self):
		super(View, self).__init__()
		self._tmp = []
		self._list = []

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
			student = Model(_id, name, add, sex, math, physics, chemistry)
			print (student)
			self._tmp.append(str(student))
		return self._tmp

	def _edit_option(self, _list):
		id_edit = int(raw_input('Enter ID Edit: '))
		for i in range(_list.__len__()):
			if int(_list[i].get_id()) == id_edit:
				print (_list[i])
				menu = "Select: Edit Student\n1. name\n2. Address\n3. Sex\n0. Return "
				while True:
					choice = (raw_input(menu+"\nChoose 0 -> 3: (press 0 to Return) "))
					choice = int(choice)
					if choice == 0:
						print ('Return...')
						break

					elif choice == 1:
						str_new = raw_input('Enter Name New: ')
						self._tmp = Controller().ct_edit(str(choice), _list, str_new, i)

					elif choice == 2:
						str_new = raw_input('Enter Add New: ')
						self._tmp = Controller().ct_edit(str(choice), _list, str_new, i)

					elif choice == 3:
						str_new = raw_input('Enter Sex New: ')
						self._tmp = Controller().ct_edit(str(choice), _list, str_new, i)

					else:
						print("Not Exist!")
					print (str(_list[i]))
					Model().write('input.txt', 'w', self._tmp)
					return _list

		else:
			print ('done!!')

	def _search_option(self, _list):
		list_std = _list
		menu = "Search Student:\n1. total scores: \n2. ID: \n3. Name\n4. Score\n0. Return"
		while True:
			choice = int(raw_input(menu+"Choose 0 -> 4 (press 0 to return): "))
			if choice == 0:
				print ('Return...')
				break

			elif choice == 1:
				find_str = raw_input('enter total score: ')
				self._tmp = Controller().con_search(str(choice), list_std, find_str)
				print (self._tmp)
				Model().write('search.txt', 'a+', self._tmp)
			elif choice == 2:
				find_str = raw_input('enter ID: ')
				self._tmp = Controller().con_search(str(choice), list_std, find_str)
				print (self._tmp)
				Model().write('search.txt', 'a+', self._tmp)
			elif choice == 3:
				find_str = raw_input('enter Name: ')
				self._tmp = Controller().con_search(str(choice), list_std, find_str)
				print (self._tmp)
				Model().write('search.txt', 'a+', self._tmp)
			elif choice == 4:
				find_str = raw_input('enter score: ')
				self._tmp = Controller().con_search(str(choice), list_std, find_str)
				print (self._tmp)
				Model().write('search.txt', 'a+', self._tmp)
			else:
				print("Not EXISTS")

	def _statistic_option(self, _list):
		menu = "Statistics Student:\n1. total < 15: \n2. 15 <= total < 20: \n3. 20 <= total < 25\n4. total > 25\n0. Return"

		while True:
			choice = int(raw_input(menu+"\nNhap lua chon 0 -> 4: "))
			if choice == 0:
				print ('Return...')
				break

			elif choice == 1:
				print ("1. total < 15 ")
				self._tmp = Controller().statistic_con(_list, '0', '15')
				print (str(self._tmp))
				Model().write('statistic.txt', 'a', self._tmp)
			elif choice == 2:
				print ("2. 15 <= total < 20: ")
				self._tmp = Controller().statistic_con(_list, '15', '20')
				print (str(self._tmp))
				Model().write('statistic.txt', 'a', self._tmp)

			elif choice == 3:
				print ("3. 20 <= total < 25")
				self._tmp = Controller().statistic_con(_list, '20', '25')
				print (str(self._tmp))
				Model().write('statistic.txt', 'a', self._tmp)

			elif choice == 4:
				print ("4. total > 25")
				self._tmp = Controller().statistic_con(_list, '25', '30')
				print self._tmp
				Model().write('statistic.txt', 'a', self._tmp)

			else:
				print("khong co lua chon nay ")

	def main_view(self):
		menu = "..::STUDENT MANAGER::..\n1. Enter infor student form keyboard\n2. View list Student\n3. Edit a Student\n4. Delete a Student\n5. Search\n6. Statistics\n0. Exit"
		list_std = Model().read('input.txt', 'r')

		while True:
			choice = input(menu+"\nMain - Choose 0 -> 6: ")
			if choice == 0:
				print ('Exiting...')
				sys.exit(1)
			elif choice == 2:
				print ('List Student:')
				self._list = (Controller().con_main())
				for i in range(self._list.__len__()):
					print (self._list[i])
			elif choice == 1:
				self._add_student()
				Controller().con_add('input.txt', 'a', self._tmp)
			elif choice == 3:
				self._edit_option(list_std)
			elif choice == 4:
				id_del = int(raw_input('Nhap id Student can xoa: '))
				for j in range(0, list_std.__len__()):
					if id_del == int(list_std[j].get_id()):
						print (list_std[j])
				self._tmp = Controller().con_delete(list_std, id_del)
				print ('Deleted!')
			elif choice == 5:
				self._search_option(Model().sorted(list_std))
			elif choice == 6:
				self._statistic_option(list_std)

			else:
				print("Choose not exists")

