# there are different paradigms of programming languages.
# one way is procedural programming, that we were doing till now. top to bottom
# there is another paradigm called functional programming where we pass functions.
# Object Oriented Programming is another type.
# it makes things easy and simpler and more real life related.

# procedural program.  (Tuples)
name = input("Enter your name: ")
house = input("Enter your house: ")
print(f"{name} from {house}")

# functional program:


def main():
    names = get_name()
    houses = get_house()
    print(f"{names} from {houses}")


def get_name():
    return input("Enter your name: ")


def get_house():
    return input("Enter your house: ")


if __name__ == "__main__":
    main()


# A function called get_student that does all the work:



def main():
    name, house = get_student()
    # student = get_student
    print(f"{names} from {houses}")
    # print(f"{student[0]} from {student[1]}"


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
# now you have to return two variables, name and the house. you have to return student as whole
# We can return multiple values, also we can do this by dictionary
    return name, house      # returning as tuple
    # return (name, house)    returning tuple
    # return [name, house]    returning list
# we can receive these return values as: "name, house = get_student()" in our main function
# Basically we have use "tuple" in this case. tuple is another type of data in python that's a collection of values like x,y or x,y,z
# It is similar to a list but, it's immutable. A list is mutable meaning you go to the location of specific values and change the value there.
# But if you have no intention of changing the values of variables and you want to effectively return multiple values, you can return it as tuple by just using a comma
# immutable means you cannot change the values.
# you are actually returning one variable that is a tuple that contains two values/things
# we use tuple if we don't want to change the values in the variable to avoid error/bugs

if __name__ == "__main__":
    main()


# we can solve this problem another way: using dictionary

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student['name'] = input("Enter your name: ")
    student['house'] = input("Enter your house: ")
    return student
# we can also simplify it as:
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

# dictionaries are mutable like lists(values can be changed)



# there is an yet another way to solve this problem:
# using OOP concepts, classes, objects
# making student a data type
# a class is a blueprint for pieces of data. class allow you to invent your own data type and create it's objects/variables
# objects are called instances of class. we can access variables and functions inside class using (.) notation and objects of classes
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():
    student = Student()
    student.name = input("Enter your name: ")   # objects are used to called the variables/functions inside class
    student.house = input("Enter your house: ")
    return student


# we could also:
# we can standardize what the attributes can be and what kind of values we can set them too
# we can also put methods/functions inside the classes.
# init method is used to create and initialize an object.
class Students:
    def __init__(self, name, house):         # __init__() method is called instance method and it used to initialize contents of an object from a class
        self.name = name                     # basically it's like designing a constructor
        self.house = house                   # every student data type variable or instance will have all the variables and methods inside student class
                                            # this function will always be called when we construct an object
                                          # 'self' argument is a temporary object that give you access to object, you have just created
# __new__() function is used to create an object, not initialize. This automatically exists and you don't need to manipulate this

# by using class you can validate user input. name isn't empty or correct house is entered. By changing init method
    def __init__(self, name, house):       # we can make an variable optional : def __init__(self, name, house=None): house here is optional
        if not name:
            raise ValueError("Missing Name")
            # sys.exit("Missing Name")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


def main():
    ...


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    student = Students(name, house)     # using constructor to pass and set the values
    return student
# constructor call is used construct student object and initialize the variable in it to values we have passed inside the constructor
#   return Student(name, house)
# also place it in try block:
    try:
        return Students(name, house)
    except ValueError:
        ...







# building up the program further: "The String Method": __str__(self)
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"         # you can return any string inside this for eg return "a student"


def main():
    student = get_student()
    print(student)    # this would print the location of student variable
# there are more special methods in python. One called "__str__" that if you define it inside your class, python will automatically call this function
# it is called whenever any time some other function wants to see your object as a string, like in above statement

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Students(name, house)


# there are many such special methods that python support inside class.
# one called: __repr__() which is used for representation of the python object. That can tell a lot about the object


# apart from these special pre-defined method, we can also create our own custom methods.
class Student:
    def __init__(self, name, house, patronus):   # adding patronous
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"         # you can return any string inside this for eg return "a student"

# classes can have custom functions built-in aka methods inside class. All methods take atleast one argument, by convection it is named self but it can be anything
# purpose of self is to have access to current object.
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦎"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🧨"

def main():
    student = get_student()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    patronus = input("Patronus: ")
    return Students(name, house, patronus)



