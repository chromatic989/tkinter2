from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("100x100")
    top.title("toplevel")
    ez = Label(top , text = "this is top window")
    ez.pack()

    top.mainloop()

l = Label(root , text="this is root window")
btn = Button(root , text="click here to open another window", command=topwin)

l.pack()
btn.pack()
root.mainloop()