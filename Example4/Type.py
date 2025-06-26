from Guitar import Guitar

class Type:
      def __init__(self, type_name: str = None, description: str = None):
            self.type_name = type_name
            self.description = description
            self.guitars = []
      
      def __str__(self):
            return f"Type: {self.type_name}\nDescription: {self.description}\nGuitars: {', '.join([guitar.brand + ' ' + guitar.model for guitar in self.guitars]) if self.guitars else 'No guitars'}"

