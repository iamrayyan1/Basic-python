from tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + " degrees Celsius")

window = Tk()

hotImage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, from_=0, to=100,
              orient=HORIZONTAL,    # orientation of scale
              length=600,
              tickinterval=10,      # adds numeric indicators(separators)
              font=("Consolas",10),
              #showvalue=0      #hides current value
              resolution = 5,    # increment of slider
              troughcolor = 'grey',
              fg = 'red',
              bg = '#10132e')

scale.set(37)   # default value
scale.pack()

coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()