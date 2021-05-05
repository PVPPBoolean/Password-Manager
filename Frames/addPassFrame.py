import tkinter as tk
from Database.PDatabase import siteData
from Backend.passwordGenerator import Pgenerator

class AddPassFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		from Frames.homeFrame import HomeFrame
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.sd = siteData()

		self.addPassFrame = tk.LabelFrame(self, text="Add New Password", bd=5)
		self.addPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.siteLabel = tk.Label(self.addPassFrame, text='Enter the website name')
		self.siteLabel.place(relx=0.05, rely=0.1, relheight=0.05)

		self.siteText = tk.Entry(self.addPassFrame, width=25, font=("Helvetica", 10))
		self.siteText.place(relx=0.05, rely=0.15, relheight=0.05, relwidth=0.75)

		self.usernameLabel = tk.Label(self.addPassFrame, text='Enter the username')
		self.usernameLabel.place(relx=0.05, rely=0.2, relheight=0.05)

		self.usernameText = tk.Entry(self.addPassFrame, width=25, font=("Helvetica", 10))
		self.usernameText.place(relx=0.05, rely=0.25, relheight=0.05, relwidth=0.75)

		self.passLabel = tk.Label(self.addPassFrame, text='Enter password')
		self.passLabel.place(relx=0.05, rely=0.3, relheight=0.05)

		self.passText = tk.Entry(self.addPassFrame, width=25, font=("Helvetica", 10))
		self.passText.place(relx=0.05, rely=0.35, relheight=0.05, relwidth=0.75)

		self.pwGenBtn = tk.Button(self.addPassFrame, text = "Generate Password", command=self.generatePass)
		self.pwGenBtn.place(relx=0.05, rely=0.4, relwidth=0.425, relheight=0.1)
		
		self.saveBtn = tk.Button(self.addPassFrame, text = "Save Password", command=self.savePass)
		self.saveBtn.place(relx=0.525, rely=0.4, relwidth=0.425, relheight=0.1)

		self.homeBtn = tk.Button(self.addPassFrame, text = "Home", command=lambda:[controller.show_frame(HomeFrame)], font = self.labelFont)
		self.homeBtn.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)

	def generatePass(self):
		gp = Pgenerator()
		p = gp.generatePass()
		self.passText.delete(0, 'end')
		self.passText.insert(0, p)
		return

	def savePass(self):
		self.sd.insertDataTable(self.siteText.get(), self.usernameText.get(), self.passText.get())
		print(self.siteText.get(), " : ", self.usernameText.get(), " : ", self.passText.get())