from datetime import datetime

class Page():
  def __init__(self, url:str = None, title:str = None):
    self.url = url
    self.title = title
    self.timestamp = None

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
      while(aux):
        
    else:
      print("The list is empty")
