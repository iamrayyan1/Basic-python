"""
# > , < , == , != , or , AND , if , else , elif

x = int(input("What's X? "))
y = int(input("What's Y? "))

if x < y:
    print("x is less than y")

elif x > y:
   print("x is greater than y")

else:       # instead of elif x == y: ; we can use this since this is last condition left
    print("x is equal to y")

# if you only "if" it will go along each loop, if we use "elif" instead it will go out of loop once condition is met it won't go to other if statements.

# use of "or" keyword
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# "!=" / "==" simpler version
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# "AND" keyword
"""


# Program: grade.py

score = int(input("What's your score? "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif score >= 60 and score < 70:   # CAN ALSO WRITE LIKE THIS.
    print("D")
else:
    print("F")


# another approach(better)

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("F")
# here in this approach it's necessary to use elif or else it will print all the grades





# Program: parity.py
# + , - , * , / , %

x = int(input("What's X? "))

if x % 2 == 0:   # gives reminder
    print("Even")
else:
    print("Odd")

# improved of above program

def main():
    x = int(input("What's X? "))
    if isEven(x):
        print("Even")
    else:
        print("Odd")


def isEven(n):
    if n % 2 == 0:
        return True          # we can return bool values, either true(1) or false(0)
    else:
        return False


# above function can be simplified to
def isEven(n):
    return True if n % 2 == 0 else False

#or
def isEven(n):
    return (n % 2 == 0)            # another way is to just return the boolean expression itself


main()



# "match" keyword

# Program: house.py to explain use of match

name = input("What's you name? ")

if name == "Harry":
    print("gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Sarah":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who")

# instead we could simplify like this:
if name == "Harry" or name == "Hermione" or name == "Sarah":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who")

# another approach with keyword "match" just like switch case
name = input("What's you name? ")

match name:
    case "Harry":
        print("gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Sarah":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                       # _: is equivalent to default or else
        print("Who")

# To tighten the code:
match name:
    case "Harry" | "Hermione" | "Sarah":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")

