import tkinter as tk
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.entryFont = ("Rockwell", 12)
        self.labelFont = ("Rockwell", 12)

        self.homeFrame = tk.LabelFrame(self, text="Home", bd=5)
        self.homeFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.newPassBtn = tk.Button(self.homeFrame, text = "Add New Password", command=lambda:[controller.show_frame(AddPassFrame)], font = self.labelFont)
        self.newPassBtn.place(relx=0.35, rely=0.42, relwidth=0.3, relheight=0.1)
        
        self.searchPassBtn = tk.Button(self.homeFrame, text = "Retrive Password", command=lambda:[controller.show_frame(SearchPassFrame)], font = self.labelFont)
        self.searchPassBtn.place(relx=0.35, rely=0.62, relwidth=0.3, relheight=0.1)