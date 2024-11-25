from tkinter import *

def submit():
    # print(listbox.get(listbox.curselection()))
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")

    for item in food:
        print(item)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())  # set size of listbox

def delete():
    # listbox.delete(listbox.curselection())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())  # set size of listbox


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",20),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())       # set size of listbox

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

window.mainloop()