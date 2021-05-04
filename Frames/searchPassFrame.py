import tkinter as tk


class SearchPassFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from Frames.homeFrame import HomeFrame
        self.entryFont = ("Rockwell", 12)
        self.labelFont = ("Rockwell", 12)

        self.searchPassFrame = tk.LabelFrame(self, text="Search Password", bd=5)
        self.searchPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.homeBtn = tk.Button(self.searchPassFrame, text = "Home", command=lambda:[controller.show_frame(HomeFrame)], font = self.labelFont)
        self.homeBtn.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)


