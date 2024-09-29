# 6. Create a class called "Employee" with properties "name" and "salary". Add a method called
# "calculateBonus" that calculates a bonus amount based on the employee's salary. Managers get
# a bonus equal to 20% of their salary, while developers get a bonus equal to 10% of their salary.
# Then, create two subclasses called "Manager" and "Developer" that inherit from the Employee
# class. The Manager class should have a method called "hire" that logs a message indicating that
# the manager is hiring someone, while the Developer class should have a method called
# "writeCode" that logs a message indicating that the developer is writing code. Finally, create a
# subclass called "SeniorManager" that inherits from the Manager class and that should have the
# "calculateBonus" method to give senior managers a bonus equal to 30% of their salary. [3
# marks]


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return None


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.2)

    def hire(self):
        print(f"{self.name} is Hiring Someone")


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.1)

    def write_code(self):
        print(f"{self.name} is writing code")


class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.3)



