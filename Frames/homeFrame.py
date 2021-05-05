import sys
import tkinter as tk
import tkinter.ttk as ttk
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame

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

		self.allPassTreeview = ttk.Treeview(self.homeBoxFrame)
		self.allPassTreeview.place(relheight=1, relwidth=1)
		treescrolly = tk.Scrollbar(self.homeBoxFrame, orient="vertical", command=self.allPassTreeview.yview)
		treescrollx = tk.Scrollbar(self.homeBoxFrame, orient="horizontal", command=self.allPassTreeview.xview)
		self.allPassTreeview.config(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
		treescrollx.pack(side='bottom', fill="x")
		treescrolly.pack(side='right', fill="y")

		self.newPassBtn = tk.Button(self.homeFrame, text = "Add New Password", command=lambda:[controller.show_frame(AddPassFrame)], font = self.labelFont)
		self.newPassBtn.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)
		
		self.searchPassBtn = tk.Button(self.homeFrame, text = "Retrive Password", command=lambda:[controller.show_frame(SearchPassFrame)], font = self.labelFont)
		self.searchPassBtn.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)
		
		# self.logoutBtn = tk.Button(self.homeFrame, text = "O", command=lambda:[sys.exit()])
		# self.logoutBtn.place(relx=0.95, rely=0.05, relwidth=0.05, relheight=0.05)