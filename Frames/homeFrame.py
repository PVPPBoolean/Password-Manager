import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.entryFont = ("Rockwell", 12)
        self.labelFont = ("Rockwell", 12)

        self.homeFrame = tk.LabelFrame(self, text="Home", bd=5)
        self.homeFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.test = tk.Button(self.homeFrame, text = "Enter", font = self.labelFont)
        self.test.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)


