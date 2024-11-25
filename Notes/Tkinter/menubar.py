from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("Cut has been executed")

def copy():
    print("Copy has been executed")

def paste():
    print("Paste has been executed")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Arial", 12))   # you can also add images next to each commands
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)


window.mainloop()