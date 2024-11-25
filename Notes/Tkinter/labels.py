from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='healthcare app.png')

label = Label(window, text="Diabetes Prediction System",
              font=("Comic Sans", 40),
              fg='#fbf8cc',
              bg='#10132e',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound=TOP)

label.pack()   # places text to the top center
# label.place(x=50, y=0)   # places text to specific coordinates


window.mainloop()