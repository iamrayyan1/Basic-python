# 3. Make a class "Student" and make a function "Print_biodata" inside it. Pass name and age of
# student to constructor. Now access "Print_biodata" function using object to print name and
# age of student.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
           return f"{self.name} of age {self.age}"


def main():
    student = print_boidata()
    print(student)


def print_boidata():
    name = input("Enter your name: ")
    house = input("Enter your age: ")
    return Student(name, house)



main()