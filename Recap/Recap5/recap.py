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
