class Book():
  def __init__(self, title:str = None, author:str = None, year:int = 0000):
    self.title = title
    self.author = author
    self.year = year
    self.available = True

  def __str__(self):
    return f"{self.title} - {self.author} - {self.year} - {self.available}"
  
class BookPhysical():
  def __init__(self, title:str = None, author:str = None, year:int = 0000):
    super().__init__(title, author, year)
    
  
class BookNo():
  def __init__(self, book):
    self.book = book
    self.next = None
    self.previous = None
 
class BookList():
  def __init__(self):
    self.start = None
    self.length = 0
