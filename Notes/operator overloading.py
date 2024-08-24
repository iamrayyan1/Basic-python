class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        print(f"Galleons: {self.galleons}")
        print(f"Sickles: {self.sickles}")
        print(f"Knuts: {self.knuts}")
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# now you want combine contents of two vaults.
# one way can be:
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)

# but a cool way would manually add up things/objects together directly:
total = potter + weasley
print(total)
# to do this, you need to overload the operator "+"
# the method to overload + is "object.__add__(self, other)"
# it will take two arguments self and other
# self means the object that is on the left of a plus sign
# while other means the objects that is on the right of a plus sign
# similar code is written inside str class to concatenate two strings
# self(or the variable on left) should be the type of variable in which class it is defined
# while other(or the variable on right) can be of any type


# shorts on classes.py