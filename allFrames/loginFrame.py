from allFrames.forgotPassFrame import ForgotPassFrame
import tkinter as tk


class LoginFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		# super().__init__(self, root)
		self.labelFont = ("Rockwell", 12, "bold")
		self.entryFont = ("Rockwell", 16)
		# self.root = rootName
		# self.config(text="Login")
		self.loginFrame = tk.LabelFrame(self, text="Login", bd=5)
		self.loginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.mpassentry = tk.Entry(self.loginFrame, show = "*", width = 20, font = self.entryFont)
		self.mpassentry.place(relx=0.275, rely=0.384, relwidth=0.45, relheight=0.07)

		self.mpassenter = tk.Button(self.loginFrame, text = "Enter", command = self.checkPass, font = self.labelFont)
		self.mpassenter.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)

		self.forgotPass = tk.Button(self.loginFrame, text = "Forgot Password", command = lambda: controller.show_frame(ForgotPassFrame))
		self.forgotPass.place(relx=0.35, rely=0.7, relwidth=0.35, relheight=0.08)

		self.mpassentry.bind("<Return>", self.shortcuts)
		self.mpassentry.bind("<Escape>", self.shortcuts)

	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			print("Enter pressed")
			self.checkPass()
		if key == '\x1b':
			print("escape pressed")
			self.root.destroy()

	def checkPass(self):
		mp = self.mpassentry.get()
		if mp == "admin":
			confirmLabel = tk.Label(self.loginFrame, text = "Login Successful", bg = 'Grey', font = self.labelFont)
			confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmLabel.after(2000, confirmLabel.destroy)
			return
		errorLabel = tk.Label(self.loginFrame, text = "Wrong Password... try again", bg = 'Grey', font = self.labelFont)
		errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		errorLabel.after(2000, errorLabel.destroy)

	# def forgot(self):
	# 	print("Forgot Password")
