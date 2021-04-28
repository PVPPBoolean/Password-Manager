import tkinter as tk
from MPdatabase import PMPDatabase
from OTPGenerator import Otp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ResetPassFrame(tk.Frame):
	def __init__(self, parent, controller):
		from forgotPassFrame import ForgotPassFrame
		tk.Frame.__init__(self,parent)
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.controller = controller

		self.resetPassFrame = tk.LabelFrame(self, text="Reset Password")
		self.resetPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.npLabel = tk.Label(self.resetPassFrame, text = "Enter new Password", font = self.labelFont)
		self.npLabel.place(relx=0.275, rely=0.1, relwidth=0.45, relheight=0.07)

		self.npentry = tk.Entry(self.resetPassFrame, width = 20, show = "*", bd = 2, font = self.entryFont)
		self.npentry.place(relx=0.23, rely=0.2, relwidth=0.6, relheight=0.07)
		self.npentry.delete(0, 'end')

		self.cpLabel = tk.Label(self.resetPassFrame, text = "Enter new Password again", font = self.labelFont)
		self.cpLabel.place(relx=0.275, rely=0.4, relwidth=0.55, relheight=0.07)

		self.cpentry = tk.Entry(self.resetPassFrame, show = "*", width = 20, bd = 2, font = self.entryFont)
		self.cpentry.place(relx=0.23, rely=0.5, relwidth=0.6, relheight=0.07)
		self.cpentry.bind("<Return>", self.shortcuts)
		self.cpentry.delete(0, 'end')
		
		self.enter = tk.Button(self.resetPassFrame, text = "Enter", font = self.labelFont, command = lambda:[self.resetPass()])
		self.enter.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

	# Shortcut for Enter Key
	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			self.resetPass()
	
	# Will check if new password and nw password entered again are same
	# and insert it into database with insertIntoTable() fom MPDatabase
	def resetPass(self):
		try:
			from loginFrame import LoginFrame
			db = PMPDatabase()

			np = self.npentry.get()
			cp = self.cpentry.get()

			if np == cp:
				db.updateIntoTable(np)
				confirmInsertLabel = tk.Label(self.resetPassFrame, text = "Successful", bg = 'Grey', font = self.labelFont)
				confirmInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
				confirmInsertLabel.after(2000, confirmInsertLabel.destroy)
				print("Password Changed Successfully")
				self.controller.show_frame(LoginFrame)
			else:
				perrorInsertLabel = tk.Label(self.resetPassFrame, text = "Password doesn't match with each other", bg = 'Grey', font = self.labelFont)
				perrorInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
				perrorInsertLabel.after(2000, perrorInsertLabel.destroy)
				print("Password doesn't match with each other")
		except Exception as e:
			errorInsertLabel = tk.Label(self.resetPassFrame, text = "Try again", bg = 'Grey', font = self.labelFont)
			errorInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			errorInsertLabel.after(2000, errorInsertLabel.destroy)
			print(e)