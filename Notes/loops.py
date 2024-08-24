
# while loop is used when you don't know when to stop the loop and the loop will only stop when certain condition is false.
# while loop
x = int(input("Enter a number of time you wanna repeat a thing: "))
while x != 0:
    print("Meow")
    x = x - 1

# or

i = 0
while i < 3:
    print("Meow")
    # i = i + 1
    i += 1


# for loop (different from cpp or c)

# list (data type just like int bool float) - list of things(there are few differences between lists and arrays)

for j in [0,1,2]:    # not the best way
    print("Meow")

for j in range(3):   # means 0 , 1 , 2 (not 3)
    print("Meow")

for _ in range(3):   # best design. In this we are not including the variable since we aren't using the variable for anything.
    print("Meow")




print("meow\n" * 3)   # this is a way that only python supports. We can print same thing numerous times with a single line of code
print("meow\n" * 3, end="")   # through this program won't go to new line at the end of the program


# this code of while true, continue and break is used to prompt a user for input again again until it provides the correct required input
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

# or this would be a better approach
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")


# MEOW FUNCTION
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("Meow")



if __name__ == "__main__":
    main()


