from tkinter import *
from tkinter import colorchooser


def ch_cl():
    clrpkr = colorchooser.askcolor(title="Choose a Color")
    bt.config(bg=clrpkr[1])


root = Tk()

bt = Button(root, command=ch_cl)
bt.pack()

root.mainloop()
