from tkinter import *


class Applications(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creat_Widget()

    def creat_Widget(self):
        pass


root = Tk()
root.geometry("500x500")
app = Applications(master=root)
root = mainloop()
