from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry("400x400")
upload = Image.open('img.jpg')
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=250, width=300 ,)
label.place(x=40 , y=360)
root.mainloop()