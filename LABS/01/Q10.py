# Write a Python program to get the largest number from a list input from user.

numbers = []
max = None
size = int(input("Enter size of the list: "))

print("Enter the elements: ")

for i in range(0, size):
    num = int(input())
    numbers.append(num)

for number in numbers:
    if max is None or number > max:
        max = number

print(f"Maximum Number in list is: {max}")
