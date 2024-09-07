# 8. Take two integer numbers from user as input. Divide these two numbers. If one number is
# being divided by zero (another number) then handle ZeroDivisionError and if entered value
# is wrong (for example, a string) then handle ValueError.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

try:
    result = num1 / num2

except ZeroDivisionError:
    print("Division by zero!!!.")
except ValueError:
    print("Invalid input.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")

else:
    print(f"The result is {result}")


