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
      while aux.next:
        aux = aux.next
      aux.next = noNewBook
    else:
      self.start = noNewBook
    print(f"{noNewBook.book} added")
    self.length += 1

  def removeBook(self, title):
    if self.start:
      aux = self.start
      while aux and aux.book.title != title:
        aux = aux.next
      if aux != None:
        self.length -= 1
        print(f"{aux.book} removed")
        if aux == self.start:
          if aux.next:
            self.start = aux.next
          else:
            self.start = None
        else:
          aux.previous.next = aux.next
          if aux.next:
            aux.next.previous = aux.previous
    else:
      print('The list is empty')

  def listAllBooks(self):
    if self.start:
      aux = self.start
      count = 0
      while aux:
        count += 1
        print(f"{count}. book: {aux.book}")
        aux = aux.next
    else:
      print('The list is empty')

  def searchBook(self, authorOrTitle):
    if self.start:
      aux = self.start
      while aux and aux.book.title != authorOrTitle:
        aux = aux.next
      if aux != None:
        print(aux.book)
      else:
        aux = self.start
        while aux and aux.book.author != authorOrTitle:
          aux = aux.next
        if aux != None:
          print(aux.book)
        else:
          print("This book not exist")
    else:
      print("The list is empty")

  def listAvailableBooks(self):
    if self.start:
      aux = self.start
      count = 0
      while aux and aux.book.available == True:
        count += 1
        print(f"{count}. available book: {aux.book}")
        aux = aux.next
    else:
      print("The list is empty")

  def loanBook(self, bookLoan):
    if self.start:
      aux = self.start
      while aux and aux.book.title != bookLoan:
        aux = aux.next
      if aux != None:
        if aux.book.available == True:
          print("You took the book")
          aux.book.available = False
        else:
          print("This book is not available")
      else:
        print("This book not exist")
    else:
      print("The list is empty")

  def returnBook(self, bookReturn):
    if self.start:
      aux = self.start
      while aux and aux.book.title != bookReturn:
        aux = aux.next
      if aux != None:
        if aux.book.available == False:
          print("You return the book")
          aux.book.available = True
        else:
          print("The book has already been returned")
      else:
        "This book not exist"
    else:
      print("The list is empty")

list = BookList()
def menu():
  while True:
    print("\n============= MENU =============")
    print("1. Add physical book")
    print("2. Add digital book")
    print("3. Remove book")
    print("4. List books")
    print("5. Search for book")
    print("6. List available books")
    print("7. Loan book")
    print("8. Return book")
    print("9. Exit")
    print("================================")
    choice = input("Choice: ")
    if choice == '1':
      title = input("Title: ")
      author = input("Author: ")
      year = input("Year: ")
      location = input("Location: ")
      newBook = BookPhysical(title, author, year, location)
      list.addBook(newBook)
    elif choice == '2':
      title = input("Title: ")
      author = input("Author: ")
      year = input("Year: ")
      url_download = input("Url download: ")
      newBook = BookPhysical(title, author, year, url_download)
      list.addBook(newBook)
    elif choice == '3':
      title = input("Title of book you want remove: ")
      list.removeBook(title)
    elif choice == '4':
      list.listAllBooks()
    elif choice == '5':
      titleOrAuthor = input("Type the author or the title of the book: ")
      list.searchBook(titleOrAuthor)
    elif choice == '6':
      list.listAvailableBooks()
    elif choice == '7':
      title = input("Type the title of book that you want loan: ")
      list.loanBook(title)
    elif choice == '8':
      title = input("Type the title of book that you want return: ")
      list.returnBook(title)
    elif choice == '9':
      break


if __name__ == '__main__':
  menu()

