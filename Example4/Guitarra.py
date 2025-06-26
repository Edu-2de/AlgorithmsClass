class Guitarra:
      def __init__(self, brand:str = None, model: str = None, year:int = 0, price:float = 0.0):
            self.brand = brand
            self.model = model
            self.year = year
            self.price = price

      def __str__(self):
            return f"Guitarra: {self.brand} {self.model}, Ano: {self.year}, Preço: R${self.price:.2f}"