from tkinter import *

# checkbutton/ checkboxes
def display():
    if x.get() == 1:
        print("You agreed!")
    else:
        print("You lost!")


window = Tk()

x = IntVar()

checkbutton = Checkbutton(window,
                          text="I agree",
                          variable=x,
                          onvalue=1,     # by default these values are 1s and 0s, but we can change them
                          offvalue=0,    # we can replace this to any datatype - any value
                          command=display,
                          font=("Arial", 20),
                          fg='#f8aa1c',
                          bg='#10132e',
                          activebackground='#10132e',
                          activeforeground='green',
                          padx=25, pady=10) # you can also add image
checkbutton.pack()

window.mainloop()