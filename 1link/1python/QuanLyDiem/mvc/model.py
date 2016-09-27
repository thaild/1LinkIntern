class model:
	def __init__(self):
		self.__solution = 0
	def _calc(self,a,b, oper):
		if oper is 'm':
			self.__solution = a%b
		if oper is 'd':
			self.__solution = a / float(b)
		if oper is 'p':
			self.__solution = a * b
		if oper is 'a':
			self.__solution = a + b
		if oper is 's':
			self.__solution = a - b


	def get_sol(self):
		return self.__solution
