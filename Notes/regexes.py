# regular expression: a patterns to match on some type of data.(defining it)
# capability to compare data or to define a pattern in our code to compare them against the data that we're receiving from someone else.
# whether it's just to validate it or if you want to clean up data.

# using normal syntax: (without regexes)

# email = input("Enter your email: ").strip()          # removing whitespaces
"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""
# a better version:
'''
username, domain = email.split("@")

if username and domain.endswith(".edu"):          # if username have characters
    print("Valid")
else:
    print("Invalid")
'''
# it would take too many boolean expressions and validations to make this code work properly.
# this code is still buggy since there are a lot of loopholes in this code


# there is a library in python called: re
# re library allows us to define the pattern like a pattern for email address and to validate user input against these patterns,
# we can also use this to change user input or to extract useful information

# search function
# re.search(pattern, string, flags = 0)   # pattern you want to search for, string you will search into, fla is se to manipulate the functionality of function
import re
email = input("Enter your email: ").strip()
"""
if re.search("@", email):      # same as the first version done above
    print("Valid")
else:
    print("Invalid")
"""
# there are certain symbols to define pattern in place of characters
# . : any character except a newline
# * : 0 or more repetitions
# + : 1 or more repetitions
# ? : 0 or 1 repetitions
# {m} : m repetitions
# {m,n}} : m-n repetitions
"""
if re.search(".+@.+", email):     # or if re.search("..*@..*",email)
    print("Valid")
else:
    print("Not Valid")
"""
# more complex validation check
"""
if re.search(r".+@.+\.edu", email):  # inorder to use actual "." in your pattern, you need to use it with \ like this "\." and at the start write r meaning raw string
    print("Valid")
else:
    print("Invalid")
"""

# matching start and the end
# ^ : matches the start of the string
# $ : matches the end of the string or just before the newline at the end of the string

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# how to restrict a character: - Set of Characters
# [] = set of characters      # instead of . write this and inside it write characters you wanna allow
# [^] = complementing the set

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid ")

# we can also limit the number of characters using {m} syntax. for example we want 6 character username
if re.search(r"^[^@]{6}@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid ")

# there are some requirements for the characters that are allowed in an email:
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):     # we can define range of characters using - . no commas or anything in between
    print("Valid")           # in this case, we are using set of characters that are allowed
else:
    print("Invalid ")


# character classes: there are some common patterns that are built-in shortcuts for representing some of the same information so you don't have to type all the characters
if re.search(r"^\w+@\w+\.edu$", email):   # instead of [a-zA-Z0-9_] you could write just \w
    print("Valid")
else:
    print("Invalid ")

# some of the built-in character classes:
# \d : decimal digit
# \D : not a decimal digit
# \s : whitespace characters
# \S : not a whitespace character
# \w : word character as well as numbers and underscore
# \W : not a word character


# we can also allow more domain names:
if re.search(r"^\w+@\w+\.(edu|com|gov|org|net)$", email):
    print("Valid")
else:
    print("Invalid ")

# some more symbols:
# A|B : either A or B
# (...) : a group
# (?:...) : non-capturing version

# handling case-insensitive of edu part: one way can be use .lower(), other could making email.lower() inside the argments we pass
# or we could use flags:
# flags we can pass are these: re.IGNORECASE, re.MULTILINE, re.DOTALL
if re.search(r"^\w+@\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid ")

# we can write two regular expressions and allow both of the patterns to work: A|B

# we can make a part of a regular expression optional too using "?" which means 0 or 1 repetitions, means the ()? expression can be there once or cannot be there, both of the things are accepted
# we could also use ()* which means 0 or more repetitions
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid ")

# allowing . in email:
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid ")


# there are still some limitations in our code for validating email address.
# this is the actual code that browsers use to validate email addresses.
# it is very cryptic, long and hard to write

# better solution here instead is to use libraries. Libraries are made to validate email addresses properly using regex

# there are more expressions in re library
# re.match(pattern, string, flags=0)   # it is similar to re.search. you don't need to specify ^ at the start of the string
# re.fullmatch(pattern, string, flags=0)   # it is similar to re.search. you don't need to specify ^ at the start of the string or $ at the end of string


# sometimes we have to clean up the user data to fix things according to the pattern.
# look into format.py file.




