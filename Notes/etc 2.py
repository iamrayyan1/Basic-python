# UNPACKING - splitting

first, last = input("Enter your name: ").split(" ")  # unpacking it into two values   # we can use _ in place of last since we are not using that variable anywhere, just using it for unpacking
print(f"hello {first} ")


# It turns out there are other ways to unpack variables.
# You can write more powerful and elegant code by understanding how to unpack variables in seemingly more advanced ways.
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")
# Notice how this returns the total value of Knuts.


# What if we wanted to store our coins in a list?
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
# Notice how a list called coins is created. We can pass each value in by indexing using 0, 1, and so on.

# This is getting quite verbose. Wouldn’t it be nice if we could simply pass the list of coins to our function?
# To enable the possibility of passing the entire list, we can use unpacking. In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
# Notice how a * unpacks the sequence of the list of coins and passes in each of its individual elements to total.
# unpacking a list using *, and breaking into individual members of list.


# Suppose that we could pass in the names of the currency in any order? In the text editor window, code as follows:
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")
# Notice how this still calculates correctly.


# When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this as a dictionary.
# In the text editor window, code as follows:
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# Notice how a dictionary called coins is provided. We can index into it using keys, such as “galleons” or “sickles”.


# Since the total function expects three arguments, we cannot pass in a dictionary. We can use unpacking to help with this.
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
# Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.




# *args and **kwargs:
# Recall the "print" documentation we looked at earlier in this course:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# args are positional arguments, such as those we provide to print like print("Hello", "World").
# kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").

# As we see in the prototype for the print function above.
# we can tell our function to expect a presently unknown number positional arguments.
# We can also tell it to expect a presently unknown number of keyword arguments.
# In the text editor window, code as follows:

def f(*args, **kwargs):
    print("Positional:", args)  # printing positional arguments(args) as list/tuple


f(100, 50, 25)
# Notice how executing this code will be printed as positional arguments.

# We can even pass in named arguments. In the text editor window, code as follows:
def f(*args, **kwargs):
    print("Named:", kwargs)   # printing keyword arguments(kwargs) as dict
    print("Positional:", args)

f(galleons=100, sickles=50, knuts=25)
# Notice how the named values are provided in the form of a dictionary.

# Thinking about the print function above, you can see how *objects takes any number of positional arguments.
# You can learn more in Python’s documentation of print.

# args and kwargs allow you to pass multiple arguments without specifying how many. It can be as many or as few you want
# Positional arguments means that they go typically from left to right in order. for eg print(total(100, 50, 25), "Knuts")
# Keyword arguments means named parameters that can be called optionally and individually called by their own name. for eg print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# when writing together, python prescribes to write args first than kwargs

def f(*args, **kwargs):
    print("Named:", kwargs)     # only kwargs as dict will be printed
    print("Positional:", args)  # only args as list will be printed

f(100, 200, galleons=100, sickles=50, knuts=25)


# print() function is also design with *args and **kwargs arguments that's why we are able to print:
# print()
# print("Hello World)
# print("Hello, sep="", end="" "
# range of arguments
# we can also name args and kwargs something else, only single * and name for Positional arguments and double ** and name for keyword arguments


# we can also pass args and kwargs to other functions as parameters while calling them,




# MAPS: there are more tools we can add on toolkit related to types of programming mode python support
# Early on, we began with procedural programming.
# We later revealed Python is an object-oriented programming language.
# We saw hints of functional programming, where functions have side effects without a return value.
# We can illustrate this in the text editor window:
def main():
    yell("This is CS50")


def yell(word):
    print(word.upper())


if __name__ == "__main__":
    main()
# Notice how the yell function is simply yelled.


# Wouldn't it be nice to yell a list of unlimited words? Modify your code as follows:
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
# Notice we accumulate the uppercase words, iterating over each of the words and uppercasing them.
# The uppercase list is printed utilizing the * to unpack it.


# Removing the brackets, we can pass the words in as arguments.
# In the text editor window, code as follows:
def main():
    yell("This", "is", "CS50")


def yell(*words):            # same as def yell(*args):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
# Notice how *words allows for many arguments to be taken by the function.


# python comes with this function called "maps" whose purpose is to allow you to map;
# that is to apply some function to every element of some sequence like a list
# map(function, iterable)
# map allows you to map a function to a sequence of values. In practice, we can code as follows:
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)       # words will be iterated and stored as upper case version inside uppercased list variable
    print(*uppercased)
# map is going to iterate over each of those words, call str.upper on each of those words, and return to me a brand new list containing all of those result together in one list

if __name__ == "__main__":
    main()
# Notice how map takes two arguments.
# First, it takes a function we want applied to every element of a list.
# Second, it takes that list itself, to which we’ll apply the aforementioned function.
# Hence, all words in words will be handed to the str.upper function and returned to uppercased.



# LIST COMPREHENSION:

# IT turns out there is another way we can solve this problem in a more simple way.
# using a feature known as list comprehension

