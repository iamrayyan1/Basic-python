# 2. Write a program to make a simple calculator performing the four basic operations (+, -, *, /) on two
# numbers input by user. The following conditions must be satisfied:
# a) A ‘+’ sign must not be used for addition.
# b) You can only use a maximum of 3 variables. No more variables are allowed.
# c) Your program should ask the user which operation he/she wants to perform and gives the
# output accordingly.

operator = input("Which operation you want to perform: ")
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if operator == "+":
    print(a, operator, b," = ", a-(-b))
elif operator == "-":
    print(a, operator, b," = ", a - b)
elif operator == "*":
    print(a, operator, b," = ", a * b)
elif operator == "/":
    print(a, operator, b," = ", a/b)
else:
    print("Incorrect operation")
