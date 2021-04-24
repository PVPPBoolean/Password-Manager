import tkinter as tk
from pwmdatabase import PwmDatabase

class SetupFrame(tk.Frame):
	def __init__(self, parent, controller):
		from allFrames.loginFrame import LoginFrame
		tk.Frame.__init__(self,parent)
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.setupFrame = tk.LabelFrame(self, text="Setup")
		self.setupFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.emailLabel = tk.Label(self.setupFrame, text = "Email", font = self.labelFont)
		self.emailLabel.place(relx=0.275, rely=0.1, relwidth=0.45, relheight=0.07)

		self.emailentry = tk.Entry(self.setupFrame, width = 20, bd = 2, font = self.entryFont)
		self.emailentry.place(relx=0.23, rely=0.2, relwidth=0.6, relheight=0.07)

		self.passLabel = tk.Label(self.setupFrame, text = "Password", font = self.labelFont)
		self.passLabel.place(relx=0.275, rely=0.4, relwidth=0.45, relheight=0.07)

		self.passentry = tk.Entry(self.setupFrame, show = "*", width = 20, bd = 2, font = self.entryFont)
		self.passentry.place(relx=0.23, rely=0.5, relwidth=0.6, relheight=0.07)
		self.passentry.bind("<Return>", self.shortcuts)
		
		self.enter = tk.Button(self.setupFrame, text = "Enter", font = self.labelFont, command = lambda:[self.insertPass(), controller.show_frame(LoginFrame)])
		self.enter.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			print("Enter pressed")
			self.insertPass()
	
	def insertPass(self):
		try:
			db = PwmDatabase()
			em = self.emailentry.get()
			mp = self.passentry.get()
			db.insertIntoTable(mp, em)
			confirmInsertLabel = tk.Label(self.setupFrame, text = "Successful", bg = 'Grey', font = self.labelFont)
			confirmInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmInsertLabel.after(2000, confirmInsertLabel.destroy)
		except:
			errorInsertLabel = tk.Label(self.setupFrame, text = "Try again", bg = 'Grey', font = self.labelFont)
			errorInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			errorInsertLabel.after(2000, errorInsertLabel.destroy)
		finally:
			self.emailentry.delete(0, 'end')
			self.passentry.delete(0, 'end')