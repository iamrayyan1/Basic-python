# 11. You have a dictionary where each key is a student’s name and each value is a list of
# their grades. You need to perform the following operations:
# • Add a new grade to a student's list of grades.
# • Calculate and print the average grade for a specific student.
# • Add a new student with an initial empty list of grades.
# • Remove a student from the dictionary


def main():

    students = {
        "rayyan": [90,88,92],
        "arham": [82,92,81],
        "malik": [85, 90, 80]
    }

    print("What operation do you wanna perform:\n1. Add a new grade to a student's list of grades.\n2. Calculate and print the average grade for a specific student.\n3. Add a new student with an initial empty list of grades.\n4. Remove a student from the dictionary\n")
    choice = int(input())

    if choice is 1:
        print("Mention student name and grade: ")
        name = input("Name: ").lower()
        grade = int(input("Grade: "))
        add_grade(students, name, grade)
    
    elif choice is 2:
        print("Mention student name: ")
        name = input("Name: ").lower()
        avg_grade(students, name)

    elif choice is 3:
        print("Mention student name: ")
        name = input("Name: ").lower()
        add_student(students, name)

    elif choice is 4:
        print("Mention student name: ")
        name = input("Name: ").lower()
        remove(students, name)

    else:
        print("Invalid Option")
        exit()


    print("\nUpdated student records:")
    for student, grades in students.items():
        print(f"{student}: {grades}")



def add_grade(students, name, grade):
    if name in students:
        students[name].append(grade)
    else:
        print(f"Student {name} not found.")


def avg_grade(students, name):
    if name in students:
        grades = students[name]
        if grades: 
            avg = sum(grades) / len(grades)
            print(f"Average grade for {name} is: {avg:.2f}")
        else:
            print(f"{name} has no grades.")
    else:
        print(f"Student {name} not found.")


def add_student(students, name):
    students[name] = []
    print(f"Student {name} added.")


def remove(students, name):
    if name in students:
        del students[name]
        print(f"Student {name} removed.")


main()






