from model.model import Model
import json


class Controller(Model):
	"""docstring for controller"""

	def __init__(self):
		super(Controller, self).__init__()
		self._tmp = []
		self._list = []

	def con_add(self, student):
		list_std = Model().read('input2.json')
		for i in range(student.__len__()):
			_id = list_std.__len__() + 1
			name = student[i]._name
			add = student[i]._add
			gender = student[i]._sex
			math = student[i]._math
			phy = student[i]._physics
			chem = student[i]._chemistry
			if math > 10 or chem > 10 or phy > 10:
				return ("Scores Error!!")
			else:
				std_dict = {"gender": gender, "add": add, "chemistry": chem, "physics": phy, "math": math, "id": _id, "name": name}
				self._tmp.append(json.dumps(std_dict))
		Model().write_add("input2.json", "w", self._tmp)
		return ("Add ok!")

	def ct_edit(self, k, st_list, str_new, i):
		self._list = Model().md_edit(k, st_list, str_new, i)
		return self._list

	def con_main(self):
		self._list = Model().read('input2.json')
		return self._list

	def con_delete(self, lists, id_st):
		Model().md_delete(lists, id_st)

	def con_search(self, k, std_list, find_str):
		self._tmp = Model().search(k, std_list, find_str)
		return self._tmp

	def statistic_con(self, st_list, score_min, score_max):
		self._tmp = Model().statistic(st_list, score_min, score_max)
		return self._tmp
