from turtle import color
from Type import Type
from Color import Color

class Guitar:
      def __init__(self, brand:str = None, model: str = None, year:int = 0, price:float = 0.0):
            self.brand = brand
            self.model = model
            self.year = year
            self.price = price
            self.type = Type()
            self.color = []


      def add_color(self, color: Color):
            if isinstance(color, Color):
                  self.color.append(color)
            if color not in self.color:
                  self.color.append(color)
            else:
                  raise TypeError("Color must be an instance of Color class or already added to this guitar")
            
      def remove_color(self, color: Color):
            if color in self.color:
                  self.color.remove(color)
            else:
                  raise TypeError("This color is not associated with this guitar")
      


      def __str__(self):
            return f"Guitar: {self.brand} {self.model}, Year: {self.year}, Price: R${self.price:.2f}, Type: {self.type}, Color: {self.color}"