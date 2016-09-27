import sys


class Student(object):
	def __init__(self, id='', name='', add='', sex='', math=0, physics=0, chemistry=0):
		self.name = name
		self.id = id
		self.add = add
		self.sex = sex
		self.math = float(math)
		self.physics = float(physics)
		self.chemistry = float(chemistry)

	def _read(self):
		self.lines = [line.rstrip('\n') for line in open('import.txt')]
		# self.lines = open('import.txt').read().splitlines()
		return self.lines

	def _show(self):
		self.students = student._read()
		print "list student:"
		print self.students

	def _read(self):
		self.students = []
		for line in open('import.txt'):
			line.strip()
			id, name, add, sex, math, physics, chemistry = line.split()
			Student = {"id": id, "name": name, "add": add, "sex": sex, "math": math, "physics": physics, "chemistry": chemistry}  # dict
			self.students.append(Student)
		return self.students


if __name__ == '__main__':
	# student = Student("id", 'name', 'add', 'sex', 0, 0, 0)
	student = Student()
	student._show()
