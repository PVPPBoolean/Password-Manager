import sys
import tkinter as tk
from tkinter import scrolledtext
import tkinter.ttk as ttk
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame
from Database.PDatabase import siteData


class HomeFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		from Frames.loginFrame import LoginFrame
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.homeFrame = tk.LabelFrame(self, text="Home", bd=5)
		self.homeFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.homeBoxFrame = tk.Frame(self.homeFrame, bd=5)
		self.homeBoxFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

		# self.allPassTreeview = ttk.Treeview(self.homeBoxFrame)
		# self.allPassTreeview.place(relheight=1, relwidth=1)
		# treescrolly = tk.Scrollbar(self.homeBoxFrame, orient="vertical", command=self.allPassTreeview.yview)
		# treescrollx = tk.Scrollbar(self.homeBoxFrame, orient="horizontal", command=self.allPassTreeview.xview)
		# self.allPassTreeview.config(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
		# treescrollx.pack(side='bottom', fill="x")
		# treescrolly.pack(side='right', fill="y")

		self.viewData = scrolledtext.ScrolledText(self.homeBoxFrame, font=self.labelFont)
		self.viewData.place(relheight=1, relwidth=1)

		self.newPassBtn = tk.Button(self.homeFrame, text = "Add New Password", command=lambda:[controller.show_frame(AddPassFrame)], font = self.labelFont)
		self.newPassBtn.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)
		
		self.searchPassBtn = tk.Button(self.homeFrame, text = "Retrive Password", command=lambda:[controller.show_frame(SearchPassFrame)], font = self.labelFont)
		self.searchPassBtn.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)

		self.refreshBtn = tk.Button(self.homeFrame, text = "(@)", command=self.insertScrolledText, font = self.labelFont)
		self.refreshBtn.place(relx=0.95, rely=0.05, relwidth=0.025, relheight=0.025)

		self.insertScrolledText()

	def insertScrolledText(self):
		self.viewData.config(state='normal')
		self.viewData.delete(1.0, 'end')
		VObj = siteData()
		allPass = VObj.viewData()
		heading = "SiteName \t\t | \t Username\n"
		heading += "-"*90+"\n"
		self.viewData.insert('insert', heading)
		for d in allPass:
			info = d[0]+" \t\t | \t "+d[1]+"\n"
			info+="-"*90+"\n"
			self.viewData.insert('insert', info)
		self.viewData.config(state='disabled')