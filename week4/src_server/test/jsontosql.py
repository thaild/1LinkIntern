import json, sqlite3 as sql



def load():
	sql_path = "E:\\1link\week4\src_server\Students.db"
	conn = sql.connect(sql_path)
	query = "insert into Student values (?,?,?,?,?,?,?)"
	json_data = open('E:\\1link\week4\src_server\input2.json').read()
	list = json.loads(json_data)

	columns = ['id', 'name', 'gender', 'add', 'math', 'physics', 'chemistry']
	for data in list:
		keys = tuple(data[c] for c in columns)
		c = conn.cursor()
		c.execute(query, keys)
		c.close()


def view():
	cur = conn.cursor()
	cur.execute("SELECT * FROM Std_tmp")

	while True:
		row = cur.fetchone()
		if row == None: break
		print (row)
	cur.close()


if __name__ == '__main__':
	load()
	view()
