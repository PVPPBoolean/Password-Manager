import tkinter as tk
from allFrames.loginFrame import loginFrame
from allFrames.forgotPassFrame import forgotPass

root = tk.Tk()
root.geometry("350x400+600+150")
root.title("Password Manager")

forgotPassObj = forgotPass(root)
loginObj = loginFrame(root)

root.mainloop()
