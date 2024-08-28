# 6. Write a Python function to multiply all the numbers in a list.

def main():
    numbers = []
    size = int(input("Enter size of the list: "))

    print("Enter the elements: ")
    for i in range(size):
        i = int(input())
        numbers.append(i)


    print(f"Product of numbers in list is: {multiply(numbers)}")


def multiply(numbers):
    product = 1

    for num in numbers:
        product *= num

    return product


main()
    
