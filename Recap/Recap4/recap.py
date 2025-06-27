class Vehicle:
      def __init__(self, make: str = None, model: str = None, speed: float = 0.0, wheel_count: int = 4):
            self.make = make
            self.model = model
            self.speed = speed
            self.wheel_count = wheel_count

      def print_info(self):
            print(f"Make: {self.make}")
            print(f"Model: {self.model}")
            print(f"Speed: {self.speed}")
            print(f"Wheel Count: {self.wheel_count}")

      def accelerate(self, increment: float):
            self.speed += increment
            return self.speed
      
      def brake(self, decrement: float):
            self.speed -= decrement
            if self.speed <= 0:
                  self.speed = 0
            return self.speed

class Automobile(Vehicle):
      def __init__(self, make: str = None, model: str = None, speed: float = 0.0, wheel_count: int = 4, engine_power: float = 0.0):
            super().__init__(make, model, speed, wheel_count)
            self.engine_power = engine_power

      def print_info(self):
            super().print_info()
            print(f"Engine Power: {self.engine_power}")

class Bicycle(Vehicle):
      def __init__(self, make: str = None, model: str = None, speed: float = 0.0, wheel_count: int = 4, number_of_gears: int = 1, luggage_rack: bool = False):
            super().__init__(make, model, speed, wheel_count)
            self.number_of_gears = number_of_gears
            self.luggage_rack = luggage_rack

      def print_info(self):
            super().print_info()
            print(f"Number of Gears: {self.number_of_gears}")
            print(f"Luggage Rack: {self.luggage_rack}")

class Car(Automobile):
      def __init__(self, make: str = None, model: str = None, speed: float = 0.0, wheel_count: int = 4, engine_power: float = 0.0, number_of_doors: int = 4):
            super().__init__(make, model, speed, wheel_count, engine_power)
            self.number_of_doors = number_of_doors

      def print_info(self):
            super().print_info()
            print(f"Number of Doors: {self.number_of_doors}")

class Motorcycle(Automobile):
      def __init__(self, make: str = None, model: str = None, speed: float = 0.0, wheel_count: int = 2, engine_power: float = 0.0):
            super().__init__(make, model, speed, wheel_count, engine_power)

      def print_info(self):
            super().print_info()
            print("This is a motorcycle.")
