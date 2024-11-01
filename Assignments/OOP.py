class Animal:
    def __init__(self, identifier, years, environment):
        self.identifier = identifier
        self.years = years
        self.environment = environment
        self.is_available = True
    
    def set_available(self):
        self.is_available = True
    
    def set_quarantine(self):
        self.is_available = False
    
    def show_info(self):
        print(f"Animal Identifier: {self.identifier}")
        print(f"Animal Age: {self.years}")
        print(f"Animal Habitat: {self.environment}")
        status = "Yes" if self.is_available else "In Quarantine"
        print(f"Is {self.identifier} available to be viewed? {status}")
        
class Mammal(Animal):
    def __init__(self, identifier, years, environment, fur_length, diet):
        super().__init__(identifier, years, environment)
        self.fur_length = fur_length
        self.diet = diet
    
    def show_info(self):
        super().show_info()
        print(f"Fur Length: {self.fur_length} cm")
        print(f"Diet Type: {self.diet}")

class Bird(Animal):
    def __init__(self, identifier, years, environment, wingspan, flight_altitude):
        super().__init__(identifier, years, environment)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
    
    def show_info(self):
        super().show_info()
        print(f"Wing Span: {self.wingspan} m")
        print(f"Flight Altitude: {self.flight_altitude} m")

class Reptile(Animal):
    def __init__(self, identifier, years, environment, scale_pattern, is_venomous):
        super().__init__(identifier, years, environment)
        self.scale_pattern = scale_pattern
        self.is_venomous = is_venomous
    
    def show_info(self):
        super().show_info()
        print(f"Scale Pattern: {self.scale_pattern}")
        print(f"Venomous Status: {self.is_venomous}")


# Creating objects
rat = Mammal("Rat", 10, "Savannah", 2.5, "Herbivore")
parrot = Bird("Parrot", 5, "Mountain", 2.0, 3000)
lizard = Reptile("Lizard", 3, "Rainforest", "striped", "Venomous")

print("Before Changing Availability Status:\n")
rat.show_info()
print("\n")
parrot.show_info()
print("\n")
lizard.show_info()

print("\nAfter Changing Availability Status:")
parrot.set_quarantine()
rat.set_available()
lizard.set_quarantine()

print("\n")
rat.show_info()
print("\n")
parrot.show_info()
print("\n")
lizard.show_info()
