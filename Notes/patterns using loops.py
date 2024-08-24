#
#
#

for _ in range(3):
    print("#")





def main():
    print_column(3)
    print_row(4)


def print_column(n):
    for _ in range(n):
        print("#")


def print_row(width):
    print("#" * width)



if __name__ == '__main__':
    main()


# complex problem
def main():
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):  # instead we could also do this: print("#" * size) # this would make the code simpler and compact
            # Print brick
            print("#", end="")

        print()      # we use this to get to the new line after each row. paced it outside j loop but inside I loop


# another way
def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(size):
    print("#" * size)


main()






# learn more about patterns to get the concepts of loop.