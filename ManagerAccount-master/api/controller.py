import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


class Controller:
	def __init__(self, _client, _worksheet):
		self.client = _client
		self.worksheet = _worksheet

	def authorize_client(self, file_secret):
		scope = [ 'https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name(file_secret, scope)
		self.client = gspread.authorize(creds)
		return self.client

	def getSheet(self, _id, _name):
		accounts = {"accounts": []}
		worksheets = self.client.open_by_key(_id).worksheets()
		wks = filter(lambda x: x._title == _name, worksheets)
		self.worksheet = wks[0]
		# Extract and print all of the values
		list_of_hashes = self.worksheet.get_all_records()
		for row in list_of_hashes:
			if row['ID'] != "":
				account = {'ID': row['ID'], 'Name': row['Name'], 'URL': row['URL']}
				accounts["accounts"].append(account)
		# print json.dumps(accounts)
		print accounts['accounts'].__len__()
		return accounts

	def postSheet(self, _id, _name, accounts):
		worksheets = self.client.open_by_key(_id).worksheets()
		wks = filter(lambda x: x._title == _name, worksheets)
		self.worksheet = wks[0]

		index = 4
		while self.worksheet.cell(index, 1).value != '':
			for acc in accounts:
				if str(acc['account']['ID']) == self.worksheet.cell(index, 1).value:
					account_ud = dict(ID=acc['account']['ID'], Name=acc['account']['Name'],
									  URL=acc['account']['UID'], UID=acc['account']['UID'],
									  LastActive=acc['account']['LastActive'],
									  FollowingNumber=acc['account']['FollowingNumber'],
									  FollowerNumber=acc['account']['FollowerNumber'],
									  PageNumber=acc['account']['PageNumber'],
									  PostNumber=acc['account']['PostNumber'],
									  GroupNumber=acc['account']['GroupNumber'],
									  FriendNumber=acc['account']['FriendNumber'])

					# cell_list = self.worksheet.range('A26:W26')
					# i = 0
					# leng = len(self.worksheet.row_values(6))
					#
					# for cell in cell_list:
					# 		# print val
					# 	cell.value = self.worksheet.row_values(6)[i]
					# 	i += 1

					self.update_account(index, account_ud)
			index += 2

	def update_account(self, index, account):
		# range_build = 'A' + str(index) + ':W' + str(index)
		# cell_list = self.worksheet.range(range_build)
		# cell_list[2].value = account['Name']
		# cell_list[11].value = account['UID']
		# cell_list[14].value = account['LastActive']
		# cell_list[17].value = account['FriendNumber']
		# cell_list[18].value = account['FollowingNumber']
		# cell_list[19].value = account['FollowerNumber']
		# cell_list[20].value = account['PostNumber']
		# cell_list[21].value = account['PageNumber']
		# cell_list[22].value = account['GroupNumber']

		# self.worksheet.update_cells(cell_list)

		# self.worksheet.update_cell(index, 3, account['Name'])
		cell_list = self.worksheet.range('A26:A33')
		cell_values = [1, 2, 3, 4, 5, 6, 7]

		for i, val in enumerate(cell_values):  # gives us a tuple of an index and value
			cell_list[i].value = val  # use the index on cell_list and the val from cell_values

			self.worksheet.update_cells(cell_list)

if __name__ == '__main__':
	# getSheet('1yZW_Omtd-Pypd7gK-0EmUgIbchvQbLu-k0yfumOuyy8')
	pass
