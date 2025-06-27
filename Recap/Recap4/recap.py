class Vehicle:
      def __init__(self, make: str, model: str, year: int):
            self.make = make
            self.model = model
            self.year = year

      def print_info(self):
            print(f"Make: {self.make}")
            print(f"Model: {self.model}")
            print(f"Year: {self.year}")

class Car(Vehicle):
      def __init__(self, make: str, model: str, year: int, doors: int):
            super().__init__(make, model, year)
            self.doors = doors

      def print_info(self):
            super().print_info()
            print(f"Doors: {self.doors}")

class Motorcycle(Vehicle):
      def __init__(self, make: str, model: str, year: int, cc: int):
            super().__init__(make, model, year)
            self.cc = cc

      def print_info(self):
            super().print_info()
            print(f"CC: {self.cc}")

vehicle = Vehicle("Generic", "Model", 2020)
car = Car("Toyota", "Camry", 2021, 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 2022, 689)

vehicle.print_info()
print()
car.print_info()
print()
motorcycle.print_info()
print()
