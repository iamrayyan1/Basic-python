from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)   # once submitted, it will disable the box

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font = ('Arial', 20),
              fg="#fbf8cc",
              bg="#10132e",
              show="*",   # incase you are typing password
              )
# entry.insert(0, "Enter your username")
entry.pack(side=LEFT)

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Backspace', command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()