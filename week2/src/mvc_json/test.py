

import json
from model.model import Model

student = {}
scores = {}
fi = open("input.json").read()
# fo = open("output.json", "w+")
data = json.loads(fi)
for x in data:
	# print x["name"]
	pass

student["id"] = "12"
student["name"] = "thai12"
student["add"] = "thai12"
student["gender"] = "thai12"
student["scores"] = scores
scores["math"] = 9
scores["physics"] = 9
scores["chemistry"] = 9

print json.dumps(student, ensure_ascii=False)




# students = json.loads(data)
# for std in students:
# 	print std
#
# fo.write('[\n')
# for i in range(students.__len__()-1):
# 	fo.write(str(json.dumps(students[i]))+',\n')
# fo.write(str(json.dumps(students[students.__len__()-1])))
# fo.write(']')
#out = json.dumps(std)
#print demjson.decode(std)

#fo.write(out)
# fi = (json.dumps({'id': 11, 'name': "le dinh thai", "add":"Hanoi","gender":"nam","score":{"math":8,"physics":9, "chemistry":10}}))



fo.close()
fi.close()