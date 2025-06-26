from Type import Type

class Guitar:
      def __init__(self, brand:str = None, model: str = None, year:int = 0, price:float = 0.0):
            self.brand = brand
            self.model = model
            self.year = year
            self.price = price

      def __str__(self):
            return f"Guitar: {self.brand} {self.model}, Year: {self.year}, Price: R${self.price:.2f}"