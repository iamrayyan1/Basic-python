# Aliza has got 40 Marks in Physics, 78 in Chemistry and 82 in Maths. Take these marks as
# input from user and store them in dictionary with "key as subject name" and "value as marks". By
# accessing data stored in dictionary, print average of his marks and also print the name of subject in
# whichshe got highestmarks.

dict = {"Physics":"", "Chemistry":"", "Maths":""}
physics_marks = int(input("Enter your marks in Physics: "))
chemistry_marks = int(input("Enter your marks in Chemistry: "))
math_marks = int(input("Enter your marks in Maths: "))

dict["Physics"] = physics_marks
dict["Chemistry"] = chemistry_marks
dict["Maths"] = math_marks
# we could also directly store these values without creating extra variables

total = 0
for marks in dict.values():
    total += marks

avg = total / len(dict)   # searched on google for this function

highest_marks = 0
highest_subject = None

for subject, marks in dict.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_subject = subject

print(f"Average Marks of Aliza is: {avg}")
print(f"Highest marks was in {highest_subject}")