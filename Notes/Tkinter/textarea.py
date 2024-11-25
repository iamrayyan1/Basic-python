# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get(1.0, END)
    print(input)

window = Tk()

text = Text(window, height=8, width=20,
            bg='light yellow',
            font=('Ink Free', 25),
            padx=10, pady=10,
            fg='purple')
text.pack()

button = Button(window, text="Click Me!", command=submit)
button.pack()

window.mainloop()
