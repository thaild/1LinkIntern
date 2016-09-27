class Base(object):
	name = ''
	def __init__(self, name):
		self.name = name


class Concrete(Base):
	math = 0
	def __init__(self, math):
		self.math = math
	def view(self):
		print
    # Oh no, we forgot to override `bar()`.
    # def bar(self):
    #     return "bar() called"

