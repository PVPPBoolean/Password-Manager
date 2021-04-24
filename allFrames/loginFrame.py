import tkinter as tk
from allFrames.forgotPassFrame import ForgotPassFrame
from pwmdatabase import PwmDatabase

class LoginFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		self.labelFont = ("Rockwell", 12, "bold")
		self.entryFont = ("Rockwell", 16)

		self.loginFrame = tk.LabelFrame(self, text="Login", bd=5)
		self.loginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.mpassentry = tk.Entry(self.loginFrame, show = "*", width = 20, font = self.entryFont)
		self.mpassentry.place(relx=0.275, rely=0.384, relwidth=0.45, relheight=0.07)

		self.mpassenter = tk.Button(self.loginFrame, text = "Enter", command = self.checkPass, font = self.labelFont)
		self.mpassenter.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)

		self.forgotPass = tk.Button(self.loginFrame, text = "Forgot Password", command = lambda: controller.show_frame(ForgotPassFrame))
		self.forgotPass.place(relx=0.35, rely=0.7, relwidth=0.35, relheight=0.08)

		self.mpassentry.bind("<Return>", self.shortcuts)

	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			print("Enter pressed")
			self.checkPass()

	def checkPass(self):
		mp = self.mpassentry.get()
		pdb = PwmDatabase()
		if (pdb.loginCheck(mp)):
			confirmLabel = tk.Label(self.loginFrame, text = "Login Successful", bg = 'Grey', font = self.labelFont)
			confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmLabel.after(2000, confirmLabel.destroy)
			return
		errorLabel = tk.Label(self.loginFrame, text = "Wrong Password... try again", bg = 'Grey', font = self.labelFont)
		errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		errorLabel.after(2000, errorLabel.destroy)