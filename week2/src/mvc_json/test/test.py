import json
from model.model import Student
inp = {"gender": "nam", "add": "ha noi", "chemistry": 9, "physics": 8, "math": 4, "id": "01", "name": "thai"}
data_file = open("input2.json").read()
Student.__dict__ = json.loads(inp)
for std in Student:
	print std
