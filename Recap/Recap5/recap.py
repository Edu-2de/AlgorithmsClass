class Person:
      def __init__(self, __code: int = 0, name: str = None, _address: str = None, __phone: str = None):
            self.__code = __code
            self.name = name
            self._address = _address
            self.__phone = __phone

      def print_name(self) -> str:
            return f"Name: {self.name}"

      def __print_phone(self) -> None:
            print(f"Phone: {self.__phone}")

class Physic(Person):
      def __init__(self, __code: int = 0, name: str = None, _address: str = None, __phone: str = None, __cpf: str = None, age: int = 0, weight: float = 0.0, height: float = 0.0):
            super().__init__(__code, name, _address, __phone)
            self.__cpf = __cpf
            self.age = age
            self.weight = weight
            self.height = height

      def print_cpf(self) -> str:
            return f"CPF: {self.__cpf}"
      
      def calculate_bmi(self) -> float:
            return self.weight / (self.height ** 2)
      
class Legal(Person):
      def __init__(self, __code: int = 0, name: str = None, _address: str = None, __phone: str = None, __cnpj: str = None, __enrollment: str = None, quantity_employees: int = 0):
            super().__init__(__code, name, _address, __phone)
            self.__cnpj = __cnpj
            self.__enrollment = __enrollment
            self.quantity_employees = quantity_employees

      def print_cnpj(self) -> str:
            return f"CNPJ: {self.__cnpj}"
      
      def issue_Note(self, note: str) -> None:
            print(f"Issued Note: {note} for CNPJ: {self.__cnpj}")



person1 = Person(1, "Alice", "123 Main St", "123-456-7890")
person2 = Physic(2, "Bob", "456 Elm St", "987-654-3210", "123.456.789-00", 30, 70.0, 1.75)
person3 = Legal(3, "Charlie", "789 Oak St", "555-555-5555", "12.345.678/0001-90", "1234567890", 50)

print(person1.print_name())
print(person2.print_name())
print(person3.print_name())

print(person2.print_cpf())
print(f"BMI: {person2.calculate_bmi():.2f}")

print(person3.print_cnpj())
person3.issue_Note("Invoice #12345")

#person1.__print_phone()  # This will raise an AttributeError since __print_phone is private
#person2.__print_phone()  # This will also raise an AttributeError
#person3.__print_phone()  # This will also raise an AttributeError since __print_phone is private

# The above code demonstrates the use of private and protected attributes and methods in Python.
# The Person class has a private method __print_phone that cannot be accessed directly from outside the class.
# The Physic and Legal subclasses inherit from Person and can access the protected attribute _address, but not the private attributes or methods.
