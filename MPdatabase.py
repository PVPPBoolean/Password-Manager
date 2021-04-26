import sqlite3
import hashlib

class PMPDatabase:
	def __init__(self):
		try:
			self.connect = sqlite3.connect("pwmdatabase.db")
			self.cursor = self.connect.cursor()
		except Exception as e:
			print(e)

	def createTable(self):
		qCreate = """
			CREATE TABLE IF NOT EXISTS masterTable (masterPass varchar(200), email varchar(100))
		"""
		self.cursor.execute(qCreate)
		self.connect.commit()

	def insertIntoTable(self, mp, em):

		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha224(bytesMP).hexdigest()

		qInsert = """
			INSERT INTO masterTable (masterPass, email)
			VALUES (?, ?)
		"""
		self.cursor.execute(qInsert, (hashedMP, em))
		self.connect.commit()

	def updateIntoTable(self, mp):

		mail = self.getMail()		
		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha224(bytesMP).hexdigest()

		qUpdate = """
			UPDATE masterTable SET masterPass = ? WHERE email = ?
		"""
		self.cursor.execute(qUpdate, (hashedMP, mail))
		self.connect.commit()

	def isEmpty(self):
		qCount = """
			SELECT COUNT(*) FROM masterTable
		"""
		self.cursor.execute(qCount)
		entries = self.cursor.fetchall()
		if (entries[0][0] == 0):
			return True
		return False
	
	def loginCheck(self, mp):
		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha224(bytesMP).hexdigest()

		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		# print(data)
		if hashedMP == data[0][0]:
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

	def getMail(self):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		print(data[0][1])
		mail = data[0][1]
		return mail

	def getPass(self):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		print(data[0][0])
		hpass = data[0][0]
		return hpass