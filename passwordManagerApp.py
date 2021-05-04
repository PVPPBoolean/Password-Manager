import tkinter as tk
from Frames.forgotPassFrame import ForgotPassFrame
from Frames.loginFrame import LoginFrame
from Frames.setupFrame import SetupFrame
from Frames.resetPassFrame import ResetPassFrame
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame
from Frames.homeFrame import HomeFrame
from Database.MPdatabase import PMPDatabase


database = PMPDatabase()
database.createTable()

class PasswordManagerApp(tk.Tk):
	def __init__(self, *args , **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.geometry(self, '550x500+600+150')
		tk.Tk.title(self, 'Password Manager')

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (LoginFrame, ForgotPassFrame, SetupFrame, ResetPassFrame, HomeFrame, SearchPassFrame, AddPassFrame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		# This will raise setupFrame if opened for first time(means user doesn't exist)
		# And raise loginFrame the rest of the time
		if(database.isEmpty()):
			self.show_frame(SetupFrame)
		elif(not database.isEmpty()):
			self.show_frame(LoginFrame)

	# Raises Frame in all files
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()