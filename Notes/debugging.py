def main():
    h = int(input("Height: "))
    pyramid(h)


def pyramid(n):
    for i in range(1, n+1):
        print("#" * i)
        # or could have done this: print("#" * (i+1))


if __name__ == "__main__":
    main()


# breakpoints: to check what's actually happening in each line of code
# click on any number where you want to place breakpoint. That line will turn red and code execution will stop just before that line



