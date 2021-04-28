import tkinter as tk
from Database.MPdatabase import PMPDatabase
from Backend.OTPGenerator import Otp
from Backend.sendMail import SendMail


class SetupFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12)

		self.controller = controller
		otpObj = Otp()
		self.generatedOTP = otpObj.generateOTP()

		self.setupFrame = tk.LabelFrame(self, text="Setup")
		self.setupFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.emailLabel = tk.Label(self.setupFrame, text = "Email", font = self.labelFont)
		self.emailLabel.place(relx=0.275, rely=0.1, relwidth=0.45, relheight=0.07)

		# User will enter email for the first time
		self.emailentry = tk.Entry(self.setupFrame, width = 20, bd = 2, font = self.entryFont)
		self.emailentry.place(relx=0.23, rely=0.2, relwidth=0.6, relheight=0.07)
		self.emailentry.delete(0, 'end')

		# Will send OTP to verify Email
		self.sendOtpButton = tk.Button(self.setupFrame, text="Send OTP", command=self.sendOtp,	font=self.labelFont)
		self.sendOtpButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.07)

		# User will enter OTP from the email
		self.otpentry = tk.Entry(self.setupFrame, width=20, font=self.entryFont)
		self.otpentry.place(relx=0.275, rely=0.4, relwidth=0.45, relheight=0.07)
		self.otpentry.insert(0, "Enter OTP here")
		self.otpentry.delete(0, 'end')

		# Will check the entered OTP with generated OTP
		self.otpEnterButton = tk.Button(self.setupFrame, text="Check OTP",	command=lambda: [self.checkOTP()], font=self.labelFont)
		self.otpEnterButton.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)

		self.passLabel = tk.Label(self.setupFrame, text = "Password", font = self.labelFont)
		self.passLabel.place(relx=0.275, rely=0.6, relwidth=0.45, relheight=0.07)

		# User will enter the password for the first time
		self.passentry = tk.Entry(self.setupFrame, show = "*", width = 20, bd = 2, font = self.entryFont)
		self.passentry.place(relx=0.23, rely=0.7, relwidth=0.6, relheight=0.07)
		self.passentry.delete(0, 'end')

		# Will insert email and password to database
		self.enter = tk.Button(self.setupFrame, text = "Enter", font = self.labelFont, command = lambda:[self.insertPass(self.checkOTP())])
		self.enter.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

	# Will check the entered OTP with otpStatus from checkOTP()
	def insertPass(self, otpStatus):
			from Frames.loginFrame import LoginFrame
			try:
				db = PMPDatabase()
				em = self.emailentry.get()
				mp = self.passentry.get()
				if(otpStatus == True):
					print("otp is true")
					db.insertIntoTable(mp, em)
					confirmInsertLabel = tk.Label(self.setupFrame, text = "Successful", bg = 'Grey', font = self.labelFont)
					confirmInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
					confirmInsertLabel.after(2000, confirmInsertLabel.destroy)
					self.controller.show_frame(LoginFrame)
				else:
					print("otp is false")
					errorInsertLabel = tk.Label(self.setupFrame, text = "Try again!", bg = 'Grey', font = self.labelFont)
					errorInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
					errorInsertLabel.after(2000, errorInsertLabel.destroy)
					self.emailentry.delete(0, 'end')
					self.passentry.delete(0, 'end')
					self.otpentry.delete(0, 'end')
			except:
				errorInsertLabel = tk.Label(self.setupFrame, text = "Database Error Try again", bg = 'Grey', font = self.labelFont)
				errorInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
				errorInsertLabel.after(2000, errorInsertLabel.destroy)
			finally:
				self.emailentry.delete(0, 'end')
				self.passentry.delete(0, 'end')
				self.otpentry.delete(0, 'end')

	# Check the OTP with generated OTP and return True or False
	def checkOTP(self):
		enteredOTP = self.otpentry.get()
		if (enteredOTP == self.generatedOTP):
			print("OTP Correct")
			confirmOtpLabel = tk.Label(self.setupFrame, text = "OTP Correct", bg = 'Grey', font = self.labelFont)
			confirmOtpLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmOtpLabel.after(2000, confirmOtpLabel.destroy)
			return True
		else:
			print("OTP Incorrect")
			wrongOtpLabel = tk.Label(self.setupFrame, text = "OTP Incorrect", bg = 'Grey', font = self.labelFont)
			wrongOtpLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			wrongOtpLabel.after(2000, wrongOtpLabel.destroy)
			return False

	# Send mail with generated OTP
	def sendOtp(self):
		mail = SendMail()
		subject = 'OTP Verification'
		message = "Your OTP for Password Manager is:\n" + str(self.generatedOTP)
		mail.send((self.emailentry.get()), subject, message)
		confirmLabel = tk.Label(self.setupFrame, text="Sending Email",	bg='Grey', font=self.labelFont)
		confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		confirmLabel.after(2000, confirmLabel.destroy())
		print("OTP send")