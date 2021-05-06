from Frames.resetPassFrame import ResetPassFrame
import tkinter as tk
from Database.MPdatabase import PMPDatabase
from Backend.OTPGenerator import Otp
from Backend.sendMail import SendMail


class ForgotPassFrame(tk.Frame):
	def __init__(self, parent, controller):
		# from loginFrame import LoginFrame
		from Frames.loginFrame import LoginFrame
		tk.Frame.__init__(self, parent)
		#colors
		self.primaryColor = '#6200ee'
		self.secondaryColor = '#3700b3'
		self.backgroundColor = '#000000'
		self.surface1Color = '#121212'
		self.surface2Color = '#212121'
		self.successColor = '#03dac6'
		self.errorColor = '#cf6679'
		self.priTextColor = '#000000'
		self.secTextColor = '#ffffff'
		#fonts
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)
		# To change frame in other functions
		self.controller = controller
		otpObj = Otp()
		self.generatedOTP = otpObj.generateOTP()
		self.forgotPassFrame = tk.LabelFrame(self, text="Forgot Password", bd=5, bg=self.backgroundColor, fg=self.secTextColor)
		self.forgotPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)
		# User will enter email to send OTP to
		self.emailentry = tk.Entry(self.forgotPassFrame, width=20, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor)
		self.emailentry.place(relx=0.275, rely=0.2, relwidth=0.45, relheight=0.07)
		self.emailentry.insert(0, "Enter your Email")
		self.emailentry.focus()
		self.emailentry.delete(0, 'end')
		# Will send OTP to email to verify email
		self.sendOtpButton = tk.Button(self.forgotPassFrame, text="Send OTP", command=self.sendOtp, font=self.labelFont, bg=self.primaryColor, fg=self.secTextColor)
		self.sendOtpButton.place(relx=0.35, rely=0.34, relwidth=0.3, relheight=0.1)
		# User will enter OTP here
		self.otpentry = tk.Entry(self.forgotPassFrame, width=20, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor)
		self.otpentry.place(relx=0.275, rely=0.52, relwidth=0.45, relheight=0.07)
		self.otpentry.bind("<Return>", self.shortcuts)
		self.otpentry.insert(0, "Enter OTP here")
		self.otpentry.delete(0, 'end')
		# Will call chekOTP function and check the OTP
		self.otpEnterButton = tk.Button(self.forgotPassFrame, text="Enter",	command=lambda: [self.checkOTP()], font=self.labelFont, bg=self.primaryColor, fg=self.secTextColor)
		self.otpEnterButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)
		# Will take back to Login Frame if user changed their mind
		self.backButton = tk.Button(self.forgotPassFrame, text="Back", command=lambda: controller.show_frame(LoginFrame), font=self.labelFont,  bg=self.primaryColor, fg=self.secTextColor)
		self.backButton.place(relx=0.35, rely=0.72, relwidth=0.3, relheight=0.1)
	# Will check OTP generated
	# OTP is generated only once in __init__()
	def checkOTP(self):
		enteredOTP = self.otpentry.get()
		if (enteredOTP == self.generatedOTP):
			# print("OTP Correct")
			self.controller.show_frame(ResetPassFrame)
		else:
			# print("OTP Incorrect")
			errorLabel = tk.Label(self.forgotPassFrame, text="OTP incorrect", bg = self.errorColor, fg = self.priTextColor, font=self.labelFont)
			errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			errorLabel.after(2000, errorLabel.destroy)

	# Will check the email with database(since changing email is not allowed) and send OTP to the entered email 
	def sendOtp(self):
		mail = self.emailentry.get()
		# print(self.emailentry.get())
		pdb = PMPDatabase()
		if (not (pdb.mailCheck(mail))):
			errorLabel = tk.Label(self.forgotPassFrame, text="Wrong Email entered",	bg = self.errorColor, fg = self.priTextColor, font=self.labelFont)
			errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			errorLabel.after(2000, errorLabel.destroy)
			return
		# self.sendMail(self.emailentry.get())
		mail = SendMail()
		subject = 'Forgot Password'
		message = "Your OTP for Password Manager is:\n" + str(self.generatedOTP)
		mail.send((self.emailentry.get()), subject, message)

		confirmLabel = tk.Label(self.forgotPassFrame, text="Email Sent", bg = self.successColor, fg = self.priTextColor, font=self.labelFont)
		confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		confirmLabel.after(2000, confirmLabel.destroy())
		# print("OTP send")

	# Shortcut for Enter key 
	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			# print("Enter pressed")
			self.sendOtp()