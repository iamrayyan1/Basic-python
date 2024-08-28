# Write a Python program to calculate the –
# Area of a trapezoid –
# Area of a parallelogram
# Calculate surface volume and area of a cylinder.

def main():
    choice = input("What function do you want to perform:\n1. Area of a trapezoid\n2. Area of a parallelogram\n3. Surface area and volume of a cylinder\n  ")

    if choice == "1":
        a = float(input("Enter base a: "))
        b = float(input("Enter base b: "))
        height = float(input("Enter height: "))
        print(f"Area of the trapezoid: {trapezoid(a, b, height)}")
        
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of the parallelogram: {parallelogram(base, height)}")

    elif choice == "3":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        print(cylinder(radius, height))

    else:
        print("Ainda na hou")

def trapezoid(a, b, height):
    return height * (a + b) / 2

def parallelogram(base, height):
    return base * height

def cylinder(r, h):
    surface_area = 2*3.14*r*(r + h)
    volume = 3.14*(r**2)*h
    return f"The surface area is {surface_area:}\nThe volume is {volume:}"


main()
