import sqlite3


# This class is of MasterTable where app password(hashed) and email is stored in masterTable 
class siteData:
	def __init__(self):
		try:
			self.connect = sqlite3.connect("pwmdatabase.db")
			self.cursor = self.connect.cursor()
		except Exception as e:
			print(e)

	# This will create masterTable (which is done in passwordManagerApp.py file)
	def createDataTable(self):
		dCreate = """
			CREATE TABLE IF NOT EXISTS data (siteName varchar(200), siteUsername varchar(100), sitePassword varchar(100))
		"""
		self.cursor.execute(dCreate)
		self.connect.commit()

	# This will hash the password and insert it along with email entered
	def insertDataTable(self, sn, su, sp):

		dInsert = """
			INSERT INTO data (siteName, siteUsername, sitePassword)
			VALUES (?, ?, ?)
		"""
		self.cursor.execute(dInsert, (sn, su, sp))
		self.connect.commit()

	def searchPass(self, searchString):
		dSearchSiteName = "SELECT * FROM data WHERE siteName LIKE '%{}%'".format(searchString)

		self.cursor.execute(dSearchSiteName)
		c = self.cursor.fetchall()
		if not c:
			return ("")
		return (c[0])

	def deleteDataTable(self, sn):
		dDelete = "DELETE FROM data WHERE siteName = (?)"
		# try:
		self.cursor.execute(dDelete, (sn, ))
		self.connect.commit()
			# print("Deleting")
		# except:
		# 	print("Can't Delete")

	def viewData(self):
		dView = """
			SELECT siteName, siteUsername FROM data 
		"""
		self.cursor.execute(dView)
		allData = self.cursor.fetchall()
		return allData 