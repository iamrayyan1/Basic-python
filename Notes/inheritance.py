# goal is to

class Student:
    def __init__(self,name, house):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        self.house = house



class Professor:
    def __init__(self,name,subject):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        self.subject = subject



# so here in our situation we are repeating name code in both the classes
# instead you can use inheritance where you can define multiple classes that somehow relate together but not exactly the same


# common class
class Wizard:               # parent class
    def __init__(self,name):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name


class Student(Wizard):              # this means that Student is a subclass of Wizard or inheriting from wizard
    def __init__(self, name, house):
        super().__init__(name)       # super() means reference to super class/parent class of this class that is wizard class. It will have the affect of accessing super class
        self.house = house


class Professor(Wizard):           # this means that Professor is a subclass of Wizard or inheriting from wizard
    def __init__(self,name, subject):
        super().__init__(name)       # calling superclass init method/constructor
        self.subject = subject


wizard = Wizard('Abbot')
student = Student('Harry','Gryffindor')
professor = Professor('John','Science')

# there are many types of inheritance.
# there are a lot more things to cover in OOP. since this is just a basic overview.
# We can create our exception class
# there are hierarchies in exception classes as well


# study about more things as well like, friend classes, polymorphism, etc.

# OPERATOR OVERLOADING:
# implement your own interpretation or functionality of operators
# for example, + is used for addition and concatenation since it is already overloaded by python makers for str class
# more on operator overloading.py


