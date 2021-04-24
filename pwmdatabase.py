import sqlite3

class PwmDatabase:
	def __init__(self):
		try:
			self.connect = sqlite3.connect("pwmdatabase.db")
			self.cursor = self.connect.cursor()
		except Exception as e:
			print(e)

	def createTable(self):
		qCreate = """
			CREATE TABLE IF NOT EXISTS masterTable (masterPass varchar(100), email varchar(100))
		"""
		self.cursor.execute(qCreate)
		self.connect.commit()

	def insertIntoTable(self, mp, em):
		qInsert = """
			INSERT INTO masterTable (masterPass, email)
			VALUES (?, ?)
		"""
		self.cursor.execute(qInsert, (mp, em))
		self.connect.commit()
	
	def isEmpty(self):
		# return self.cursor.getCount()
		qCount = """
			SELECT COUNT(*) FROM masterTable
		"""
		self.cursor.execute(qCount)
		entries = self.cursor.fetchall()
		if (entries[0][0] == 0):
			return True
		return False
	
	def loginCheck(self, mp):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		# print(data)
		if mp == data[0][0]:
			return True
		return False

	def mailCheck(self, mail):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		print(data[0][1])
		if mail == data[0][1]:
			return True
		return False