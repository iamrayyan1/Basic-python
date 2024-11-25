from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()   # instantiate an instance of a window

window.geometry('500x500')
window.title("Health Care App")

icon = PhotoImage(file='diabetes icon.png')
window.iconphoto(True, icon)

window.config(background="#333333")

window.mainloop()  # places window on computer screen. listen for events