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
    aux = self.start
    page = PageNo(newPage)
    if aux:
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
