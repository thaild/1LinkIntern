
import json
def save_data_file():
	data_file = []
	fi = open("../input3.json").read()
	try:
		fi_data = json.loads(fi)
		for i in range(fi_data.__len__()):
			data_file.append(json.dumps(fi_data[i]))
	except Exception:
		print (Exception.message)
	data = list(set(data_file))
	datatmp = sorted(data, key=lambda i: i['id'])
	print (data_file)
	# for i in range(data_file.__len__()):
	# 	fo.write(data_file[i])
	# 	if i < data_file.__len__() - 1:
	# 		fo.write(',\n')
	#

if __name__ == '__main__':
    save_data_file()
