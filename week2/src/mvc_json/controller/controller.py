from model.model import Model


class Controller(Model):
	"""docstring for controller"""

	def __init__(self):
		super(Controller, self).__init__()
		self._tmp = []
		self._list = []

	def con_add(self, student):
		# self._list.append(student)
		Model().write_add("input.json", "w", student)

	def ct_edit(self, k, _list, str_new, i):
		self._list = Model().md_edit(k, _list, str_new, i)
		return self._list

	def con_main(self):
		students = Model().read('input.json')
		return students

	def con_delete(self, _list, _id):
		self._list = Model().md_delete(_list, _id)

	def con_search(self, k, _list, find_str):
		self._tmp = Model()._search(k, _list, find_str)
		return self._tmp

	def statistic_con(self, _list, _score_min, _score_max):
		self._tmp = Model().statistic(_list, _score_min, _score_max)
		return self._tmp
