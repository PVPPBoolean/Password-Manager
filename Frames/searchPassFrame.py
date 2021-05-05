import tkinter as tk
from Database.PDatabase import siteData
from Backend.passwordGenerator import Pgenerator


class SearchPassFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		from Frames.homeFrame import HomeFrame
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.Gobj = Pgenerator()
		self.Pobj = siteData()

		self.searchPassFrame = tk.LabelFrame(self, text="Search Password", bd=5)
		self.searchPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.searchLabel = tk.Label(self.searchPassFrame, text='Enter the website name')
		self.searchLabel.place(relx=0.05, rely=0.1, relheight=0.05)

		self.siteText = tk.Entry(self.searchPassFrame, width=25, font=("Helvetica", 10))
		self.siteText.place(relx=0.05, rely=0.15, relheight=0.05, relwidth=0.75)

		self.searchBtn = tk.Button(self.searchPassFrame, text='Q', command=self.searchPass)
		self.searchBtn.place(relx=0.85, rely=0.1375, relheight=0.075, relwidth=0.075)

		self.siteLabel = tk.Label(self.searchPassFrame, text='site name')
		self.siteLabel.place(relx=0.05, rely=0.25, relheight=0.05, relwidth=0.425)

		self.usernameLabel = tk.Label(self.searchPassFrame, text='username')
		self.usernameLabel.place(relx=0.525, rely=0.25, relheight=0.05, relwidth=0.425)
		
		self.passLabel = tk.Label(self.searchPassFrame, text='password')
		self.passLabel.place(relx=0.05, rely=0.35, relheight=0.05, relwidth=0.425)

		self.copyBtn = tk.Button(self.searchPassFrame, text = "Copy to Clipboard", command=self.copy)
		self.copyBtn.place(relx=0.525, rely=0.35, relheight=0.05, relwidth=0.425)

		self.homeBtn = tk.Button(self.searchPassFrame, text = "Home", command=lambda:[controller.show_frame(HomeFrame)], font = self.labelFont)
		self.homeBtn.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)


	def searchPass(self):
		print("searched")
		returnedData = self.Pobj.searchPass(self.siteText.get())
		if returnedData != "": 
			self.siteLabel.config(text = "Site: "+returnedData[0])
			self.usernameLabel.config(text = "Username: "+returnedData[1])
			self.passLabel.config(text = "Password: "+returnedData[2])
		else:
			confirmLabel = tk.Label(self.searchPassFrame, text = "First Search!!!!!!", bg = 'Grey', font = self.labelFont)
			confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmLabel.after(2000, confirmLabel.destroy)

	def copy(self):
		print("password copied")
		p = (self.passLabel['text']).split(" ")
		
		self.Gobj.c2c(p[1])
		self.usernameLabel.config(text = "Username")
		self.siteText.config(text = "Site")
		self.passLabel.config(text = "Password")