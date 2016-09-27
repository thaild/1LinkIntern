

def divide(a, b):
	if (b == 0):
		raise Exception("[error] divide by zero")
	else:
		return b / a

try:
	c = divide(3, 5)
	print c
except Exception, e:
	print e
# c = divide(1, 0)
# print c