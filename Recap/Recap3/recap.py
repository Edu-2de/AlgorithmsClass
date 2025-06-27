class Student:
      def __init__(self, code: int = 0, name: str = None, registration: str = None):
            self.code = code
            self.name = name
            self.registration = registration
      
      def print(self):
            print(f"Code: {self.code}")
            print(f"Name: {self.name}")
            print(f"Registration: {self.registration}")


class StudentSchool(Student):
      def __init__(self, code: int = 0, name: str = None, registration: str = None, year: int = 0):
            super().__init__(code, name, registration)
            self.year = year

      def print(self):
            super().print()
            print(f"Year: {self.year}")
