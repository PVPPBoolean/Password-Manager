from resetPassFrame import ResetPassFrame
import tkinter as tk
from MPdatabase import PMPDatabase
from OTPGenerator import Otp
from sendMail import SendMail

class ForgotPassFrame(tk.Frame):
	def __init__(self, parent, controller):
		from loginFrame import LoginFrame
		tk.Frame.__init__(self, parent)
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.controller = controller
		otpObj = Otp()
		self.generatedOTP = otpObj.generateOTP()

		self.forgotPassFrame = tk.LabelFrame(
			self, text="Forgot Password", bd=5)
		self.forgotPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.emailentry = tk.Entry(self.forgotPassFrame, width=20, font=self.entryFont)
		self.emailentry.place(relx=0.275, rely=0.2, relwidth=0.45, relheight=0.07)
		self.emailentry.insert(0, "Enter your Email")
		self.emailentry.focus()

		self.sendOtpButton = tk.Button(self.forgotPassFrame,
			text="Send OTP",
			command=self.sendOtp,
			font=self.labelFont)
		self.sendOtpButton.place(relx=0.35, rely=0.34, relwidth=0.3, relheight=0.1)

		self.otpentry = tk.Entry(self.forgotPassFrame,
			width=20,
			font=self.entryFont)
		self.otpentry.place(relx=0.275, rely=0.52, relwidth=0.45, relheight=0.07)
		self.otpentry.bind("<Return>", self.shortcuts)
		self.otpentry.insert(0, "Enter OTP here")

		self.otpEnterButton = tk.Button(self.forgotPassFrame, text="Enter",	command=lambda: [self.checkOTP()], font=self.labelFont)
		self.otpEnterButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)
		
		# controller.show_frame(LoginFrame)

		self.backButton = tk.Button(self.forgotPassFrame, text="Back", command=lambda: controller.show_frame(LoginFrame), font=self.labelFont)
		self.backButton.place(relx=0.35, rely=0.72, relwidth=0.3, relheight=0.1)

	def checkOTP(self):
		enteredOTP = self.otpentry.get()
		if (enteredOTP == self.generatedOTP):
			print("OTP Correct")
			self.controller.show_frame(ResetPassFrame)
		else:
			print("OTP Incorrect")

	def sendOtp(self):
		mail = self.emailentry.get()
		print(self.emailentry.get())
		pdb = PMPDatabase()
		if (not (pdb.mailCheck(mail))):
			errorLabel = tk.Label(self.forgotPassFrame, text="Wrong Email entered",	bg='Grey', font=self.labelFont)
			errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			errorLabel.after(2000, errorLabel.destroy)
			return

		self.sendMail(self.emailentry.get())

		confirmLabel = tk.Label(self.forgotPassFrame, text="Sending Email",	bg='Grey', font=self.labelFont)
		confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		confirmLabel.after(2000, confirmLabel.destroy())
		print("OTP send")

	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			print("Enter pressed")
			self.sendOtp()

	def sendMail(self, reciever):
		mail = SendMail()
		subject = 'Forgot Password'
		message = "Your OTP for Password Manager is:\n" + str(self.generatedOTP)
		mail.send(reciever, subject, message)
	
	# def checkEmailValidity(self, email):
	# 	import re
	# 	regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

	# 	if(re.search(regex,email)):
	# 		return True
	# 	return False