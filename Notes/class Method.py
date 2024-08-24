# hat.py
# we will pass to the sorting hat the name of a student like "Harry" this sorting hat will tell us what house student should be in
# instance method will always take at least one argument called self
# choosing a house randomly from a list of houses
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in",house)



hat = Hat()
hat.sort("Harry")     # calling instance method using object


# use class when you want to represent a real world entity.
# what if we need just one hat, not like hat1, hat2 etc
# sometimes you don't want objects of class
class Hat:
    houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]  # this is variable of class that is only one and is shared and used by all the objects

    @classmethod
    def sort(cls, name):         # cls is a reference to the class
        house = random.choice(cls.houses)   # houses is no longer an instance varaible rather a class variable so accessible by the class itself
        print(name, "is in",house)


# hat = Hat() Now you don't need this code since you don't need to create any object rather use class directly
Hat.sort("Harry") # using class method using class itself, we don't need objects to call class methods

# two types of methods, class methods and instance methods
# encapsulat ing related data and methods inside class
