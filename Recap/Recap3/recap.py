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

class StudentGraduation(Student):
      def __init__(self, code: int = 0, name: str = None, registration: str = None, semester: int = 0):
            super().__init__(code, name, registration)
            self.semester = semester

      def print(self):
            super().print()
            print(f"Semester: {self.semester}")


student1 = Student(1, "Alice", "12345")
student2 = StudentSchool(2, "Bob", "67890", 2023)
student3 = StudentGraduation(3, "Charlie", "54321", 2)

student1.print()
print()
student2.print()
print()
student3.print()
print()
