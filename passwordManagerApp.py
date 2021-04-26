import sys
import tkinter as tk
from forgotPassFrame import ForgotPassFrame
from loginFrame import LoginFrame
from setupFrame import SetupFrame
from resetPassFrame import ResetPassFrame
from MPdatabase import PMPDatabase

database = PMPDatabase()
database.createTable()

class PasswordManagerApp(tk.Tk):
	def __init__(self, *args , **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.geometry(self, '350x400+600+150')
		tk.Tk.title(self, 'Password Manager')

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (LoginFrame, ForgotPassFrame, SetupFrame, ResetPassFrame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		if(database.isEmpty()):
			self.show_frame(SetupFrame)
		elif(not database.isEmpty()):
			self.show_frame(LoginFrame)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()