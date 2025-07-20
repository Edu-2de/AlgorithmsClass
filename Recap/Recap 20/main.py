class Book():
  def __init__(self, title:str = None, author:str = None, year:int = 0000):
    self.title = title
    self.author = author
    self.year = year
    self.available = True

  def __str__(self):
    return f"{self.title} - {self.author} - {self.year} - {self.available}"
 