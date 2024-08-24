# libraries are the lines of code that other people, or you have written that you can use  in you code
# share code with others or share your code among your various projects

# module in python is library that have one or more functions and features built into it.
# Encourage reusability of code instead of copy pasting same code again and again

# some modules comes with python
# 'import' keyword is used import a module into your program


# 'random' module   (some file called random.py that already exist) we can use functions inside random library
# random.choice(seq)  # random.py contain function named choice() that takes in parameters

import random

coin = random.choice(["heads", "tails"])
print(coin)


# "from" keyword is used to import specific functions from the module, not the entire module
from random import choice
coin = choice(["heads", "tails"])    # so now we can just call the function directly instead starting it from random.something
print(coin)

# randint(a,b) # another function that comes with random module. It returns backs a random integer between the range a and b
from random import randint
num = randint(1, 100)    # or you could: num = random.randint(1,100)
print(num)

# random.shuffle(x) is another function that takes in list of values and shuffle them up.
import random
cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)



# python also comes with 'statistics' library
# statistics.mean() takes in list of values and provide the avg
import statistics
print(statistics.mean([100,90]))


# command-line arguments: allows you to arguments(input to the program) just when you are executing at the command line
# when we are executing at the command line environment we can write numbers, words and all those things will be stored in program as list

# sys module in python give access to commands we type in terminal
# sys.argv - there is a list variable called argument that stores all the words that human type in command line before pressing enter to run program
import sys
print("hello, my name is ", sys.argv[1])    # it will print whatever word we will write after file name
# sys.argv[0] would store file name

# catching exceptions
try:
    print("hello, my name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")

# another way
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is ", sys.argv[1])

# optimized code
if len(sys.argv) < 2:
    sys.exit("Too few arguments")   # sys.exit will exit the code after printing the statement
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is ", sys.argv[1])


# printing multiple names:
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:  # we have set that it will start from index 1 and go through till the end
    print("hello, my name is ", arg)
# sys.argv[1:-1] by this we will slice off whatever there is at the last index



# 'packages' are the third party libraries that we can install on our systems and can access more functions that other people have implemented for us
# pypi.org can be used to install different packages
# 'pip' is a package manager that comes with python that installs the package by just writing a command
# for example "pip install cowsay" - this will install cowsay package
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])


# APIs - application programming interface, third party and services that you can w
# 'requests' package can be installed through pip allows you to make web requests




# we can also make our own libraries/module/package
import sys
from ownLib import hello  # importing a function from a python file that I wrote

if len(sys.argv) == 2:
    hello(sys.argv[1])




