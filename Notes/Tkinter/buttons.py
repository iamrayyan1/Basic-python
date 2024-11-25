from tkinter import *

# button = you click it, then it does stuff

count = 0
def click():
    global count
    count = count + 1
    print(count)


window = Tk()

photo = PhotoImage('button icon.png')

button = Button(window,
                text="Click Me",
                command=click,
                font=("Comic Sans", 30),
                fg="#fbf6aa",
                bg="#10132e",
                activeforeground="#fbf6aa",
                activebackground="#f8aa1c",
                state=ACTIVE,
                image=photo,
                compound="bottom",
                )
button.pack()

window.mainloop()