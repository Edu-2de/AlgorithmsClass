class rectangle:
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def __str__(self):
          return f"rectangle with: {self.width} and {self.height}"

      def area(self):
          return self.width * self.height

   
rectangle1 = rectangle(10, 5)

print(rectangle1)
print(f"Area: {rectangle1.area()}")