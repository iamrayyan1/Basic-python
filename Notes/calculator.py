"""
x = input("Enter a number X: ")
y = input("Enter a number Y: ")
z = x + y  # this won't add the number instead it will concatenate 2 strings.
z = int(x) + int(y)  # this will add integers properly
print(z)

# by default in python input function take in input as string, we can convert it to integer while taking input
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print(a + b)

# float
a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))
print(a + b)  # float result
print(round(a + b))  # rounding numbers, we can also specify the number of dp we want to round upto

print(f"{a + b:,}")

c = round(a / b, 2)
print(f"{c:.2f}")  # another way to round off to certain dp
"""





def main():
    x = int(input("Enter a number X: "))
    print("x squared is", square(x))


def square(n):
    return n + n
#   return n ** 2    n raised to power 2
#   return pow(n, 2) another way of writing

if __name__ == "__main__":
    main()
