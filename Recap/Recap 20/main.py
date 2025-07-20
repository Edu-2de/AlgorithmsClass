class Book():
  def __init__(self, title:str = None, author:str = None, year:int = 0000):
    self.title = title
    self.author = author
    self.year = year
    self.available = True

  def __str__(self):
    return f"{self.title} - {self.author} - {self.year} - {self.available}"
  
class BookPhysical(Book):
  def __init__(self, title:str = None, author:str = None, year:int = 0000, location:str = None):
    super().__init__(title, author, year)
    self.location = location

  def __str__(self):
    return f"{super().__str__()} - {self.location}"
  
class BookDigital(Book):
  def __init__(self, title:str = None, author:str = None, year:int = 0000, url_download:str = None):
    super().__init__(title, author, year)
    self.url_download = url_download

  def __str__(self):
    return f"{super().__str__()} - {self.url_download}"
  
class BookNo():
  def __init__(self, book):
    self.book = book
    self.next = None
    self.previous = None
 
class BookList():
  def __init__(self):
    self.start = None
    self.length = 0

  def addBook(self, newBook):
    noNewBook = BookNo(newBook)
    if self.start:
      aux = self.start
      
    else:
      self.start = noNewBook
      print(f"{self.start.book} added")
    self.length += 1
