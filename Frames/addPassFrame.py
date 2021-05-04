import tkinter as tk


class AddPassFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from Frames.homeFrame import HomeFrame
        self.entryFont = ("Rockwell", 12)
        self.labelFont = ("Rockwell", 12)

        self.addPassFrame = tk.LabelFrame(self, text="Add New Password", bd=5)
        self.addPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.homeBtn = tk.Button(self.addPassFrame, text = "Home", command=lambda:[controller.show_frame(HomeFrame)], font = self.labelFont)
        self.homeBtn.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)


