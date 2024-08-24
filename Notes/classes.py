# why we should use classes

class Package:
    def __init__(self, id, sender, receiver, weight):      # self refers to the current object?new instance of class we are creating
        self.id = id                           # all these variables self.id, self.sender and so on are called instance variable
        self.sender = sender                   # for example, number is sent as argument by constructor and is assigned to self.number
        self.receiver = receiver
        self.weight = weight

# instance methods: we can also combine functions that will common across all packages
    def __str__(self):
        return f'Package {self.id}: {self.sender} to {self.receiver}, {self.weight}kg'

# we can use instance methods to calculate the cost of shipping.
    def calculate_cost(self, cost_per_kg):     # self represents the object that has called the method
        return cost_per_kg * self.weight


def main():
#   Packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    # But this is a bad design we could encapsulate all the info of package into a class. While each package acts as an object

    packages = [
        Package(1, 'Alice', 'Bob', 10),
        Package(2, 'Bob', 'Charlie', 5),
    ]
    for package in packages:
        # print(f"Package {package.id}: {package.sender} to {package.receiver}, {package.weight}kg")
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")


main()