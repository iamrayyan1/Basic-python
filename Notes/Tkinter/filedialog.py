from tkinter import *
from tkinter import filedialog


# OPEN AND READ FILE

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    data = file.read()
    print(data)
    file.close()

window = Tk()

button = Button(window, text="Click Me", command=openFile)
button.pack()

window.mainloop()


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()



# SAVE FILE
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()

