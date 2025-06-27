from Guitar import Guitar

class Color:
      def __init__(self, name: str = None, hex_value: str = None):
            self.name = name
            self.hex_value = hex_value
            self.guitars = []
      
      def __str__(self):
            return f"Color: {self.name}, Hex: {self.hex_value}"