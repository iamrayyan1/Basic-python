from tkinter import *

# radio button = similar to checkbox, but you can only select one from a group

food = ['pizza', 'hamburger', 'cheese']

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered burger")
    elif x.get() == 2:
        print("You ordered cheese")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
burgerImage = PhotoImage(file='burger.png')
cheeseImage = PhotoImage(file='cheese.png')

foodImages = [pizzaImage, burgerImage, cheeseImage]

x = IntVar()

for index in range(len(food)):    # this will create 3 radio buttons
    radiobutton = Radiobutton(window,
                              text=food[index],    # adds text to radio buttons
                              variable=x,          # groups the radiobuttons together if they share the same variable
                              value=index,          # assigns each radiobutton a different value
                              padx=25,
                              font=('Impact',20),
                              image=foodImages[index],  # add images to radio button
                              compound=LEFT,           # displays both image and text
                              indicatoron=0,           # eliminate circle indicators
                              width = 375,              # sets width of radio buttons
                              command=order           # set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)


window.mainloop()