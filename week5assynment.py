# Assignment 1: Design Your Own Class (Smartphone)
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def show_details(self):
        return f"{self.brand} {self.model} - Battery: {self.battery_life} hours"

# Inheritance: GamingSmartphone extends Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system

    def show_details(self):
        return f"{self.brand} {self.model} - Battery: {self.battery_life} hours - Cooling: {self.cooling_system}"

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 20)
phone2 = GamingSmartphone("ASUS", "ROG Phone 7", 30, "Advanced Vapor Cooling")

print(phone1.show_details())
print(phone2.show_details())

# Activity 2: Polymorphism Challenge (Vehicle Movement)
class Vehicle:
    def move(self):
        pass  # Placeholder method

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
vehicles = [car, plane, boat]
for v in vehicles:
    print(v.move())