# Properties, Getters and Setters:
# By default, all variables and methods are public by default
# Things are made private to prevent illegal access to any other function outside class.
# Properties is an attribute that have more defense mechanism, more functionality implemented by you to prevent programmers from messing things up.
# A keyword known as "@property" which is technically a function. There are some @ syntax that allows you to decorate functions.
# In python you have decorators which are functions that modify the behavior of other functions
# By using getters and setters, we are trying to prevent programmers from illegally accessing variables outside class
# To set and get a variable, you require to pass through a function or method called getter and setter respectively.
# we can put any error correction inside these function to prevent any wrong input inside these  variables.
# so whenever a programmer will try to modify the value of a variable it will pass through setter function
# Before getter function you need to write a decorator called "@property", while before setter function we write "@house.setter"
# first getter is written than setter.
# The @property decorator allows you to define a method as a property.
# The @house.setter decorator is used to define the setter method for the house property.
# we can keep all our error checking inside setter function, no need to write it inside init function
# whenever we will call ".house" getters and setters will be called so to for convention we use "._house" at some places where these methods are not required
class Student:
    def __init__(self, name, house):
    # we no longer need a error checking code for house and name since we have already mentioned it in setter function which will be called whenever we will try to set or modify the value of the house variable
        self.name = name
        self.house = house

    def __str__(self):     # convert student's object into a string
        return f"{self.name} from {self.house}"

    # Getter - Get some value
    @property
    def house(self):
        return self._house           # we put an _ before instance variable name to differentiate it from original variable

    # Setter - Set some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house        # by convention, we put _ before instance variable while setting the value to differentiate it from the original variable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name



def main():
    student = get_student()
    student.house = "Number Four, Privet Drive" # this will give ValueError since it is not from the list provided inside the setter function of house
    student._house = "Number Four, Privet Drive" # but this ._house wont pass through setter function and since our instance variable name is _house it will set the value and value would change
    # Unfortunately there are no such thing as private public or protected in python to stop from changing the values of variables
    # So the honor system in python is that by convention if an instance variable starts with an "_", please don't touch that variable and break things.
    # _ is meant to signify a convention that this is meant to be private meaning don't touch this. or when a programmer use "__" this really means programmers DO NOT TOUCH IT.
    print(student)


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Students(name, house)



# int is also a class that is biult in python. class int(x, base=10)  class constructor(__int__)
# str is also a class. class str(object='')
# str.lower() is method inside str class
# str.strip([chars]) use to strip characters that is method inside str class
# list is also a built-in class. class list([iterable])
# list.append(x) is a method inside list class that allows you to append something into the list
# dict is a class as well

# type.py
print(type(50))      # type() function is used to tell the data type
print(type("hello, world"))
print(type([]))
print(type(list()))
print(type({}))
print(type(dict()))


# till now we are calling all of our variables instance variables and all of our methods instance methods.
# it turns out, there's other types of variables and methods out there and one of those are called class methods
# "CLASS METHODS"
# sometimes it's not necessary or sensible to associate a function with objects of a class but rather with class itself
# An instance or an object of a class is very specific like a building with same structure but they are little bit different paint and such
# rather sometimes you have functionality related to each of those houses that is exactly the same no matter the object
# sometimes you want some methods related with class itself no matter what the specific object's own values or instances variables are

# there is an another keyword/decorator for this called @classmethod
# @classmethod: it is use to specify that this method is not implicitly an instance method that has access to 'self'(the object itself). rather it is a class method that's not going to have access to self but it does know what class it's inside

# go to "class methods.py"


# applying idea of class method to  clean up one other thing.

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):     # convert student's object into a string
        return f"{self.name} from {self.house}"

    @classmethod           # class method means you can call this method without instantiating a student object first
    def get(cls):          # it will take in cls since it is a class method
        # we will able to call get() without having a student object
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        return cls(name, house)              # returning a new object of the current class


def main():
    student = Student.get()
    print(student)


'''
def get_student():                         # removing get_student from here and placing it inside class to simplify the code 
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Students(name, house)
'''

# beside class methods which are distinct from instance methods which do not have their decorator
# there is yet other types of methods you can have classes in python, they tend to be called static methods.
# static method comes with another decorator called "@staticmethod"


# INHERITANCE
# you can design your class in a hierarchical fashion where you can have one class inherit from or borrow attributes from another class if they have all those in common
# more code on inheritance.py