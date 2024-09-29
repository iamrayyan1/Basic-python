# 1. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on
# full fare as a maintenance charge. So total fare for bus instance will become the final amount =
# total fare + 10% of the total fare. [2 marks]

class Vehicle:
    def __init__(self, seating_cap):
        self.seating_cap = seating_cap

    def fare(self):
        return self.seating_cap * 100

class Bus(Vehicle):
    def __init__(self, seating_cap):
        super().__init__(seating_cap)

    def fare(self):
        x = super().fare()
        return x + (x * 0.10)

car = Vehicle(4)
print(f"The fare for the car is {car.fare()}")

bus = Bus(4)
print(f"The fare for the bus is {bus.fare()}")
