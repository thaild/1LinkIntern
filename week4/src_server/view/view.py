
import sys
import json, threading
from controller.controller import Controller
from model.model import Model, Student


class View(object):
	"""docstring for view"""
	def __init__(self):
		super(View, self).__init__()
		self._tmp = []
		self._list = []

	def show_student(self, std):
		return str(std._id) + ' ' + str(std._name) + ' ' + str(std._add) + ' ' + str(std._sex) + ' ' + str(std._math) + ' ' + str(std._chemistry) + ' ' + str(std._physics)

	def add_student(self):
		n = int(input('Nhap n: '))
		for i in range(n):
			print ("Nhap thong tin cho Student {}".format(i + 1))
			_id = 'id'
			name = raw_input('Nhap Name: ')
			add = raw_input('Nhap add: ')
			sex = raw_input('Nhap Sex: ')
			math = float(raw_input('Nhap diem Toan: '))
			phy = float(raw_input('Nhap diem ly: '))
			chem = float(raw_input('Nhap diem hoa: '))
			student = Student(_id, name, add, sex, math, phy, chem)
			self._tmp.append(student)
		return self._tmp

	def edit_option(self, std_list):
		id_edit = int(raw_input('Enter ID Edit: '))
		for i in range(std_list.__len__()):
			if int(std_list[i]["id"]) == id_edit:
				print (str(json.dumps(std_list[i])))
				menu = "Select: Edit Student\n1. name\n2. Address\n3. Sex\n0. Return"
				while True:
					choice = (raw_input(menu+"\nChoose 0 -> 3: (press 0 to Return) "))
					choice = int(choice)
					if choice == 0:
						print ('Return...')
						break
					elif choice == 1 or choice == 2 or choice == 3:
						str_new = raw_input('Enter New: ')
						self._tmp = Controller().ct_edit(str(choice), std_list, str_new, i)
					else:
						print("Not Exist!")
					print (str(json.dumps(std_list[i])))
					Model().write('input2.json', 'w', self._tmp)
					return std_list

		else:
			print ('done!!')

	def search_option(self, std_list):
		menu = "Search Student:\n1. total scores \n2. ID: \n3. Name\n4. Score\n0. Return"
		while True:
			choice = int(raw_input(menu+"\nChoose 0 -> 4 (press 0 to return): "))
			if choice == 0:
				print ('Return...')
				break
			elif choice == 1 or choice == 2 or choice == 3 or choice == 4:
				find_str = raw_input('Enter search: ')
				self._tmp = Controller().con_search(str(choice), std_list, find_str)
				print (self._tmp)
			else:
				print("Not EXISTS")

	def statistic_option(self, list):
		menu = "Statistics Student:\n1. total < 15 \n2. 15 <= total < 20 \n3. 20 <= total < 25\n4. total > 25\n0. Return"
		while True:
			choice = int(raw_input(menu+"\nNhap lua chon 0 -> 4: "))
			if choice == 0:
				print ('Return...')
				break
			elif choice == 1:
				print ("1. total < 15 ")
				self._tmp = Controller().statistic_con(list, '0', '15')
				print (str(self._tmp))
			elif choice == 2:
				print ("2. 15 <= total < 20: ")
				self._tmp = Controller().statistic_con(list, '15', '20')
				print (str(self._tmp))
			elif choice == 3:
				print ("3. 20 <= total < 25")
				self._tmp = Controller().statistic_con(list, '20', '25')
				print (str(self._tmp))
			elif choice == 4:
				print ("4. total > 25")
				self._tmp = Controller().statistic_con(list, '25', '30')
				print self._tmp
			else:
				print("Choose not exists")

	def view_student(self, students):
		for student in students:
			print (student["id"] + ' | ' + student["name"] + ' | ' + student["add"] + ' | ' + student["gender"] + ' | ' + str(student["math"]) + ' | ' + str(student["physics"]) + ' | ' + str(student["chemistry"]))

	def main_view(self):
		menu = "..::STUDENT MANAGER::..\n1. Enter infor student form keyboard\n2. View list Student\n3. Edit a Student\n4. Delete a Student\n5. Search\n6. Statistics\n0. Exit"
		list_std = Model().read('input2.json')

		while True:
			choice = input(menu+"\nMain - Choose 0 -> 6: ")
			if choice == 0:
				print ('Exiting...')
				sys.exit(1)
			elif choice == 1:
				self._tmp = self.add_student()
				for std in self._tmp:
					print Model().student_print(std)
				print Controller().con_add(self._tmp)
			elif choice == 2:
				print ('List Student:')
				lists = Controller().con_main()
				self.view_student(lists)
			elif choice == 3:
				self.edit_option(list_std)
			elif choice == 4:
				id_del = int(raw_input('Nhap id Student can xoa: '))
				for j in range(0, list_std.__len__()):
					if id_del == int(list_std[j]["id"]):
						print (str(json.dumps(list_std[j])))
				Controller().con_delete(list_std, id_del)
				print ('Deleted!')
			elif choice == 5:
				self.search_option(Model().sorted(list_std))
			elif choice == 6:
				self.statistic_option(list_std)

			else:
				print("Choose not exists")

