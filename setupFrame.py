import tkinter as tk
from MPdatabase import PMPDatabase
from OTPGenerator import Otp
from sendMail import SendMail

class SetupFrame(tk.Frame):
	def __init__(self, parent, controller):
		from loginFrame import LoginFrame
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

		self.emailentry = tk.Entry(self.setupFrame, width = 20, bd = 2, font = self.entryFont)
		self.emailentry.place(relx=0.23, rely=0.2, relwidth=0.6, relheight=0.07)

		self.sendOtpButton = tk.Button(self.setupFrame, text="Send OTP", command=self.sendOtp,	font=self.labelFont)
		self.sendOtpButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.07)

		self.otpentry = tk.Entry(self.setupFrame, width=20, font=self.entryFont)
		self.otpentry.place(relx=0.275, rely=0.4, relwidth=0.45, relheight=0.07)
		# self.otpentry.bind("<Return>", self.shortcuts)
		self.otpentry.insert(0, "Enter OTP here")

		self.otpEnterButton = tk.Button(self.setupFrame, text="Check OTP",	command=lambda: [self.checkOTP()], font=self.labelFont)
		self.otpEnterButton.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)

		self.passLabel = tk.Label(self.setupFrame, text = "Password", font = self.labelFont)
		self.passLabel.place(relx=0.275, rely=0.6, relwidth=0.45, relheight=0.07)

		self.passentry = tk.Entry(self.setupFrame, show = "*", width = 20, bd = 2, font = self.entryFont)
		self.passentry.place(relx=0.23, rely=0.7, relwidth=0.6, relheight=0.07)
		# self.passentry.bind("<Return>", self.shortcuts)
		
		self.enter = tk.Button(self.setupFrame, text = "Enter", font = self.labelFont, command = lambda:[self.insertPass(self.checkOTP())])
		self.enter.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

	# def shortcuts(self, event):
	# 	key = event.char
	# 	if key == '\r':
	# 		print("Enter pressed")
	# 		self.insertPass()
	
	def insertPass(self, otpStatus):
			print(otpStatus)
			print(type(otpStatus))
			# status = otpStatus
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
					#ider ereror aa raha hai
					self.controller.show_frame(self.LoginFrame)
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

	def sendOtp(self):
		print(self.emailentry.get())
		self.sendmail(self.emailentry.get())
		confirmLabel = tk.Label(self.setupFrame, text="Sending Email",	bg='Grey', font=self.labelFont)
		confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		confirmLabel.after(2000, confirmLabel.destroy())
		print("OTP send")

	def sendmail(self, reciever):
		mail = SendMail()
		subject = 'OTP Verification'
		message = "Your OTP for Password Manager is:\n" + str(self.generatedOTP)
		mail.send(reciever, subject, message)