class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		content = "My name is %s. I'm %s year olds." % (self.name, self.age)
		return content


student = Student("Thai", 22)
print student
