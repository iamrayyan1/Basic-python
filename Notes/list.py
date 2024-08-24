students = ["Harry", "Sarah", "Ron"]
print(students)  # this would print all the content of list
print(students[0])  # accessing the first value(0 index) on the list
print(students[1])
print(students[2])

# we can use loops to make this process efficient

for student in students:   # in this case we aren't using _ since we are actually using student variable
    print(student)    # using for loop to print all the content of list


# another way
for i in range(len(students)):
    print(students[i])

for i in range(len(students)):
    print(i + 1, students[i])


# dict (another data type - dictionary) - associate something with something else. A 2-D relation unlike lists. Just like human dictionary words with its definition
# though we can use list within list (just like array within array(2D arrays)) instead of dict

# using list (but this is not feasible when we have a lot of things)
students = ["Harry", "Sarah", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# using dict
student = {
    "Harry": "Gryffindor",
    "Sarah": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(student["Harry"])   # list allow you to use actual words instead of index in lists
print(student["Sarah"])
print(student["Ron"])
print(student["Draco"])

# using loop to print dict
for s in student:
    print(s)    # we will only see the student names not the house
    print(student[s])      # this would print just the house
    print(s, student[s])   # this would print both the student names and the house
    print(s, student[s], sep=", ")  # this formats the output changing the default seperator that was " " to ", "




# what if we have more information about the students
# for example their name, house and patronous in this case
# we will use in this case 'list of dict' for storing all the information

students = [
    {"name": "Harry", "age": 23, "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Sarah", "age": 22, "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "age": 21, "house": "Gryffindor", "patronous": "Jack Russel"},
    {"name": "Draco", "age": 20, "house": "Slytherin", "patronous": None}     # None is a keyword in python that means empty/nothing/blank
]
# above is list of students with 4 dict

# now printing it using loops
for student in students:
    print(student["name"])   # we would get just the name of students
    print(student["name"], student["age"], student["house"], student["patronous"], sep=", ")  # now we will get the complete information


# there is still a lot to study about lists and dictionaries(watch separate videos for both)