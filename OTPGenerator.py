import random

class Otp:
	def __init__(self):
		self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		self.OTP = ''

	def generateOTP(self):
		for _ in range(6):
			self.OTP += random.choice(self.characters)
		return self.OTP