from datetime import datetime

class Page():
  def __init__(self, url:str = None, title:str = None, timestamp=None):
    self.url = url
    self.title = title
    self.timestamp = timestamp

  def __str__(self):
    return f"url:{self.url}, title:{self.title}, accessed in: {self.timestamp}"

class PageNo():
  def __init__(self, page):
    self.page = page
    self.next = None
    self.previous = None

class ListPage():
  def __init__(self):
    self.start = None
    self.actual = None
    self.length = 0

  def add(self, newPage):
    page = PageNo(newPage)
    if self.start:
      aux = self.start
      while aux and aux != self.actual:
        aux = aux.next
      if aux != None:
        aux.next = page
        page.next = None
        page.previous = aux
    else:
      self.start = page
    self.actual = page
    self.length +=1
    print(f"You are in the page: {self.actual.page}")
    

  def backToPreviousPage(self):
    if self.start:
      aux = self.start
      while aux and aux != self.actual:
        aux = aux.next
      if aux != None:
        if aux.previous:
          self.actual = aux.previous
          print(f"You are now in the page: {self.actual.page}")
        else:
          print("No more pages to back")
    else:
      print("The list is empty")

  def goToNextPage(self):
    if self.start:
      aux = self.start
      while aux and aux != self.actual:
        aux = aux.next
      if aux != None:
        if aux.next:
          self.actual = aux.next
          print(f"You are now in the page: {self.actual.page}")
        else:
          print("No more pages to go")
    else:
      print("The list is empty")

  def listAllHistory(self):
    if self.start:
      aux = self.start
      count=0
      while(aux):
        count+=1
        print(f"{count}. {aux.page}")
        aux = aux.next
    else:
      print("The list is empty")

  def searchPage(self, urlOrTitle):
    if self.start:
      aux = self.start
      while aux and aux.page.title != urlOrTitle or aux.page.url != urlOrTitle:
        aux = aux.next
      if aux != None:
        print(aux.page)
      else:
        print("This url or title not exists")
    else:
      print("The list is empty")
    

list = ListPage()
def menu():
  while True:
    print("\n============= MENU =============")
    print("1. Go to new page")
    print("2. Back")
    print("3. Forward")
    print("4. List history")
    print("5. Search page")
    print("6. Remove page")
    print("7. Exit")
    print("================================")
    choice = input("Choice: ")

    if choice == "1":
      url_page = input("What is the URL of the page?")
      title = input("What is the name of the page?")
      date = datetime.now()
      formate = date.strftime("%d/%m/%Y %H:%M")
      new_page = Page(url_page, title, formate)
      list.add(new_page)
    elif choice == "2":
      list.backToPreviousPage()
    elif choice == "3":
      list.goToNextPage
    elif choice == "4":
      list.listAllHistory()
    elif choice == "5":
      titleOrUrl = input("Type url or title of the page: ")
      list.searchPage(titleOrUrl)
    elif choice == "7":
      break

if __name__ == "__main__":
  menu()