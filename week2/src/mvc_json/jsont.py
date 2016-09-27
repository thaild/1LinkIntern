import json

json_data = open("output.json").read()
per =json.loads(json_data)
for i in range(per.__len__()):
	for x in per["persons"]:
		print x["name"]
		pass
# da = json.loads(fi.read())
# 	print da

json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'

d = {}
d["Name"] = "Luke"
d["Country"] = "Canada"
print json.dumps(d, ensure_ascii=False)


# json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'
#
# try:
# 	decoded = json.loads(json_input)
#
# 	# Access data
# 	for x in decoded['persons']:
# 		print x['name']
#
# except (ValueError, KeyError, TypeError):
# 	print "JSON format error"
