# 4. Make a class "Employee". Create "get_data" function inside this class that will take input
# from user employee name ,monthly salary and percentage of tax. Create another function
# "Salary_after_tax" that will deduct 2% tax on monthly salary and return remaining salary.
# There will be another function of "update_tax_percentage" inside this class that will change
# tax percentage (for example initially if it was taken 2% then you may update it to 3%).
# Now again salary will be calculated based on this new tax percentage.

class Employee:
    def __init__(self, name='', salary=0.0, tax=2.0):
        self.name = name
        self.salary = salary
        self.tax = tax

    def get_data(self):
        self.name = input("Enter your name: ")
        self.salary = input("Enter your salary: ")
        self.tax = input("Enter tax")

    def salary_after_tax(self):
        new_salary = self.salary - (self.salary*(self.tax/100))
        return new_salary

    def update_tax_percentage(self):
        self.tax = float(input("Updated tax: "))
        return self.salary_after_tax()

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary:.2f}, Tax Percentage: {self.tax:.2f}"


def main():
    name = input("Enter your name: ")
    salary = float(input("Enter your salary: "))
    tax = float(input("Enter tax percentage: "))

    emp = Employee(name, salary, tax)
    print(emp)

    print(f"Initial salary after tax: {emp.salary_after_tax()}")

    emp.update_tax_percentage()
    print(f"Salary after tax with updated percentage: {emp.salary_after_tax()}")


main()


