#  Calculate the body mass index (BMI) of two variables input by the user, where: BMI= weight/(height)^2.

def main():
    weight = float(input("What is your weight? "))
    height = float(input("Your height? "))
    bmi = weight/(height**2)
    print("BMI: ", bmi)


main()
