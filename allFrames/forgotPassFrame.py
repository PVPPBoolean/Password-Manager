import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class forgotPass:
    def __init__(self, rootName):
        self.entryFont = ("Rockwell", 8)
        self.labelFont = ("Rockwell", 8)
        self.root = rootName

        self.forgotPassFrame = tk.LabelFrame(self.root, text="Forgot Password", bd=5)
        self.forgotPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.emailentry = tk.Entry(self.forgotPassFrame, width = 20, font = self.entryFont)
        self.emailentry.place(relx=0.275, rely=0.384, relwidth=0.45, relheight=0.07)
        self.emailentry.bind("<Return>", self.shortcuts)

        self.sendOtpButton = tk.Button(self.forgotPassFrame, text = "Send OTP", command = self.sendOtp, font = self.labelFont)
        self.sendOtpButton.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)

    def sendOtp(self):
        if self.emailentry.get() != "manishjalui11@gmail.com":
            errorLabel = tk.Label(self.forgotPassFrame, text = "Email id that you have entered in not found in our system", bg = 'Grey', font = self.labelFont)
            errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
            errorLabel.after(2000, errorLabel.destroy)
            return
        self.sendMail(self.emailentry.get())
        confirmLabel = tk.Label(self.forgotPassFrame, text = "Mail Send succesfully", bg = 'Grey', font = self.labelFont)
        confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
        confirmLabel.after(2000, confirmLabel.destroy)
        print("Otp send")

    def shortcuts(self, event):
        key = event.char
        if key == '\r':
            print("Enter pressed")
            self.sendOtp()

    def sendMail(self,reciever):
        sender = ""
        senderPassword = ""
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender, senderPassword)
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = reciever
        msg['subject'] = 'Forgot Password'
        Message = "You Forgot something quite important!! \n Dw we are here to help you"
        msg.attach(MIMEText(Message, 'plain'))
        text = msg.as_string()
        server.sendmail(sender, reciever, text)