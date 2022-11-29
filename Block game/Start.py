from tkinter import *
from subprocess import call

root=Tk()
root.geometry('200x100')
frame = Frame(root)
frame.pack(pady=20,padx=20)

def Open():
    call(["python", "Game.py"])

btn=Button(frame,text='Play Game',command=Open)
btn.pack()

root.mainloop()
