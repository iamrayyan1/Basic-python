# filing is used to save the information of the program even when you close the program

# list: we can store more than one piece of information. But the content disappear when we close the program

# names.py

names = []
'''
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)
    # or we could names.append(input("What's your name? ")

# sort the list alphabetically
for name in sorted(names):
    print(f"hello, {name}")
'''
# we will lose the information as soon as program ends.
# we use filing to save the information, the way of storing information so the information is there when you come back
'''
# using filing to save names in a file:
name = input("What's your name? ")
# function called 'open' to open a file, it specifies if you have to read, write or append
file = open("names.txt", "w")   # open in write format, if file doesn't exist file will be created. if file exists, the old content will be erased and new content will be written from the start
file.write(name)    # write name in the file
file.close()        # closing the file when done
'''
# append mode is used to update the file

name = input("What's your name? ")
'''
file = open("names.txt", "a")
file.write(f"{name}\n")  # append start with the same line where you left, so to format the text you have to do it on your own.
file.close()
'''
# you can also open and close files 'with' keyword automatically

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
# no need to write close code, it will close the file automatically after indented code finishes

'''
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line.rstrip())   # but after every line extra line is printed. We have used a new line character while storing names and print itself also have a new line character by default
                                    # .rstrip() is used to remove new line character and print name only
'''
# shorter code to read file
with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())


# sorting before printing program:
names = []

with open("names.txt") as file:    # if you are reading file, you don't need to mention it, it is already set to default
    for line in file:
        names.append(line.rstrip())   # adding names to the list but striping the new line character

for name in sorted(names):
    print(f"hello, {name}")

# we could also sort the entire file instead:
with open("names.txt", "r") as file:
    for line in sorted(file, reverse=True):   # reverse is false by default in sorted function, by making it true we can sort it in reverse order
        print("hello", line.rstrip())


# we could store info in csv(comma-seperated values) file if you have to store more than one categories of content.

