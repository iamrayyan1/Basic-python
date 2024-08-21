# Write a program that takes a list of numbers as input and returns the sum of all the elements in the list.

numbers = []
total = 0
size = int(input("Enter size of the list: "))

print("Enter the elements: ")

for i in range(size):
    num = int(input())
    numbers.append(num)

for i in range(size):
    total += numbers[i]

print(f"Sum of all elements in list: {total}")