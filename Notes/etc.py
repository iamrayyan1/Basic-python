# SET

# set is another data type
# In mathematics, a set is a collection of values where are there no duplicates
# it's not quite a list, it's a more special than that where any duplicates are eliminated for you
# you can use it when you want to eliminate duplicates automatically

# below is the list of dicts
# In this approach, we have a list of dictionaries, each being a student.
# An empty list called houses is created.
# We iterate through each student in students.
# If a student’s house is not already in 'houses' list, we append to our list of houses.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):   # sorting the list alphabetically
    print(house)


# this is the one way we could solve this problem but instead using sets we can automatically remove these duplicates
# It turns out we can use the built-in set features to eliminate duplicates.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# Notice how no checking needs to be included to ensure there are no duplicates. The set object takes care of this for us automatically.
# You can learn more in Python’s documentation of 'set'.

print()


# GLOBAL VARIABLES:
# In other programming languages, there is the notion of global variables that are accessible to any function.
# Global variable is written outside all the functions and can be used by all the functions. and is usually mentioned in top of the code

balance = 0

def main():
    print("Balance:", balance)     # we can read/print/access the global variable from anywhere
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance    # but to write/modify the global variable from a function, you need to make it local in function by global keyword
    balance += n      # local variables only exist inside the function it is defined in


def withdraw(n):
    global balance       # global balance is added to use global functions directly without passing parameter of it inside function
    balance -= n


if __name__ == "__main__":
    main()

# Notice how we now add the functionality to add and withdraw funds to and from balance.
# However, executing this code, we are presented with an error! We see an error called UnboundLocalError.
# You might be able to guess that, at least in the way we’ve currently coded balance and our deposit and withdraw functions,
# we can’t reassign it a value inside a function.
# To interact with a global variable inside a function, the solution is to use the global keyword.
# Notice how the global keyword tells each function that balance does not refer to a local variable: instead, it refers to the global variable we originally placed at the top of our code.
# Now, our code functions!


# using OOP, we can use a class instead of a global variable. we can write the above code like this:
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()

# Notice how we use account = Account() to create an account.
# Classes allow us to solve this issue of needing a global variable more cleanly because these instance variables are accessible to all the methods of this class utilizing self.


# CONSTANTS: In some languages you cannot change the value of python but in python there is no system that prevents us from changing value of constants

# Some languages allow you to create variables that are unchangeable, called “constants”.
# Constants allow one to program defensively and reduce the opportunities for important values to be altered.

MEOWS = 3      # are represented in CAPS

for _ in range(MEOWS):
    print("meow")

# Notice MEOWS is our constant in this case. Constants are typically denoted by capital variable names and are placed at the top of our code.
# Though this looks like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code!
#  Instead, you’re on the honor system: if a variable name is written in all caps, just don’t change it!



# One can create a class “constant”, now in quotes because we know Python doesn’t quite support “constants”.
# class variable as constant
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()

# Because MEOWS is defined outside any particular class method, all of them have access to that value via Cat.MEOWS.



# TYPE HINTS:
# In other programming languages, one expresses explicitly what variable type you want to use.
# As we saw earlier in the course, Python does not require the explicit declaration of types.
# Nevertheless, it’s good practice need to ensure all of your variables are of the right type
# mypy is a program that can help you test to make sure all your variables are of the right type.
# You can install mypy by executing in your terminal window: pip install mypy.

# mypy
def meow(n):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
# You may already see that number = input("Number: )" returns a string, not an int. But meow will likely want an int!

# A type hint can be added to give Python a hint of what type of variable meow should expect.
def meow(n: int):     # type hint is added. it specifies what type of variable should be passed in
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
# but still the error is still there.

# After installing mypy, execute mypy meows.py in the terminal window. mypy will provide some guidance about how to fix this error


# you can provide type hint to all your variables.
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)
# Notice how number is now provided a type hint.
#Again, executing mypy meows.py in the terminal window provides much more specific feedback to you, the programmer.


# We can fix our final error by coding as follows:
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)
# Notice how running mypy how produces no errors because cast our input as an integer.


# Let’s introduce a new error by assuming that meow will return to us a string, or str
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
# Notice how the meow function has only a side effect. Because we only attempt to print “meow”, not return a value, an error is thrown when we try to store the return value of meow in meows.

# We can further use type hints to check for errors, this time annotating the return values of functions. In the text editor window, code as follows:
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
# Notice how the notation -> None tells mypy that there is no return value.

# We can modify our code to return a string if we wish:
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
# Notice how we store in meows multiple strs. Running mypy produces no errors.






# DOCSTRINGS

# A standard way of commenting your function’s purpose is to use a docstring.
def meow(n):
    """Meow n times."""
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
# Notice how the three double quotes designate what the function does.


# You can use docstrings to standardize how you document the features of a function.
def meow(n):
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
# Notice how multiple docstring arguments are included. For example, it describes the parameters taken by the function and what is returned by the function.

# Established tools, such as Sphinx, can be used to parse docstrings and automatically create documentation for us in the form of web pages and PDF files such that you can publish and share with others.



# ARGPARSE - a library to handle complex CLAs

# Suppose we want to use command-line arguments in our program. In the text editor window, code as follows:

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":      # -n means numbers of times. It is a convention to write like this before writing number
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py [-n NUMBER]")
# Notice how sys is imported, from which we get access to sys.argv—an array of command-line arguments given to our program when run.
# We can use several if statements to check whether the use has run our program properly.

# Let’s assume that this program will be getting much more complicated.
# How could we check all the arguments that could be inserted by the user?
# We might give up if we have more than a few command-line arguments!


# Luckily, argparse is a library that handles all the parsing of complicated strings of command-line arguments.
import argparse    # argparse are use to handle complex CLAs

parser = argparse.ArgumentParser()
parser.add_argument("-n")          # command line argument that you want to support in your program
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
# Notice how argparse is imported instead of sys.
# An object called parser is created from an ArgumentParser class.
# That class’s add_argument method is used to tell argparse what arguments we should expect from the user when they run our program.
# Finally, running the parser’s parse_args method ensures that all of the arguments have been included properly by the user.



# We can also program more cleanly
# such that our user can get some information about the proper usage of our code when they fail to use the program correctly.
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
# Notice how the user is provided some documentation. Specifically, a help argument is provided. Now, if the user executes python meows.py --help or -h, the user will be presented with some clues about how to use this program.
# We can further improve this program. In the text editor window, code as follows:

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
# Notice how not only is help documentation included, but you can provide a default value when no arguments are provided by the user.

# more on etc 2.py


