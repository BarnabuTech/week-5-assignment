# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery  # Battery percentage

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged to {self.battery}%")

    def call(self, number):
        if self.battery > 0:
            print(f"Calling {number} from {self.model}...")
            self.battery -= 5
        else:
            print("Battery dead! Please charge the phone.")

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery}%")

# Subclass: AdvancedSmartphone (Inheritance)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery=100, face_recognition=True):
        super().__init__(brand, model, battery)
        self.face_recognition = face_recognition  # New feature

    def unlock(self):
        if self.face_recognition:
            print(f"{self.model} unlocked using Face ID.")
        else:
            print(f"{self.model} unlocked using PIN.")

# Example usage
phone1 = Smartphone("Samsung", "Galaxyy S22", 80)
phone2 = AdvancedSmartphone("Apple", "iPhone 14 Pro", 90)

phone1.call("1234567890")
phone2.unlock()
phone2.charge(10)
phone1.show_info()
phone2.show_info()
