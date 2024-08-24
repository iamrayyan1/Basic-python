# formating user's name.
# David Malan or Malan, David, people can type both, so it's important to format or clean up the data according to the pattern you have set.

name = input("Enter your name: ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello,{name}")

# this could be also done to format or clean up the csv file, but you have to first open to read the file

# still the above code is buggy and fragile with many loopholes.

# for example, there is a possibility that user might forget to leave a space after comma as a result it will lead to value error.
# so by using regex we can make " " after comma optional using "?" symbol.
import re

if re.search(r"^.+, ?.+$", name):
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello,{name}")

# we can get more information from re.search by specifying a variable than an assignment operator and get back more precise answers to what has been found when searched for
# using re library we can also capture things
# using parantheses we can capture things
# a reverse of this would be: (?:...) : non-capturing version

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:             # if matches true: meaning if the format is followed.
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello,{name}")

# matches captures some of the user's input. things inside (...) are being captured and stored in matches. we can access these values using matches.groups()

# we could also do this:
name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.groups(1)   # things inside first parantheses
    first = matches.group(2)   # things inside second parantheses
    name = f"{first} {last}"
print(f"Hello,{name}")

# a better design:
name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)          # added ? to allow both "Malan, David" and "Malan,David"
if matches:
    name = matches.groups(2) + " " + matches.group(1)        # directly using variables
print(f"Hello,{name}")

# dealing whitespaces:
name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)          # added * to allow both "Malan, David" and "Malan,David" and also will deal with whitespaces between the characters
if matches:
    name = matches.groups(2) + " " + matches.group(1)        # directly using variables
print(f"Hello,{name}")

# clean up even further using Walrus Operator: ":="
name = input("Enter your name: ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):      # using := to assign something to a variable and also ask a if condition, both things on the same line
    name = matches.groups(2) + " " + matches.group(1)
print(f"Hello,{name}")


# we can also extract user's input inorder to answer some question.
# look into extract.py file.

