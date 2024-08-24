# Syntax Error: It must be fixed before running the program.
# There are more types of errors that we face during the run time.


x = int(input("Enter a number: "))
print(f"X is {x}")
# One thing is wrong in this program since it is possible that the user might enter a letter instead of a number. This will cause a run-time error
# when we enter a string instead of integer we get "ValueError: invalid literal for int() with base 10: 'hello'"

# we can fix this by write code with error handling in mind to handle or catch errors that might happen unexpectedly

# try, except keywords are used to catch errors


try:
    x = int(input("Enter a number: "))
    print(f"X is {x}")
except ValueError:                 # if we face ValueError then this line of code will print
    print("x is not an integer")   # this would not crash the program, but rather will give proper error message to user

# we can catch each type of error individually and write line of code specific for each error, but you can also make generalise exception message that will work for all types of errors except the errors for which you have already written the code

# a better way nto write above code

try:
    x = int(input("Enter a number: "))     # it is the best practice to write as minimum line of code as possible in try block
except ValueError:
    print("x is not an integer")

print(f"X is {x}")   # but as we move out of the try block we face another error called "NameError" because the error is basically happening on the right side of the assignment operator in the try block and when a user enter string, the assignment operator fails to assign the value to x. The error is in the single line that our try block is unable to catch. And then when x was printed after the except block the error will occur

# so to solve this error, there is another keyword of try and except syntax called 'else'
# code under else block will only be executed if no error is caught

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"X is {x}")                  # through else keyword x will only be printed if no exception has occurred. Unlike in previous code where x was printing even when error was occurring


# we could also
while True:        # it will prompt the user again until the user enter the correct value and then the program goes to else block to break the loop and then value is printed
    try:
        x = int(input("Enter a number: "))
        # we could also place break statement here
    except ValueError:
        print("x is not an integer")
    else:
        break              # break statement is used to break out of the loop

print(f"X is {x}")


def main():
    number = get_int()
    print(f"X is {number}")


# make a function
def get_int():
    while True:
        try:
            num = int(input("Enter a number: "))
            # you could also write 'return num' here
            # or simpler would be:
            # return int(input("Enter a number: "))
        except ValueError:
            print("x is not an integer")
        else:
            return num          # return breaks you out of the loop and also returns a value


# 'pass' keyword can be used when you want catch an exception, but you don't want to do anything with it.
def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass      # it will prompt the user again and again to Enter a number until correct number is entered. no error message will be shown when the exception is caught


# we can also mention the prompt as the function argument
def main():
    y = get_num("What's x? ")
    print(f"X is {y}")


def get_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass      # it will prompt the user again and again to Enter a number until correct number is entered. no error message will be shown when the exception is caught


# finally we can also raise exceptions ourselves using the 'raise' keyword.


