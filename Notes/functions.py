# making functions using "def" keyword in python
# main(this is optional in python)
def main():
    name = input("Enter your name: ")  # you cannot use variables that is defined in one function into another function since it doesn't exist in scope.
    hello(name)   # passing arguments
    hello()
# functions can also return value


def hello(to="world"):   # setting default parameters to world in case the no arguments passed while calling function
    print("Hello,", to)


main()  # calling main
