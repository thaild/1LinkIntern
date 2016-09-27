

import json
from model.model import Model

students = Model()
std = {}
fi = open("input.json")
fo = open("output.json", "w+")
data = fi.read()
students = json.loads(data)
fo.write('[\n')
for i in range(students.__len__()-1):
	fo.write(str(json.dumps(students[i]))+',\n')
fo.write(str(json.dumps(students[students.__len__()-1])))
fo.write(']')
#out = json.dumps(std)
#print demjson.decode(std)

#fo.write(out)
# fi = (json.dumps({'id': 11, 'name': "le dinh thai", "add":"Hanoi","gender":"nam","score":{"math":8,"physics":9, "chemistry":10}}))



fo.close()
fi.close()