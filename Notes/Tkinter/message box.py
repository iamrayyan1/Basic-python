from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info message', message='You are a person')
    #messagebox.showwarning(title='WARNING', message='You have Diabetes')
    #messagebox.showerror(title='ERROR', message='Something went wrong')

    """
    ans = messagebox.askquestion(title='ask question', message='Do you like pie?')
    if ans == 'yes':
        print("I like pie too")
    else:
        print("why do you not like pie")
    """

    """
    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
        print("You clicked OK")
    else:
        print("You clicked Cancel")
    """

    """
    if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?'):
        print("You clicked Retry")
    else:
        print("You clicked Cancel")
    """

    ans = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code', icon='info')
    if ans == 'True':
        print('You like to code')
    elif ans == 'False':
        print('Then why are you watching this video')
    else:
        print("You have dodged the question")


window = Tk()


button = Button(window, command=click, text='ClickMe')
button.pack()



window.mainloop()