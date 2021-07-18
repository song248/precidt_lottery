from tkinter import *
import model

root = Tk()
 
lbl = Label(root, text="이름")
lbl.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK")
btn.pack()
 
root.mainloop()