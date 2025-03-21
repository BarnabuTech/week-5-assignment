# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # To be overridden by subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water.")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Calls the appropriate move() method
