# Write a program to make function employee() meeting following requirements:
# Employee name and monthly salary will be passed to this function. This function will cut 2
# percent tax from salary and display salary after tax with name of employee. If the salary is
# missing in the function call then assign default value 10,000 to salary.



def employee(name, salary = 10000):
    taxrate = 0.02
    salaryaftertax = salary * (1 - taxrate)
    print(f"Name of the Employtee is : {name}")
    print(f"Salary of the employee after taxation is: pkr{salaryaftertax}")

employee("rayyan", 79000)
employee("haris")
