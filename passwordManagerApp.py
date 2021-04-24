from allFrames.forgotPassFrame import ForgotPassFrame
import tkinter as tk
from allFrames.loginFrame import LoginFrame


class PasswordManagerApp(tk.Tk):
    def __init__(self, *args , **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # self.root = tk.Tk()
        # self.root.geometry("350x400+600+150")
        # self.root.title("Password Manager")
        # container = tk.Frame(self.root)
        container = tk.Frame(self)
        # container.place(relx=0, rely=0, relheight=1,relwidth=1)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginFrame, ForgotPassFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
