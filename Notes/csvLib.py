import csv

# students = []
'''
with open("students.csv") as file:
    reader = csv.reader(file)   # reader function whose purpose is to read a csv file for you and figure out where are the commas, quotes and potential cornered cases and deal with it
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
    # for name, home in reader:
        # students.append({"name": name, "home": home})
for student in sorted(students, key=lambda x: x["name"]):
    print(f"{student['name']} is from {student['home']}")
'''

# we can add a row, which will act as header
# we can also use csvDictReader, which will iterate over file acting dict of column instead of liist.

# reader returns lists
# DictReader returns dictionary
'''
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
        # we could also have done this: students.append(row)

for student in sorted(students, key=lambda x: x["name"]):
    print(f"{student['name']} is from {student['home']}")

# by this things will be printed according to column heading and prevent error.
'''

# WRITING A CSV FILE.
'''
name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
'''

# another way to write in csv file is to use DictWriter. Instead of writing it as list, it will write as dictionary
name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])   # in fieldname write list of columns
    writer.writerow({"name": name, "home": home})


# there are also more file formats where you can read and write in a file

# binary file - 0s and 1s, can store text, graphic and video information

# pillow library that allows you to navigate image files and perform operations on image files.


