# Write a program to take an integer list input from user and count all the even numbers in that list
# and print the count.

numbers = []
count = 0
size = int(input("Enter size of the list: "))

print("Enter the elements: ")

for i in range(0, size):
    num = int(input())
    numbers.append(num)

for i in range(0, size):
    if numbers[i] % 2 == 0:
        count += 1

print(f"Number of even elements in list: {count}")