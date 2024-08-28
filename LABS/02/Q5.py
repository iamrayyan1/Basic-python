# Write a program to make function employee() meeting following requirements:
# Employee name and monthly salary will be passed to this function. This function will cut 2
# percent tax from salary and display salary after tax with name of employee. If the salary is
# missing in the function call then assign default value 10,000 to salary.


def employee(name, salary = 10000):
    tax = 0.02
    after_tax = salary*(1 - tax)
    print(f"Name: {name}")
    print(f"Salary after taxation: ${after_tax}")


employee("rayyan", 18000)
employee("rayyan")
