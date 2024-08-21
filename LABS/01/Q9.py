# Write a Python program to create the multiplication table (from 1 to 10) of a number.

input = int(input("Input a Number: "))

for i in range(1, 11):
    print(f"{input} x {i} = ", input*i)

