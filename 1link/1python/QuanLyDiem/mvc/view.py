MSG = ("Enter the operation:\n- addition\t(a)\n- substraction",
       "\t(s)\n- product\t(p)\n- division\t(d)\n- modulo\t(m)\n")

class view:
	def __init__(self):
		self.__first_num = self.__Sol = None
		self.__secon_num = self.__oper = None

	def getInput(self, mode = None):
		val = None
		while True:
			if mode == 1:
				val = raw_input("enter first number: ")
				if val.isdigit():
					self.__first_num = val = int(val)
					break
			elif mode == 2:
				val = raw_input("enter second number: ")
				if val.isdigit():
					self.__secon_num = val = int(val)
					break

			elif mode == 'continue':
				val = raw_input("continue (y or n): ")
			if val == 'y' or val == 'n': break

			elif mode == 'oper':
				val = raw_input(MSG)
				if val == 'a' or val == 'm' or val == 'p' or val == 'd' or val == 's':
					self.__oper = val
					break
			else: break
		return val
	def set_sol(self, _sol):
		self.sol = _sol
		print "result: ",self.sol