# Write a program to take marks of 3 subjects as input by user and store them in a dictionary having appropriate keys. 
# Using that dictionary calculate average and percentage of those marks.

dict = {"Maths": "", "Physics": "", "Chemistry":" "};

for subject in dict.keys():
    dict[subject] = int(input(f"Enter marks of {subject}: "))

sum = 0
for i in dict.values():
    sum += i

avg = sum / len(dict)
percentage = ((sum/300)*100) 

print(f"Student average is: {avg}")
print(f"Student percentage is: {percentage}%")


