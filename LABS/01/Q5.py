# Write a program to take a list and a number input from user and then delete all elements in the list
# less than that number.

numbers = []
size = int(input("Enter size of the list: "))
target = int(input("Enter the target number: "))

print("Enter the elements: ")

for i in range(size):
    num = int(input())
    numbers.append(num)

for number in numbers:
    if number < target:
        numbers.remove(number)

print(numbers)