# List comprehensions allow you to create a list on the fly in one elegant one-liner.
# without using a loop, without calling append, but to do everything in one-liner.
# We can implement this in our code as follows:
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]           # same as calling for loop and calling append. all inside one list
    print(*uppercased)


if __name__ == "__main__":
    main()
# Notice how instead of using map, we write a Python expression within square brackets.
# For each argument, .upper is applied to it.



# Taking this concept further, let’s pivot toward another program.
# In the text editor window, type code gryffindors.py and code as follows:
# using list comprehension to filter values in or out of our resulting list
students = [
    {"name": "Hermione", "house": "Gryffindor"},   # list of students(dicts)
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
# Notice we have a conditional while we’re creating our list.
# If the student’s house is Gryffindor, we append the student to the list of names. Finally, we print all the names.

# More elegantly, we can simplify this code with a list comprehension as follows:
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"       # combining everything in one line
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
# Notice how the list comprehension is on a single line!



# FILTER: we can also use filter function to solve above problem
# filter(function, iterable)
# Using Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.
# In the text editor window, code as follows:
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house":  "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)   # applying is_gryffindor to all the students objects inside list
# the function that we pass inside filter should return either true or false. like should I include this, true or false

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):  # to sort a dictionary use this syntax. mentioning what you wanna sort
    print(gryffindor["name"])
# Notice how a function called is_gryffindor is created.
# This is our filtering function that will take a student s, and return True or False depending on whether the student’s house is Gryffindor.
# You can see the new filter function takes two arguments.
# First, it takes the function that will be applied to each element in a sequence—in this case, is_gryffindor.
# Second, it takes the sequence to which it will apply the filtering function—in this case, students.
# In gryffindors, we should see only those students who are in Gryffindor.


# filter can also use lambda functions as follows:
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)  # using lambda function instead of passing is_gryffindor
# making function inside using lambda
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
# Notice how the same list of students is provided.
# You can learn more in Python’s documentation of filter.





# DICTIONARY COMPREHENSION


# We can apply the same idea behind list comprehensions to dictionaries. In the text editor window, code as follows:
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})   # create list of dicts that only contain students of gryffindor

print(gryffindors)   # prints a list of dicts
# Notice how this code doesn’t (yet!) use any comprehensions. Instead, it follows the same paradigms we have seen before.

# We can now apply dictionary comprehensions by modifying our code as follows:
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]   # inside a list comprehension, you need a dict

print(gryffindors)
# Notice how all the prior code is simplified into a single line where the structure of the dictionary is provided for each student in students.


# We can even simplify further as follows:
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}    # one big dictionary, no list
# this time creating dictionary comprehension instead of list comprehension
print(gryffindors)
# it will print as {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor"}
# Notice how the dictionary will be constructed with key-value pairs.






# ENUM: enumerate(iterable, start=0)
# one other function from python toolkit.

# enumerate: mention (a number of things) one by one.

# We may wish to provide some ranking of each student. In the text editor window, code as follows:

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])    # printing name one by one and numbering them by (i+1)
# Notice how each student is enumerated when running this code.

# Utilizing enumeration, we can do the same:
students = ["Hermione", "Harry", "Ron"]
# enumerate(iterable, start=0)
for i, student in enumerate(students):     # enumerate carry both index and value.
    print(i + 1, student)
# Notice how enumerate presents the index and the value of each student.

# You can learn more in Python’s documentation of enumerate.






# GENERATORS AND ITERATORS:

# you program might run out of memory
# In Python, there is a way to protect against your system running out of resources the problems they are addressing become too large.
# In the United States, it’s customary to “count sheep” in one’s mind when one is having a hard time falling asleep.
# In the text editor window, type code sleep.py and code as follows:
n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)
# Notice how this program will count the number of sheep you ask of it.


# We can make our program more sophisticated by adding a main function by coding as follows:
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    main()
# Notice how a main function is provided.

# We have been getting into the habit of abstracting away parts of our code.
# We can call a sheep function by modifying our code as follows:
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()
# Notice how the main function does the iteration.

# We can provide the sheep function more abilities. In the text editor window, code as follows:
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []          # creating an empty list
    for i in range(n):
        flock.append("🐑" * i)       # adding sheeps like this [ , 🐑, 🐑🐑, 🐑🐑🐑, 🐑🐑🐑🐑, 🐑🐑🐑🐑🐑]
    return flock


if __name__ == "__main__":
    main()
# Notice how we create a flock of sheep and return the flock.


# Executing our code, you might try different numbers of sheep such as 10, 1000, and 10000.
# What if you asked for 1000000 sheep, your program might completely hang or crash.
# Because you have attempted to generate a massive list of sheep, your computer may be struggling to complete the computation.

# When inputting a very large value, you program might stop or crash since we ran out of memory or computation

# The yield generator can solve this problem by returning a small bit of the results at a time.
# In the text editor window, code as follows:
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i        # using yield keyword to returning one by one at a time not returning all at ones
# yield basically returns iterator

if __name__ == "__main__":
    main()
# Notice how yield provides only one value at a time while the for loop keeps working.

# You can learn more in Python’s documentation of generators.
# You can learn more in Python’s documentation of iterators.+




