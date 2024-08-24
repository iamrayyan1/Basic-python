'''
with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]})
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        # we could have also: student = {"name": name, "house": house}    # recommended
        students.append(student)


def get_name(student):
    return student["name"]


def get_house(student):
    return student["house"]



for student in sorted(students, key=get_name, reverse=True):     # sorting the list of dictionaries by name, in reverse order
    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")         # sorting the list of dictionaries by house.

for student in sorted(students, key=lambda student: student["name"]):     # instead of making a function that returns the name and calling it inside key, you could have done like this.
    print(f"{student['name']} is in {student['house']}")

# there is a csv library to read and write on csv files to make it easy and efficent